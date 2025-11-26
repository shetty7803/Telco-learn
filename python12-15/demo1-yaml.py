import yaml

with open("docker.yaml") as f:
    data = yaml.safe_load(f)

seen = set()

for service, config in data.get("services", {}).items():
    has_port = False  

    for item in config.get("environment", []):
        if "_PORT" in item and "=" in item:
            key, value = item.split("=", 1)
            entry = f"{service} {key} = {value}"
            if entry not in seen:
                seen.add(entry)
                print(entry)
                has_port = True



