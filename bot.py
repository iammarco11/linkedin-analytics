import os
from dotenv import load_dotenv
import requests
import json


class Linkedin(object):
    def __init__(self, post_id, username_list, access_token):
        self.access_token = access_token
        self.baseurl = "https://api.linkedin.com/v2"
        self.post_id = post_id
        self.username_list = username_list
        self.reacted = []
        self.not_reacted = []

        self.headers = {
            "Authorization": "Bearer {}".format(self.access_token),
            "X-Restli-Protocol-Version": "2.0.0"
        }

    def __get_reactions_post(self):
        url = "/reactions/(entity:urn%3Ali%3Aactivity%3A{})?q=entity&count=1000&projection=(elements)".format(self.post_id)
        response = requests.get(self.baseurl+url, headers=self.headers)
        json_text = json.loads(response.text)
        elements = json_text["elements"]

        for element in elements:
            actor = element["created"]["actor"]
            actor_elements = actor.split(':')
            actor_id = actor_elements[-1]

            url = "/people/(id:{})".format(actor_id)
            response = requests.get(self.baseurl+url, headers=self.headers)
            json_text = json.loads(response.text)
            if json_text["id"] != "private":
                self.reacted.append(json_text["vanityName"])

    def check_not_reacted(self):
        self.__get_reactions_post()

        for username in username_list:
            if username not in self.reacted:
                self.not_reacted.append(username)

        return self.not_reacted
 
load_dotenv('.env')
access_token = os.getenv("ACCESS_TOKEN")
post_id = "" #postid is the longest digit sequence of the linkedin post found along the URL
username_list = [] #enter the usernames as strings to check if that user has liked the post

checker = Linkedin(post_id, username_list, access_token)
print(checker.check_not_reacted())
