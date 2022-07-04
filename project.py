import requests
import json

from pprint import pprint

book_search = input("What genre are you looking for? ")


def execute(book_search, printme=False):
    app_key = '0gMd3PpIeyyeh9bOrp2uV4iMjftYHjZp'
    url = 'https://api.nytimes.com/svc/books/v3/lists/current/{}.json?api-key={}'.format(book_search, app_key)

    response = requests.get(url)
    print(response)

    bestsellers = response.json()

    if printme:
        pprint(bestsellers)

    return bestsellers


bookResults = execute(book_search)

availableBooks = [x['title'] for x in bookResults['results']['books']]

print("The available books are : ")
print(availableBooks)

availableAuthors = [x['author'] for x in bookResults['results']['books']]

print("The authors are : ")
print(availableAuthors)

availableLinks = [x['buy_links'] for x in bookResults['results']['books']]

print("The links to buy are : ")
print(availableLinks)

availablePrice = [x['price'] for x in bookResults['results']['books']]

print("The price of the book is : ")
print(availablePrice)

fileTowrite = json.dumps(availableBooks)

bf = open('bookfile.txt', 'w')

bookFile = bf.write(fileTowrite)

bf.close()
