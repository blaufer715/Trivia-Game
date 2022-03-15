import requests
from bs4 import BeautifulSoup
from csv import writer, DictWriter, DictReader
import random
import time

base_url = "https://quotes.toscrape.com/"
# url = "page/1/"

# quotes = []
# count = 0
# while url:
# 	response = requests.get(base_url + url)
# 	print(f"now scraping {base_url}{url}")
# 	soup = BeautifulSoup(response.text, "html.parser")
# 	statements = soup.find_all(class_ = "quote")
# 	for statement in statements:
# 		quote_text = statement.find(class_ = "text").get_text()
# 		author = statement.find(class_ = "author").get_text()
# 		href = statement.find("a")["href"]
# 		quote = dict(text = quote_text, author = author, bio_link =  href)
# 		quotes.append(quote)
# 	next_btn = soup.find(class_ = "next")
# 	url = next_btn.find("a")["href"] if next_btn else None
# 	time.sleep(2) #### Creates delay so website isn't scraped to aggresively. If scraping too much data can overload server
# 	#### Also likely to get caught if you are sending too many scraping requests to the same website too quickly

# with open ("quotes.csv", "w") as file:
# 	headers = ("text", "author", "bio_link")
# 	csv_writer = DictWriter(file, headers)
# 	csv_writer.writeheader()
# 	for row in quotes:
# 		csv_writer.writerow(row)

with open ("quotes.csv") as file:
	csv_reader = DictReader(file)
	quotes = list(csv_reader)



# print(quotes)
# print(next_btn)
# print(page_href)

random_quote = random.choice(quotes)
# print(random_quote)


def author_bio(): 
	name_breakdown = random_quote["author"].split(" ")
	author_url = base_url + random_quote["bio_link"]
	response2 = requests.get(author_url)
	soup2 = BeautifulSoup(response2.text, "html.parser")
	global birth_date
	birth_date = soup2.find(class_ = "author-born-date").get_text()
	global birth_place
	birth_place = soup2.find(class_ = "author-born-location").get_text()
	global description
	description = soup2.find(class_ = "author-description").get_text()
	description = description.replace(name_breakdown[0], "")
	description = description.replace(name_breakdown[-1], "this person")
	description = description.split(".")
	global initials
	initials = f"{name_breakdown[0][0].upper()}.{name_breakdown[-1][0].upper()}."





# print(random_quote)

guesses = 4
print (random_quote["text"])
author_bio()

while guesses > 0:
	guess = input("WHO SAID IT?  ").lower()
	if guess == random_quote["author"].lower():
		print ("You Win!")
		play_again = ' '
		while play_again.lower() not in ("yes", "y", "n", "no"):  
			play_again = input("Do you want to play again? (y/n)")
		if play_again in ("y", "yes"):
			random_quote = random.choice(quotes)
			author_bio()
			guesses = 4
			print(random_quote["text"])
		else: 
			print("game over")
			break
	else:
		guesses -= 1
		print (f"Guesses Remaining: {guesses}")
		print("Here's a hint: ")
		if guesses == 3:
			print(f"This person was born in {birth_place}, on {birth_date}") 
		elif guesses == 2:
			random_num = random.randint(3,5)
			print(description[random_num])		
		elif guesses == 1:
			print(f"Initials: {initials}") 
		elif guesses == 0 :
			print("You Lose")
			print("Author: " +  random_quote["author"])
			play_again = ' '
			while play_again.lower() not in ("yes", "y", "n", "no"): 
				play_again = input("Do you want to play again? (y/n)")
			if play_again in ("y", "yes"):
				random_quote = random.choice(quotes)
				author_bio()
				guesses = 4
				print (random_quote["text"])
			else: 
				print("game over")
				break
