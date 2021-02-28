from bs4 import BeautifulSoup
import requests
import lxml

url = input("Enter the linkedin post url: ")
r = requests.get(str(url))
src = r.text
print(src)
soup = BeautifulSoup(src, features="lxml")
likes = soup.find_all("span", {"class": "social-counts-reactions__social-counts-numRections"})

print(likes)
