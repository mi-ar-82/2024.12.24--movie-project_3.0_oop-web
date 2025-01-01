import csv
from istorage import IStorage


class StorageCsv(IStorage):
    """
    A class to handle movie storage using CSV files.
    Implements the IStorage interface.
    """

    def __init__(self, file_path):
        """
        Initialize the StorageCsv with a file path.

        Args:
            file_path (str): Path to the CSV file.
        """
        self.file_path = file_path

    def _load_movies(self):
        """
        Loads movies from the CSV file and returns them as a dictionary.
        If the file doesn't exist or is empty, returns an empty dictionary.
        """
        movies = {}
        try:
            with open(self.file_path, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    title = row['title']
                    movies[title] = {
                        'rating': float(row['rating']),
                        'year': int(row['year']),
                    }
        except FileNotFoundError:
            # If the file doesn't exist, return an empty dictionary
            pass
        return movies

    def _save_movies(self, movies):
        """
        Saves the movies dictionary to the CSV file.

        Args:
            movies (dict): A dictionary of movies to save.
        """
        with open(self.file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'rating', 'year']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for title, data in movies.items():
                writer.writerow({
                    'title': title,
                    'rating': data['rating'],
                    'year': data['year'],
                })

    def list_movies(self):
        """
        Returns all movies in storage as a dictionary.

        Returns:
            dict: A dictionary of dictionaries containing movie information.
        """
        return self._load_movies()

    def add_movie(self, title, year, rating, poster=None):
        """
        Adds a new movie to the storage.

        Args:
            title (str): The title of the movie.
            year (int): The release year of the movie.
            rating (float): The rating of the movie.
            poster (str): The poster URL (ignored for CSV storage).
        """
        movies = self._load_movies()
        movies[title] = {
            'year': year,
            'rating': rating,
        }
        self._save_movies(movies)

    def delete_movie(self, title):
        """
        Deletes a movie from storage.

        Args:
            title (str): The title of the movie to delete.
        """
        movies = self._load_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)

    def update_movie(self, title, rating):
        """
        Updates the rating of an existing movie in storage.

        Args:
            title (str): The title of the movie to update.
            rating (float): The new rating for the movie.
        """
        movies = self._load_movies()
        if title in movies:
            movies[title]['rating'] = rating
            self._save_movies(movies)
