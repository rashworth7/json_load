from urllib.request import urlopen
import json
import requests

# == INSTRUCTIONS ==
#
# Below, you'll find lots of incomplete functions.
#
# Your job: Implement each function so that it does its job effectively.
#
# * Use the material, Python Docs and Google as much as you want

# == EXERCISES ==

# Purpose: Use Python libraries to request the provided URL, convert the
#          response data to JSON, and return the data.
# Example:
#   Call:    load_data_from_url("https://example.org/my.json")
#   Returns: A JSON object
def load_data_from_url(example_url):
    # url = urlopen(example_url)
    # response = url.read().decode('UTF-8')
    # json_data = json.loads(response)
    # return json_data

#Using requests module - this seems easier?
    response = requests.get(example_url)
    return response.json()

# Purpose: Use Python libraries to open the specified file, convert the
#          data to JSON, and return the data.
# Example:
#   Call:    load_data_from_file("my_test_data.json")
#   Returns: A JSON object

# open the json file first, then load the file and return the output
def load_data_from_file(filename):
    with open(filename) as file:
        output = json.load(file)
        return output

# Purpose: Load the sample JSON from file, and returns a list of films 
#           directed by the named person.
# Example:
#   Call:    get_films_by_director("my_test_data.json", "Olivia Wilde")
#   Returns: ["Booksmart, "Don't Worry Darling"]
def get_films_by_director(filename, director):
    with open(filename) as file:
        data = json.load(file)

 # Using a for loop   
    # data = load_data_from_file(filename)
    # print(data)
    # films = []
    # for film in data:
    #     if film["director"] == director:
    #         films.append(film["name"])

    # return films

 # Using a fitler method
    # data = load_data_from_file(filename)
    # films  = list(filter(lambda film: film['director'] == director, data))
    # film_names = [film['name'] for film in films]
    # return film_names 

# Using a list comprehension method
    # data = load_data_from_file(filename)
    films = [film['name'] for film in data if film['director'] == director]
    return films

#get_films_by_director("../test.json", "Frank Darabont")

# Purpose: Load the sample JSON from file, and returns a list of films 
#           starring the named person.
# Example:
#   Call:    get_films_by_actor("my_test_data.json", "Dwayne Johnson")
#   Returns: ["Jumanji", "Jungle Cruise"]
def get_films_by_actor(filename, desired_actor):

    with open(filename) as file:
        data = json.load(file)

 # Using a for loop   
    # data = load_data_from_file(filename)
    # films = []
    # for film in data:
    #     if desired_actor in film['stars']:
    #         films.append(film['name'])
    # return films

# Using a filter method
    # data = load_data_from_file(filename)
    # films = list(filter(lambda film: desired_actor in film['stars'], data))
    # film_list = [film['name'] for film in films]
    # return film_list

#  Using list comprehensionm
    # data = load_data_from_file(filename)
    return [film['name'] for film in data if desired_actor in film['stars']]

# Purpose: Load the sample JSON from file, and returns a list of films 
#           with a rating which is AT LEAST the value specified.
# Example:
#   Call:    get_films_with_minimum_rating("test.json", 9.3)
#   Returns: ["The Shawshank Redemption"]
def get_films_with_minimum_rating(filename, rating):
    with open(filename) as file:
         data = json.load(file)

# Using a for loop
    # data = load_data_from_file(filename)
    # films = []
    # for film in data:
    #     if film['imdb_rating'] >= rating:
    #         films.append(film['name'])
    # return films

# Using filter

    # films = list(filter(lambda film: film['imdb_rating'] >= rating, data))
    # film_list = [film['name'] for film in films]
    # return film_list

# Using list comprehension

    return [film['name'] for film in data if film['imdb_rating'] >= rating]

# Purpose: Load the sample JSON from file, and returns a list of films 
#           which were released during the specified years.
# Example:
#   Call:    get_films_within_year_range("my_test_data.json", 1994, 1996)
#   Returns: ["The Lion King", "Independence Day"]
def get_films_within_year_range(filename, start_year, end_year):
    with open(filename) as file:
        data = json.load(file)
    
# Using a for loop
    # data = load_data_from_file(filename)
    # films = []
    # for film in data:
    #     if film['year'] >= start_year and film['year'] <= end_year:
    #         films.append(film['name'])
    # return films

#Using a filter

    # films = list(filter(lambda film: film['year'] >= start_year and film['year'] <= end_year, data))
    # return [film['name'] for film in films]

#Using list comprehension
    return [film['name'] for film in data if start_year <= film['year'] <= end_year]

# Purpose: Load the sample JSON from file, and returns a list of films 
#           in order of the year that they were released.
# Example:
#   Call:    order_films_chronologically("test.json")
#   Returns: ["12 Angry Men", "The Godfather", "The Godfather: Part II", ... ]
def order_films_chronologically(filename):
    with open(filename) as file:
        data = json.load(file)

    sorted_dict = sorted(data, key = lambda film: film['year'])
    return [film['name'] for film in sorted_dict]


# Purpose: Load the sample JSON from file, and returns a list of films 
#           starting with the most recent.
# Example:
#   Call:    order_films_most_recent_first("test.json")
#   Returns: ["The Dark Knight", "The Shawshank Redemption", "The Godfather: Part II", ... ]
def order_films_most_recent_first(filename):
    with open(filename) as file:
        data = json.load(file)

    sorted_dict = sorted(data, key=lambda film: film['year'], reverse=True)
    return [film['name'] for film in sorted_dict]

# Purpose: Load the sample JSON from file, and returns a deduplicated list 
#           of all the actors whose name begins with that letter,
#           in alphabetical order.
# Example:
#   Call:    all_actors_starting_with_letter("test.json", "a")
#   Returns: ["Aaron Eckhart, "Al Pacino"]
def all_actors_starting_with_letter(filename, letter):
    with open(filename) as file:
        data = json.load(file)

# Loop through the list of dictionaries and then the list of actors in each film to append to the list.
# Could be done as a list comprehension but this seems a little complicated.... Example below
    actors = []
    for film in data:
        for actor in film['stars']:
            if actor not in actors and actor[0].lower() == letter:
                actors.append(actor)
    actors.sort()
    return actors

    # actors_set  = {actor for film in data for actor in film['stars'] if actor[0].lower() == letter}
    # actors_list = list(actors_set)
    # return sorted(actors_list)