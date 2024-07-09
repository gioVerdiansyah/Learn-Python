import requests
import json

webhook_url = "http://127.0.0.1:4545/hook_me"

data = {
    "name": "Verdiansyah",
    "division": "BackEnd Developer"
}

r = requests.post(webhook_url, json.dumps(data), headers={"Content-Type": "application/json"})
print(r.content)