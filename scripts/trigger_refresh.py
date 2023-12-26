import json
import requests

# Fetch service instances from Eureka server
eureka_url = "http://localhost:6087/notification/eureka/apps"
response = requests.get(eureka_url, headers={"Accept": "application/json"})
service_instances = response.json()["applications"]["application"]

# Check if there are service instances
if service_instances:
    # Iterate over service instances and trigger /refresh endpoint
    for application in service_instances:
        for instance in application["instance"]:
            homepage_url = instance["homepageUrl"]
            refresh_url = f"{homepage_url}/actuator/refresh"
            
            # Trigger /refresh endpoint
            requests.post(refresh_url)
            
            print(f"Refresh triggered for {homepage_url}")
else:
    print("No changes in the configuration repository.")
