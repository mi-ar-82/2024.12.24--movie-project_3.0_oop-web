# Movie Project 3.0 OOP Web

This project is a web-based movie application developed using Object-Oriented Programming (OOP) principles in Python. It allows users to manage and browse a collection of movies through a web interface.

## Features

- **Movie Management**: Add, edit, and delete movies from your collection.
- **Search Functionality**: Search for movies by title, genre, or release date.
- **Responsive Web Interface**: User-friendly interface accessible from various devices.

## Installation

   
1. Clone the Repository
    ```bash
    git clone https://github.com/mi-ar-82/2024.12.24--movie-project_3.0_oop-web.git
    cd 2024.12.24--movie-project_3.0_oop-web/
   
2. Create a Virtual Environment
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
   
3. Install Dependencies
Install all required Python packages listed in requirements.txt:
    ```bash
    pip install -r requirements.txt
   
   
4. Add Your OMDb API Key
Create a file named .env in the root directory and add your OMDb API key:
    ```python
    # .env
    OMDB_API_KEY = "your_actual_api_key_here"

5. Run the Application
Execute the main script to start the app:
    ```bash
    python main.py
   

---

## Menu Options

#### **1. List Movies**

- **What it does**: Displays all movies stored in the JSON file.
- **How it works**:
  - The app retrieves all movies using `list_movies()` from `StorageJson`.
  - If no movies exist, it outputs: "No movies found."
  - Otherwise, it lists each movie with its title, year, and IMDb rating.
- **Example Output**:
  
  ```
  Inception (2010): 8.8/10
  The Dark Knight (2008): 9.0/10
  ```

---

#### **2. Add Movie**

- **What it does**: Adds a new movie by fetching details from the OMDb API.
- **How it works**:
  - Prompts the user for a movie title.
  - Fetches details (title, year, IMDb rating, poster) from the OMDb API.
  - Saves the movie to storage using `add_movie()`.
  - If the movie is not found in OMDb, it shows an error message.
- **Example Interaction**:
  
  ```
  Enter movie title: Inception
  Movie 'Inception' added successfully!
  ```

---

#### **3. Delete Movie**

- **What it does**: Deletes a movie from storage.
- **How it works**:
  - Prompts the user for a movie title.
  - Deletes the specified movie using `delete_movie()`.
  - If the movie doesn’t exist, it still outputs a success message for simplicity.
- **Example Interaction**:
  
  ```
  Enter the title of the movie to delete: Inception
  Movie 'Inception' deleted (if it existed).
  ```

---

#### **4. Update Movie**

- **What it does**: Updates the IMDb rating of an existing movie.
- **How it works**:
  - Prompts for a movie title and new rating (0–10).
  - Validates that the rating is within range.
  - Updates the rating using `update_movie()`.
  - If the movie doesn’t exist or input is invalid, it shows an error message.
- **Example Interaction**:
  
  ```
  Enter the title of the movie to update: Inception
  Enter new rating (0-10): 9.5
  Movie 'Inception' updated successfully!
  ```

---

#### **5. Show Statistics**

- **What it does**: Displays statistics about the stored movies.
- **How it works**:
  - Calculates total movies, average rating, highest-rated movie, and lowest-rated movie.
  - If no movies exist, outputs: "No movies found."
- **Example Output**:
  
  ```
  Movie Statistics:
  Total Movies: 3
  Average Rating: 8.7
  Highest Rated Movie: The Dark Knight (9.0/10)
  Lowest Rated Movie: Interstellar (8.5/10)
  ```

---

#### **6. Generate Website**

- **What it does**: Creates an HTML website displaying all movies in a grid format.
- **How it works**:
  - Loads all movies from storage using `list_movies()`.
  - Reads an HTML template (`_static/index_template.html`).
  - Generates HTML for each movie with its title, poster image, year, and rating.
  - Saves the final HTML file (`index.html`) in the project directory.
- **Error Handling**:
  - If no movies exist, outputs: "No movies found to generate the website."
  - If the template file is missing, outputs: "Error: Template file not found."
- **Example Interaction**:
  
  ```
  Website generated successfully! Open 'index.html' to view your collection.
  ```

---

#### **0. Exit**

- Exits the application gracefully with a goodbye message.

---
   


