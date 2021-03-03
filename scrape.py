from bs4 import BeautifulSoup
import requests
import lxml

url = input("Enter the linkedin post url: ")
r = requests.get(str(url))
src = r.text
print(src)
soup = BeautifulSoup(src, features="lxml")
likes = soup.find_all("span", {"class": "social-counts-reactions__social-counts-numRections"})
likes_details = soup.find_all("div", {"class": "artdeco-modal artdeco-modal--layer-default social-details-reactors-modal"})

print(likes)
print(likes_details)
