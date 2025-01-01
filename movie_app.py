class MovieApp:
    #A class to manage the movie application, including user commands and menu handling.

    def __init__(self, storage):
        """
        Initialize the MovieApp with a storage instance.

        Args:
            storage (IStorage): An instance of a class implementing IStorage.
        """
        self._storage = storage

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
        Add a new movie to the storage.
        """
        try:
            title = input("Enter movie title: ").strip()
            year = int(input("Enter release year: "))
            rating = float(input("Enter rating (0-10): "))
            poster = input("Enter poster URL: ").strip()
            self._storage.add_movie(title, year, rating, poster)
            print(f"Movie '{title}' added successfully.")
        except ValueError as e:
            print(f"Error: {e}")

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
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
