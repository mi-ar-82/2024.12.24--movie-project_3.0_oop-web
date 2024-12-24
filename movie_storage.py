import json

def get_movies():
    """Loads movies from the 'movies.json' file. Returns an empty dictionary if the file doesn't exist or is corrupted."""
    try:
        with open('movies.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error: Corrupted movies.json file.")
        return {}



def save_movies(movies):
    """Saves the movies dictionary to the 'movies.json' file."""
    with open('movies.json', 'w') as f:
        json.dump(movies, f)


def add_movie(title, year, rating):
    """Adds a movie to the movies database.

    Args:
      title: The title of the movie.
      year: The year of release.
      rating: The movie rating.
    """
    movies = get_movies()
    movies[title] = {"year": year, "rating": rating}
    save_movies(movies)


def delete_movie(title):
    """Deletes a movie from the movies database.

    Args:
      title: The title of the movie to delete.
    """
    movies = get_movies()
    if title in movies:
        del movies[title]
        save_movies(movies)


def update_movie(title, rating):
    """Updates the rating of a movie in the movies database.

    Args:
      title: The title of the movie to update.
      rating: The new rating for the movie.
    """
    movies = get_movies()
    if title in movies:
        movies[title]["rating"] = rating
        save_movies(movies)

