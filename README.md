### Linkedin analytics - Introduction

This repo is a very minimalistic use of Linkedin market product API to retrieve as well as check whether certain usernames have reacted to your post. Can be used to check if the followers are active. Will be implementing more features or making it a wrapper API library soon.

##### Short note on API access token process.

For this particular use I would recommend going through the [documentation](https://docs.microsoft.com/en-us/linkedin/marketing/getting-started#what-permissions-are-available) very thoroughly to understand the process of permissions.

##### How to run the script?

First a virtualenv can be initialised and then install the necessary packages by:

```
pip install -r requirements.txt
```

After that create a `.env` file as given in the `.env.template` file. Copy your access token there in the given field.

For the post id, go to a post URL and you would find a long string of integers. Copy that into the `bot.py` script in the end.

Last you can fill in the usernames of which you want to check whether they have reacted to the post or not.

After everything is done just run
```
python3 bot.py
```

Note: It may take time to give the final output if the post has a lot of reactions.

