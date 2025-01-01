import os
import omdb
from omdb_api_key import OMDB_API_KEY  # Import the API key from local file


class MovieApp:
    #A class to manage the movie application, including user commands and menu handling.

    def __init__(self, storage):
        """
        Initialize the MovieApp with a storage instance.

        Args:
            storage (IStorage): An instance of a class implementing IStorage.
        """
        self._storage = storage
        omdb.set_default('apikey', OMDB_API_KEY)  # Use the imported API key

    def _command_list_movies(self):
        """
        List all movies in the storage.
        """
        movies = self._storage.list_movies()
        if not movies:
            print("No movies found.")
        else:
            for title, data in movies.items():
                print(f"{title} ({data['year']}): {data['rating']}/10")
    
    def _command_add_movie(self):
        """
        Add a new movie by fetching details from the OMDb API.
        """
        try:
            title = input("Enter movie title: ").strip()
            if not title:
                raise ValueError("Title cannot be empty.")
            
            # Fetch movie details from OMDb API
            movie_data = omdb.get(title = title)
            
            if not movie_data or 'title' not in movie_data:
                print(f"Error: Movie '{title}' not found in OMDb database.")
                return
            
            # Extract required fields
            movie_title = movie_data.get('title')
            year = int(movie_data.get('year', 0))
            rating = float(movie_data.get('imdb_rating', 0)) if movie_data.get('imdb_rating') != 'N/A' else 0.0
            poster = movie_data.get('poster', 'N/A')
            
            # Save to storage
            self._storage.add_movie(movie_title, year, rating, poster)
            print(f"Movie '{movie_title}' added successfully!")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def _command_delete_movie(self):
        """
        Delete a movie from the storage.
        """
        title = input("Enter the title of the movie to delete: ").strip()
        self._storage.delete_movie(title)
        print(f"Movie '{title}' deleted (if it existed).")

    def _command_update_movie(self):
        """
        Update a movie's rating in the storage.
        """
        try:
            title = input("Enter the title of the movie to update: ").strip()
            rating = float(input("Enter new rating (0-10): "))
            self._storage.update_movie(title, rating)
            print(f"Movie '{title}' updated successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def _command_statistics(self):
        """
        Display statistics about the movies in storage.
        """
        movies = self._storage.list_movies()
        if not movies:
            print("No movies found.")
            return

        ratings = [data['rating'] for data in movies.values()]
        average_rating = sum(ratings) / len(ratings)
        highest_rated_movie = max(movies.items(), key=lambda x: x[1]['rating'])
        lowest_rated_movie = min(movies.items(), key=lambda x: x[1]['rating'])

        print("\nMovie Statistics:")
        print(f"Total Movies: {len(movies)}")
        print(f"Average Rating: {average_rating:.2f}")
        print(f"Highest Rated Movie: {highest_rated_movie[0]} ({highest_rated_movie[1]['rating']}/10)")
        print(f"Lowest Rated Movie: {lowest_rated_movie[0]} ({lowest_rated_movie[1]['rating']}/10)")
    
    def run(self):
        """
        Run the main loop of the movie application.
        """
        while True:
            print("\nMenu:")
            print("1. List movies")
            print("2. Add movie")
            print("3. Delete movie")
            print("4. Update movie")
            print("5. Show statistics")
            print("6. Generate website")
            print("0. Exit")
            
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                self._command_list_movies()
            elif choice == "2":
                self._command_add_movie()
            elif choice == "3":
                self._command_delete_movie()
            elif choice == "4":
                self._command_update_movie()
            elif choice == "5":
                self._command_statistics()
            elif choice == "6":
                self._generate_website()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def _generate_website(self):
        """
        Generate a website displaying all movies in the collection.
        """
        # Load movies from storage
        movies = self._storage.list_movies()
        
        if not movies:
            print("No movies found to generate the website.")
            return
        
        # Load the HTML template
        try:
            with open("_static/index_template.html", "r") as template_file:
                template = template_file.read()
        except FileNotFoundError:
            print("Error: Template file not found.")
            return
        
        # Generate HTML for each movie
        movie_grid_html = ""
        for title, details in movies.items():
            movie_html = f"""
            <li>
                <div class="movie">
                    <img class="movie-poster" src="{details.get('poster', 'https://via.placeholder.com/128x193')}" alt="{title} poster">
                    <div class="movie-title">{title}</div>
                    <div class="movie-year">{details.get('year', 'N/A')}</div>
                    <div class="movie-rating">Rating: {details.get('rating', 'N/A')}/10</div>
                </div>
            </li>
            """
            movie_grid_html += movie_html
        
        # Replace placeholders in the template
        output_html = template.replace("__TEMPLATE_TITLE__", "My Movie Collection")
        output_html = output_html.replace("__TEMPLATE_MOVIE_GRID__", movie_grid_html)
        
        # Save the final HTML to a new file
        output_path = "index.html"
        with open(output_path, "w") as output_file:
            output_file.write(output_html)
        
        print(f"Website generated successfully! Open '{output_path}' in your browser.")
        
    
