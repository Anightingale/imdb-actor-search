from bs4 import BeautifulSoup
import requests

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
	
	# download html contents of imdb page
	imdbpage = requests.get("https://www.imdb.com/")

	# starts with 2 if successful
	print("status code: {}".format(imdbpage.status_code))

	# use beautiful soup to parse document
	soup = BeautifulSoup(imdbpage.content, 'html.parser')
	print(soup.prettify())


    actorname = input("Please enter actor\'s name: ")
    print('length of name :: {}'.format(len(actorname)))
    print("actor :: {}".format(actorname))

    # my_function('hello world')
    # my_object = MyClass('Amy')
    # my_object.say_name()

if __name__ == '__main__':
    main()