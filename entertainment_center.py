import model
import fresh_tomatoes
import media

def launch():
	# Created an instance of Model in order to have the data available
	movies = model.Model()
	movies_arr = []
	# Created a loop in order to dynamically parse the json object and create
	# Movie objects based on the json object properties
	for movie in movies.data["movies"]:
		movie_obj=media.Movie(movie["title"],movie["storyline"],movie["poster"],
			movie["trailer"])
		movies_arr.append(movie_obj)
	# Calling the open_movies_page as a way to generate the index.html and 
	# launch the browser
	fresh_tomatoes.open_movies_page(movies_arr)

launch()
