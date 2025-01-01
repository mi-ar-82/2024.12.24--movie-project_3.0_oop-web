from storage_json import StorageJson

# Initialize storage with a test JSON file path
storage = StorageJson('test_movies.json')

# Step 1: List movies (should be empty initially)
print("Initial movies:", storage.list_movies())

# Step 2: Add a new movie
storage.add_movie("Inception", 2010, 8.8, "inception_poster.jpg")
print("After adding Inception:", storage.list_movies())

# Step 3: Add another movie
storage.add_movie("The Matrix", 1999, 9.0, "matrix_poster.jpg")
print("After adding The Matrix:", storage.list_movies())

# Step 4: Update a movie's rating
storage.update_movie("Inception", 9.2)
print("After updating Inception's rating:", storage.list_movies())

# Step 5: Delete a movie
storage.delete_movie("The Matrix")
print("After deleting The Matrix:", storage.list_movies())

# Step 6: List movies again (should only contain Inception)
print("Final movies:", storage.list_movies())
