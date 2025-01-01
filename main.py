from movie_app import MovieApp
from storage.storage_json import StorageJson


def main():
    #Main function to initialize and run the MovieApp.

    # Initialize JSON storage
    storage = StorageJson('data/movies.json')

    # Initialize and run the MovieApp
    app = MovieApp(storage)
    app.run()

if __name__ == "__main__":
    main()
