import os
import json
import yaml
import glob
from datetime import datetime, timezone
from collections import Counter

# SIMPLE JSON LOGGER (writes to logs.jsonl line-by-line)
def log(level, message, **extra):
    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": level.upper(),
        "message": message,
    }
    if extra:
        log_entry.update(extra)
    with open("logs.jsonl", "a", encoding="utf-8") as lf:
        lf.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

# SAFE GET helper to avoid KeyErrors
def safe_get(dct, *keys):
    cur = dct
    for k in keys:
        if not isinstance(cur, dict) or k not in cur:
            return None
        cur = cur[k]
    return cur

# PARSE YAML TO EXTRACT ENDPOINT METADATA
def parse_yaml(doc):
    meta = {
        "title": safe_get(doc, "info", "title"),
        "version": safe_get(doc, "info", "version"),
        "securitySchemes": list((safe_get(doc, "components", "securitySchemes") or {}).keys()),
        "paths": {},
        "method_count": {}
    }

    method_counter = Counter()
    paths = doc.get("paths", {})

    valid_methods = {"get", "post", "put", "delete", "patch", "options", "head"}

    for path, methods in paths.items():
        meta["paths"][path] = {}

        # methods may include 'parameters' at path level; ensure it's a dict
        if not isinstance(methods, dict):
            continue

        for method, content in methods.items():
            if not isinstance(method, str):
                continue
            mlow = method.lower()
            if mlow not in valid_methods:
                continue

            method_counter[mlow.upper()] += 1

            info = {
                "summary": content.get("summary"),
                "responses": list((content.get("responses") or {}).keys()),
                "security": []
            }

            if isinstance(content.get("security"), list):
                for sec_obj in content["security"]:
                    if isinstance(sec_obj, dict):
                        info["security"].extend(list(sec_obj.keys()))

            meta["paths"][path][mlow] = info

    meta["method_count"] = dict(method_counter)
    return meta

# BUILD SUMMARY RESULT ACROSS ALL FILES
def build_summary(all_meta):
    method_counter = Counter()
    auth_methods = set()
    with_resp = []
    without_resp = []
    total = 0

    for fname, meta in all_meta.items():
        for path, methods in meta.get("paths", {}).items():
            for method, info in methods.items():
                total += 1
                method_counter[method.upper()] += 1

                if info.get("responses"):
                    with_resp.append({"file": fname, "path": path, "method": method})
                else:
                    without_resp.append({"file": fname, "path": path, "method": method})

                for s in info.get("security", []):
                    auth_methods.add(s)

        for s in meta.get("securitySchemes", []):
            auth_methods.add(s)

    return {
        "total_endpoints": total,
        "method_count": dict(method_counter),
        "endpoints_with_response": with_resp,
        "endpoints_without_response": without_resp,
        "auth_methods": list(auth_methods)
    }

# MAIN
def main():
    os.makedirs("output", exist_ok=True)

    yaml_files = glob.glob("yamls/*.yaml") + glob.glob("yamls/*.yml")
    # process all files (no top-5 limit)
    if not yaml_files:
        log("error", "No YAML files found in yamls/ folder")
        print("No YAML files found!")
        return

    log("info", "YAML files found", count=len(yaml_files))
    print(f"Found {len(yaml_files)} YAML file(s) to parse.")

    all_meta = {}

    for filepath in yaml_files:
        fname = os.path.basename(filepath)
        try:
            with open(filepath, "r", encoding="utf-8") as fp:
                doc = yaml.safe_load(fp)
            meta = parse_yaml(doc)
            all_meta[fname] = meta
            log("info", "Parsed file", file=fname)
            # quick terminal feedback per file
            print(f"Parsed: {fname}  methods: {meta.get('method_count', {})}")
        except Exception as e:
            log("error", "Failed to parse", file=fname, error=str(e))
            print(f"Failed to parse {fname}: {e}")
            continue

    # Save metadata
    with open("output/metadata.json", "w", encoding="utf-8") as f:
        json.dump(all_meta, f, indent=2, ensure_ascii=False)
    log("info", "metadata.json created")
    print("Wrote output/metadata.json")

    # Summary
    summary = build_summary(all_meta)
    with open("output/summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    log("info", "summary.json created", total_endpoints=summary["total_endpoints"])

    # final terminal summary
    print("\nOverall summary:")
    print(" total endpoints:", summary["total_endpoints"])
    print(" method counts:", summary["method_count"])
    print(" auth methods:", summary["auth_methods"])
    print(" outputs written to output/ and logs.jsonl")
    print("✔ Done!")

if __name__ == "__main__":
    main()
