from bs4 import BeautifulSoup
import requests
url = 'https://en.wikipedia.org/wiki/Joseph_Stalin'
result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")
Paragraph = doc.find('<p>'[3])

print(Paragraph.string)

