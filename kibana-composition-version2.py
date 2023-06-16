import requests, json
from requests.auth import HTTPBasicAuth

# establish session and create Kibana Space
session = requests.Session()
session.auth = HTTPBasicAuth("your-username", "your-password")

kibana_url = "https://observability-34c3a7.kb.westeurope.azure.elastic-cloud.com:9243"
headers = {
    "kbn-xsrf": "true",
    "Content-Type": "application/json"
}
space = {
    "id": "azure",
    "name": "Azure Space",
    "description": "Azure Resources Kibana Space",
    "initials": "AR"
}
r = session.post(f"{kibana_url}/api/spaces/space", headers=headers, json=space)
r.raise_for_status()
print(json.dumps(r.json(), indent=2))

# specify Kibana Space to perform the following operations
space_id = "azure"

# search for specified Kibana Space
r = session.get(f"{kibana_url}/api/spaces/space/{space_id}", headers=headers)
print(json.dumps(r.json(), indent=2))

# delete specified Kibana Space
r = session.delete(f"{kibana_url}/api/spaces/space/{space_id}", headers=headers)

# define properties for data view
data_view = {
    "data_view": {
        "id": "data-view-1",
        "version": "",
        "title": "database*",
        "name": "Database logs data view",
        "namespaces": ["azure"],
        "fields": {}
    }
}

# create data view in azure Kibana Space
r = session.post(f"{kibana_url}/api/data_views/data_view", headers=headers, json=data_view)
print(json.dumps(r.json(), indent=2))

# specify data view and retrieve information about it
dataview_id = "data-view-1"
r = session.get(f"{kibana_url}/s/{space_id}/api/data_views/data_view/{dataview_id}", headers=headers)
print(json.dumps(r.json(), indent=2))

# delete specified data view
r = session.delete(f"{kibana_url}/s/{space_id}/api/data_views/data_view/{dataview_id}", headers=headers)
print(json.dumps(r.json(), indent=2))
