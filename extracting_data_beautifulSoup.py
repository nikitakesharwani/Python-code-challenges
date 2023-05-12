import requests
from bs4 import BeautifulSoup

url = "https://techcrunch.com/"

response =requests.get(url)

print(response)

htmlContent = response.content

# print(htmlContent)

soup = BeautifulSoup(htmlContent , "html.parser")

# print(soup.prettyfy)

print(soup.findAll('div'))



