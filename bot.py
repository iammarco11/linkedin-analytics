import os
from dotenv import load_dotenv
import requests


load_dotenv('.env')
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
print(CLIENT_ID)
print(CLIENT_SECRET)
print(ACCESS_TOKEN)
url = "https://api.linkedin.com/v2/organizationAcls?q=organization&organization=urn%3Ali%3Aorganization%3A14547467&role=ADMINISTRATOR&state=APPROVED"

admin_request_url = "https://api.linkedin.com/v2/reactions/(entity:urn%3Ali%3Aactivity%3A6750434325692596224)?q=entity"
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
print(re.json())
