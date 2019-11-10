# IMPORTS
from bs4 import BeautifulSoup
import requests
import urllib.parse

# GLOBAL VARIABLES


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
	
	# make sure actor name exists
	actor = 0
	while isinstance(actor, int):
		inputname = input("Please enter actor\'s name: ")
		actor = getactorinfo(inputname)

	print("\nDisplaying movies from{}".format(actor.get_text()))

	getactormovies(actor)

def getactormovies(actor): 

	profilepage = requests.get("https://www.imdb.com" + actor.find('a')['href'])

	print("https://www.imdb.com" + actor.find('a')['href'])

	# use beautiful soup to parse document
	soup = BeautifulSoup(profilepage.content, 'html.parser')

	# find each actor and their unique description
	#movielist = soup.find_all(class_="filmo-category-section")
	movielist = soup.select('b a')

	for movie in movielist:
		print(movie.get_text())

	#profile: https://www.imdb.com/name/nm0413168/?ref_=fn_nm_nm_1




def getactorinfo(inputname): 
	
	# get html contents of page when actors of exact name `actorname` is searched on imdb
	inputname = urllib.parse.quote(inputname)
	imdbpage = requests.get("https://www.imdb.com/find?q=" + inputname + "&s=nm&exact=true")

	# use beautiful soup to parse document
	soup = BeautifulSoup(imdbpage.content, 'html.parser')

	# find each actor and their unique description
	actorinfo = soup.find_all(class_='result_text')
	
	if len(actorinfo) == 0: 
		print("No actors named " + inputname)
		return 0
	if len(actorinfo) == 1:
		# there is only 1 actor in search result
		return actorinfo[0]
	else: 
		# multiple actors in search result
		# allow user to select an actor based on avalailable information
		print("\nWhich actor did you mean? Please insert number\n")
		currdisplayed = 0
		num = ''
		numtodisplay = 5
		
		# display only 5 actors at a time, allow user to scroll
		while currdisplayed < len(actorinfo) and not num: 
			
			for i in range(numtodisplay):
				print("{}. {}".format(currdisplayed+i+1, actorinfo[currdisplayed+i].get_text()))
			currdisplayed+=numtodisplay
			
			#check if user has scrolled through entire list
			if currdisplayed > len(actorinfo)-numtodisplay:
				numtodisplay= len(actorinfo)%numtodisplay
			
			if currdisplayed < len(actorinfo):
				# TODO: REMOVE THIS LINE WHEN LOOPED AGAIN
				print("press `enter` to see more...")

			num = input()
		
		#make sure input is an integer
		while not num:
			print("Please insert integer")
			num = input()
			

		return actorinfo[int(num)-1]		

