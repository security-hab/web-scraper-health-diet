import csv
import json

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "YOUR USER AGENT"
}

url = (
    "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
)
req = requests.get(url, headers=headers)
src = req.text

with open("index.html", "w", encoding="utf-8") as file:
    file.write(src)

with open("index.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
product = soup.find_all(class_="mzr-tc-group-item-href")
productDictionary = {}

for i in product:
    productName = i.text
    productLink = "https://health-diet.ru" + i.get("href")

    productDictionary[productName] = productLink

with open("result.json", "w", encoding="utf-8") as file:
    json.dump(productDictionary, file, indent=4, ensure_ascii=False)

with open("result.json", encoding="utf-8") as file:
    allCategories = json.load(file)

count = 0

for productName, prooductLink in allCategories.items():
    rep = [",", "-", " "]
    for i in rep:
        if i in productName:
            productName = productName.replace(i, "_")

    req = requests.get(url=prooductLink, headers=headers)
    src = req.text

    with open(f"{productName}.html", "w", encoding="utf-8") as file:
        file.write(src)

    with open(f"{productName}.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    result = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")

    product = result[0].text
    calories = result[1].text
    proteins = result[2].text
    fats = result[3].text
    carbohydrates = result[4].text

    with open(f"{productName}.csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow([product, calories, proteins, fats, carbohydrates])

    productData = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")

    for i in productData:
        product_td = i.find_all("td")

        title = product_td[0].find("a").text
        calories = product_td[1].text
        protein = product_td[2].text
        fats = product_td[3].text
        carbohydrates = product_td[4].text

        with open(f"{productName}.csv", "a", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow([title, calories, protein, fats, carbohydrates])

        count += 1
