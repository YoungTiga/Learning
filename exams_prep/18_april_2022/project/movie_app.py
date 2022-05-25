from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def check_if_user_exists(self, username):
        for user in self.users_collection:
            if user.username == username:
                return True
        return False

    def check_if_movie_exists(self, title):
        for movie in self.movies_collection:
            if movie.title == title:
                return True
        return False

    def check_if_user_liked_movie(self, username, movie_title):
        for user in self.users_collection:
            if user.username == username:
                for movie in user.movies_liked:
                    if movie.title == movie_title:
                        return True
                return False

    def register_user(self,username: str, age: int):
        user = User(username,age)
        if username in [user.username for user in self.users_collection]:
            raise Exception("User already exists!")
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self,username: str, movie: Movie):
        user = [user for user in self.users_collection if user.username == username]
        if username not in [user.username for user in self.users_collection]:
            raise Exception("This user does not exist!")
        current_user = user[0]
        if not movie.owner.username == username:
            raise Exception(f"{current_user.username} is not the owner of the movie {movie.title}!")
        if movie.title in [m.title for m in self.movies_collection]:
            raise Exception("Movie already added to the collection!")
        current_user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self,username: str, movie: Movie, **kwargs):
        if movie.title not in [m.title for m in self.movies_collection]:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        user = [user for user in self.users_collection if user.username == username][0]
        if not movie.owner.username == username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attr, value in kwargs.items():
            setattr(movie,attr,value)
            # movie.attr = value
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self,username: str, movie: Movie):
        if movie.title not in [m.title for m in self.movies_collection]:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        user = [user for user in self.users_collection if user.username == username][0]
        if not movie.owner.username == username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        # user.movies_owned.remove(movie)
        self.movies_collection.pop(self.movies_collection.index(movie))
        # self.movies_collection.remove(movie)
        user.movies_owned.pop(user.movies_owned.index(movie))
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self,username: str, movie: Movie):
        user = [user for user in self.users_collection if user.username == username][0]
        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie.title in [m.title for m in user.movies_liked]:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self,username: str, movie: Movie):
        user = [user for user in self.users_collection if user.username == username][0]
        if movie.title not in [m.title for m in user.movies_liked]:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        # user.movies_liked.remove(movie)
        user.movies_liked.pop(user.movies_liked.index(movie))
        return f"{username} disliked {movie.title} movie."


    def display_movies(self):
        res = ''
        if not self.movies_collection:
            return "No movies found."

        sorted_movies = sorted(self.movies_collection, key = lambda x: (-x.year,x.title))
        for movie in sorted_movies:
            res += movie.details()+"\n"

        return res.strip()

    def __str__(self):
        res = ""
        if not self.users_collection:
            res += "All users: No users.\n"
        else:
            res += f"All users: {', '.join(user.username for user in self.users_collection)}\n"

        if not self.movies_collection:
            res +=  "All movies: No movies.\n"
        else:
            res += f"All movies: {', '.join(movie.title for movie in self.movies_collection)}\n"

        return  res.strip()

