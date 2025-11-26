"""
import yaml

with open("docker.yaml") as f:
    data = yaml.safe_load(f)

env_list = data['services']['oai-amf']['environment']

for item in env_list:
    if "MCC=" in item:
        print(item)        
        #print("MCC: ", item.split("=")[1])   # prints only value: 001
        """
"""
import yaml

with open("docker.yaml") as f:
    data = yaml.safe_load(f)

services = data.get("services", {})

for name, info in services.items():
    print(f"\nService: {name}")

    # ---- Print IPv4 Address ----
    ipv4 = (
        info
        .get("networks", {})
        .get("public_net", {})
        .get("ipv4_address")
    )
    print(f"  IPv4 Address: {ipv4}")

    # ---- Print Dependencies ----
    deps = info.get("depends_on", [])
    if deps:
        print(f"  Depends On: {', '.join(deps)}")
    else:
        print("  Depends On: None")
"""
import yaml

with open("docker.yaml") as f:
    data = yaml.safe_load(f)

for service, details in data.get("services", {}).items():
    print(f"\nService: {service}")

    # Get IPv4 Address (safely)
    ipv4 = details.get("networks", {}).get("public_net", {}).get("ipv4_address", "No IP")
    print(f"  IPv4 Address: {ipv4}")

    # Get depends_on
    depends = details.get("depends_on")
    if isinstance(depends, list):
        depends = ", ".join(depends)
    else:
        depends = "None"

    print(f"  Depends On: {depends}")
