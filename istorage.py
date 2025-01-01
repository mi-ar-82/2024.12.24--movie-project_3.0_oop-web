from abc import ABC, abstractmethod
#This interface specifies the methods required for any storage mechanism. (json,csv, other)


class IStorage(ABC):
    #Interface for storage classes. Defines CRUD operations.

    @abstractmethod
    def list_movies(self):
        #Returns a dictionary of all movies.
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        #Adds a new movie to the storage.
        pass

    @abstractmethod
    def delete_movie(self, title):
        #Deletes a movie from the storage.
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        #Updates the rating of a movie in the storage.
        pass
