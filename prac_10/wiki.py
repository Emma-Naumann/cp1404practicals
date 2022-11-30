"""
Emma Naumann
CP1404 Practical 10
Wikipedia search and summary using user input program
"""

import wikipedia

search_phrase = input("Search phrase: ")
while search_phrase != "":
    try:
        # print(wikipedia.summary(search_phrase))
        page = wikipedia.page(search_phrase, auto_suggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    search_phrase = input("Page title/search phrase: ")
