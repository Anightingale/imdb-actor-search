import sys
from classmodule import MyClass
from funcmodule import my_function

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
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))
    my_function('hello world')
    my_object = MyClass('Amy')
    my_object.say_name()
if __name__ == '__main__':
    main()