class Profile:

    def __init__(self, name, password):

        self.__name = name

        self.__password = password
        if   len(self.get_name()) < 5 or len(self.get_name()) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        if len(self.get_password()) < 8 or not any([x.isupper() for x in self.get_password()]) or not any([x.isdigit() for x in self.get_password()]):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
    def get_name(self):
        return self.__name

    def get_password(self):
        return self.__password




    def __str__(self):
        return f'You have a profile with username: "{self.__name}" and password: {"*"*len(self.__password)}'


# profile_with_invalid_password = Profile('My_username', 'mypassword1')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
