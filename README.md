📰 NPR News Headlines Scraper
This project is a Python script that scrapes the top news headlines from the NPR homepage using requests and BeautifulSoup, then saves them to a .txt file.

📌 Features
Fetches the latest top headlines from NPR
Parses HTML content using BeautifulSoup
Saves headlines to a text file (npr_headlines.txt)
Includes a script to read and print the saved headlines

📁 Project Structure
npr_scraper/
│
├── scraper.py         
├── read_headlines.py    
├── npr_headlines.txt    
└── README.md            
🛠️ Requirements
Python 3.x

requests

beautifulsoup4

Install dependencies:

bash
Copy
Edit
pip install requests beautifulsoup4

EXAMPLE OUTPUT:
1. This Tuscan startup sold all its olive oil in the U.S. Then came Trump's tariffs
2. As Trump's tariffs take shape, is America really winning?
3. Here's a list of where Trump's tariff threats — and trade deals — stand
4. State Department may require some visa applicants to post bond of up to $15,000
5. Texas Democrats walked out to block the GOP. How well has the tactic worked before?
6. He said, she said, it said: I used ChatGPT as a couple's counselor. How did we fare?
7. To avoid fakes when shopping online, watch out for these 4 red flags
8. New books this week: unconventional novels and an oral history of Hiroshima, Nagasaki
9. Hurricane Katrina was a catalyst for change in New Orleans' public defender office
10. Tennessee readies for execution of man with working implanted defibrillator
11. Dali owners suing ship manufacturer for Baltimore's Key Bridge crash
12. Watch NPR's news roundup: Texas legislators, Israel weighs expanding war in Gaza
13. Yosemite employees worked for weeks with no pay before the government hired them
14. What's the secret to India's moves to conquer the global chess scene?
15. River Tiber: Tiny Desk Concert
16. Federal judge halts Arkansas Ten Commandments law
17. What can Texas Republicans actually do about Democrats' effort to block redistricting?
18. Texas Democrats block GOP redistricting plan by fleeing the state
19. Wildfire smoke is like smoking 'half a pack a day.' Here's how to protect yourself
20. Brazil's Supreme Court orders house arrest for former President Bolsonaro

