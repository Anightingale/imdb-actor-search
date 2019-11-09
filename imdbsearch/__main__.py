from bs4 import BeautifulSoup
import requests
import urllib.parse

# from .classmodule import MyClass
# from .funcmodule import my_function

"""
Command-line interface Tool:
	1. Queries IMDB
	2. User enters movie star's name
		a. If more than one actor has that name:
			i. Return a menu for allowing selection of an individual based on available information
	3. Prints the list of movies that the star has appeared in to screen
		a. Default - Sorted in date order (oldest first)
		b. Allow for reversal of order (newest first)
	4. Allow option for sending result to a well-structured JSON document
	5. Publish your new Python package to PyPi.org automatically from Github when a new tag is pushed 
		a. Use a free CI/CD tool such as Travis/CircleCI"
"""
def main():
	
	actorname = input("Please enter actor\'s name: ")
	# format for web address

	print("actor :: {}".format(actorname))

	# >>> import urllib.parse
	# >>> query = 'Hellö Wörld@Python'
	# >>> urllib.parse.quote(query)
	# 'Hell%C3%B6%20W%C3%B6rld%40Python'

	# download html contents of imdb page

	# link format for searching for actors of exact input name
	# https://www.imdb.com/find?q=hugh%20jackman&s=nm&exact=true
	# replace `space` with `%20`

	actorname = urllib.parse.quote(actorname)

	imdbpage = requests.get("https://www.imdb.com/find?q=" + actorname + "&s=nm&exact=true")

	# starts with 2 if successful
	print("status code: {}".format(imdbpage.status_code))
	print("https://www.imdb.com/find?q=" + actorname + "&s=nm&exact=true")

	# use beautiful soup to parse document
	soup = BeautifulSoup(imdbpage.content, 'html.parser')
	print(soup.find("tr a"))


	# each actor under that name is under that class 'findResult' which is elements of class 'findList'


    # my_function('hello world')
    # my_object = MyClass('Amy')
    # my_object.say_name()

if __name__ == '__main__':
    main()