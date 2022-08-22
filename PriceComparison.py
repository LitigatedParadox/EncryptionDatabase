SiteDatabase = open("PriceComparisonDatabase.txt", "a")
from bs4 import BeautifulSoup
import requests

InitialCommand = input("Enter command or URL you would like to compare with: ")
if InitialCommand == 'help':
    print("This tool will compare prices from multiple listings of the same item on different sites." + "\n"
        "To add a site to the database, use the 'addsite' command, followed by the URL")
elif InitialCommand.startswith("https://"):
    URL = str(InitialCommand)
    result = requests.get(URL)
    doc = BeautifulSoup(result.text, "html.parser")
    Price = doc.find('<strong')
    if str(Price) == "None":
        ItemPropPrice = doc.find('class=')
        print(ItemPropPrice)
    else:
        print(str(Price))