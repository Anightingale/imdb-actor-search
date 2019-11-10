from bs4 import BeautifulSoup
import requests
import urllib.parse

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
	
	inputname = input("Please enter actor\'s name: ")

	actor = getactorinfo(inputname)

	print("\nDisplaying movies from{}".format(actor.get_text()))



def getactorinfo(inputname): 
	
	# get html contents of page when actors of exact name `actorname` is searched on imdb
	inputname= urllib.parse.quote(inputname)
	imdbpage = requests.get("https://www.imdb.com/find?q=" + inputname + "&s=nm&exact=true")

	# starts with 2 if successful, 4 or 5 if not
	print("status code: {}".format(imdbpage.status_code))

	# use beautiful soup to parse document
	soup = BeautifulSoup(imdbpage.content, 'html.parser')

	# find each actor and their unique description
	actorinfo = soup.find_all(class_='result_text')
	
	if(len(actorinfo) > 1):
		# allow user to select an actor based on avalailable information
		for i in range(len(actorinfo)):
			
			print("{}. {}".format(i+1, actorinfo[i].get_text()))

		num = int(input("\nWhich actor did you mean? Please insert number: "))
		
		return actorinfo[num-1]

	else: 
		# there is only 1 actor in search result
		return actorinfo[0]

