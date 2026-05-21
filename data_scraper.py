import requests
from bs4 import BeautifulSoup
import csv

# Website URL
url = "https://quotes.toscrape.com/"

# Get webpage
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find quotes
quotes = soup.find_all("div", class_="quote")

# Create CSV file
with open("scraped_quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Column names
    writer.writerow(["Quote", "Author"])

    # Extract data
    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text

        writer.writerow([text, author])

print("Scraping completed successfully!")
print("CSV file created!")