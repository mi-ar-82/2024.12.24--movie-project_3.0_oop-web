import json
from storage.istorage import IStorage

class StorageJson(IStorage):
    #This class will manage movies stored in a JSON file.
    #Implementation of IStorage for JSON files.
    

    def __init__(self, file_path):
        #Initializes the JSON storage with the given file path.
        self.file_path = file_path

    def _load_movies(self):
        #Loads movies from the JSON file. Returns an empty dictionary if the file doesn't exist or is corrupted.
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_movies(self, movies):
        #Saves movies to the JSON file.
        with open(self.file_path, 'w') as f:
            json.dump(movies, f)

    def list_movies(self):
        #Returns all movies in the storage as a dictionary.
        #overrides method in iStorage !!!
        return self._load_movies()

    def add_movie(self, title, year, rating, poster):
        #Adds a new movie to the storage.
        # overrides method in iStorage !!!
        movies = self._load_movies()
        movies[title] = {"year": year, "rating": rating, "poster": poster}
        self._save_movies(movies)

    def delete_movie(self, title):
        #Deletes a movie from the storage.
        #overrides method in iStorage !!!
        movies = self._load_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)
    
    def update_movie(self, title, rating):
        """Updates the rating of an existing movie in the storage."""
        movies = self._load_movies()
        if title in movies:
            movies[title]["rating"] = rating
            self._save_movies(movies)
        else:
            raise ValueError(f"Movie '{title}' does not exist.")

