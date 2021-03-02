import os
from dotenv import load_dotenv
import requests
import json


load_dotenv('.env')
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

url = "https://api.linkedin.com/v2/organizationAcls?q=organization&organization=urn%3Ali%3Aorganization%3A14547467&role=ADMINISTRATOR&state=APPROVED"

admin_request_url = "https://api.linkedin.com/v2/reactions/(entity:urn%3Ali%3Aactivity%3A6750434325692596224)?q=entity&count=67&projection=(elements)"
headers={
    "Connection": "Keep-Alive",
    "Authorization": "Bearer {}".format(ACCESS_TOKEN),
    "Content-Type":"application/json",
}


headers_admin={
    "Authorization": "Bearer {}".format(ACCESS_TOKEN),
    "X-Restli-Protocol-Version": "2.0.0"
}
re = requests.get(url, headers=headers)
print(re.status_code)
print(re.json())

re = requests.get(admin_request_url, headers=headers_admin)
print(re.status_code)
json_text = json.loads(re.text)
#print(json_text)
elements = json_text["elements"]

for element in elements:
    actor = element["created"]["actor"]
    actor_elements = actor.split(':')
    actor_id = actor_elements[-1]

    url = "https://api.linkedin.com/v2/people/(id:{})".format(actor_id)
    print(url)
    re = requests.get(url, headers=headers_admin)
    print(re.status_code)
    print(re.text)

