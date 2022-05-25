from project.user import User
from project.library import Library

class Registration:

    def add_user(self,user: User, library: Library):
        if any([x.username==user.username for x in library.user_records]):
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    def remove_user(self,user: User, library: Library):
        if not any([x.username == user.username for x in library.user_records]):
            return "We could not find such user to remove!"
        user_to_remove = [x for x in library.user_records if x.username == user.username][0]
        library.user_records.remove(user_to_remove)

    def change_username(self,user_id: int, new_username: str, library: Library):
        if not any([x.user_id==user_id for x in library.user_records]):
            return f"There is no user with id = {user_id}!"
        current_user = [x for x in library.user_records if x.user_id==user_id][0]

        if new_username == current_user.username:
            return "Please check again the provided username - it should be different than the username used so far!"
        if current_user.username in library.rented_books:
            library.rented_books[new_username] = library.rented_books[current_user.username]
        current_user.username = new_username
        return f"Username successfully changed to: {new_username} for user id: {user_id}"
