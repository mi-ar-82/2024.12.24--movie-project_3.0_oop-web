import random
import movie_storage

def menu():
    menu = """Menu:
    0. Exit
    1. List movies
    2. Add movie
    3. Delete movie
    4. Update movie
    5. Stats
    6. Random movie
    7. Search movie
    8. Movies sorted by rating"""
    print(menu)
    return input("Enter choice (0-8):")

# 5.1 average
def get_average_rating(movies):
    if not movies:  # Check if the dictionary is empty
        return 0
    total_rating = sum(movie['rating'] for movie in movies.values())
    number_of_movies = len(movies)
    return round(total_rating / number_of_movies, 2)

# 5.2 display stats
def display_movie_stats(movies):
    average_rating = get_average_rating(movies)
    print(f"\nMovie Collection Statistics:")
    print(f"Number of movies: {len(movies)}")
    print(f"Average rating: {average_rating}")
    if movies:
        highest_rated = max(movies, key = movies[x]['rating'])
        lowest_rated = min(movies, key = movies[x]['rating'])
        print(f"Highest rated movie: {highest_rated} ({movies[highest_rated]['rating']})")
        print(f"Lowest rated movie: {lowest_rated} ({movies[lowest_rated]['rating']})")
    else:
        print("No movies in the collection.")

# 6.1
def get_random_movie(movies):
    return random.choice(list(movies.items()))

# 6.2
def display_random_movie(movies):
    title, movie_info = get_random_movie(movies)
    print(f"\nRandom Movie Pick:")
    print(f"Title: {title}")
    print(f"Rating: {movie_info['rating']}")
    print(f"Year: {movie_info['year']}")

# 7.1
def search_movies(movies, search_term):
    search_term = search_term.lower()
    matching_movies = {}
    for title, info in movies.items():
        if search_term in title.lower():
            matching_movies[title] = info
    return matching_movies

# 7.2
def display_search_results(movies):
    search_term = input("Enter a part of a movie name: ")
    results = search_movies(movies, search_term)
    if results:
        print(f"\nMovies matching '{search_term}':")
        for title, info in results.items():
            print(f"{title}: Rating - {info['rating']}, Year - {info['year']}")
    else:
        print(f"No movies found for: '{search_term}'.")

def display_movie(title, data):
    #Displays the movie information
    print(f"{title} ({data['year']}): {data['rating']}/10")


def main():
    while True:
        menu_input = menu()
        if menu_input == "0":
            print("Bye!")
            break
        elif menu_input == "1":
            movies = movie_storage.get_movies()
            if not movies:
                print("No movies found.")
            else:
                for title, data in movies.items():
                    print(f"{title} ({data['year']}): {data['rating']}/10")
        elif menu_input == "2":
            while True:
                try:
                    title = input("Enter new movie name: ")
                    if not title:
                        raise ValueError("Title cannot be empty.")
                    year = int(input("Enter the year of release: "))
                    rating = float(input("Enter the rating (0-10): "))
                    movie_storage.add_movie(title, year, rating)
                    print(f"Movie {title} successfully added")
                    break  # Exit loop if input is valid
                except ValueError as e:
                    print(f"Error: {e}")
        elif menu_input == "3":
            while True:
                try:
                    title = input("Enter the movie name to delete: ")
                    if not title:
                        raise ValueError("Title cannot be empty.")
                    movie_storage.delete_movie(title)
                    print(f"Movie {title} deleted (if it existed)")
                    break
                except ValueError as e:
                    print(f"Error: {e}")
        elif menu_input == "4":
            while True:
                try:
                    title = input("Enter the movie name to update: ")
                    if not title:
                        raise ValueError("Title cannot be empty.")
                    rating = float(input("Enter the new rating (0-10): "))
                    movie_storage.update_movie(title, rating)
                    print(f"Movie {title} updated (if it existed)")
                    break
                except ValueError as e:
                    print(f"Error: {e}")
        elif menu_input == "5":
            movies = movie_storage.get_movies()
            if not movies:
                print("No movies found.")
            else:
                ratings = [data['rating'] for data in movies.values()]
                print(f"Average rating: {sum(ratings) / len(ratings):.2f}")
                print(f"Highest rating: {max(ratings)}")
                print(f"Lowest rating: {min(ratings)}")
        elif menu_input == "6":
            movies = movie_storage.get_movies()
            if not movies:
                print("No movies found.")
            else:
                title = random.choice(list(movies.keys()))
                print(f"Your random movie is: {title}")
        elif menu_input == "7":
            search_term = input("Enter search term: ")
            movies = movie_storage.get_movies()
            found = False
            for title, data in movies.items():
                if search_term.lower() in title.lower():
                    print(f"{title} ({data['year']}): {data['rating']}/10")
                    found = True
            if not found:
                print("No movies found matching the search term.")
        elif menu_input == "8":
            movies = movie_storage.get_movies()
            if not movies:
                print("No movies found.")
            else:
                sorted_movies = sorted(movies.items(), key = lambda item: item[1]['rating'], reverse = True)
                for title, data in sorted_movies:
                    display_movie(title, data)
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
