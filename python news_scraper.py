import requests
from bs4 import BeautifulSoup
url = 'https://www.npr.org/'
print(f"Fetching headlines from {url}...")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print("Parsing HTML...")
headlines = soup.find_all('h3', class_='title')
print(f"Found {len(headlines)} headline tags.")
if headlines:
    with open('npr_headlines.txt', 'w', encoding='utf-8') as file:
        for i, headline in enumerate(headlines, 1):
            text = headline.get_text(strip=True)
            if text:
                print(f"{i}. {text}")
                file.write(f"{i}. {text}\n")
    print("\n✅ Headlines saved to 'npr_headlines.txt'")
else:
    print("⚠ No headlines found.")