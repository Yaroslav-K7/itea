import datetime

login_input = input("Enter login: ")
password_input = input("Enter password: ")
repeat_password_input = input("Repeat passport: ")
post = input("Write a message: ")


class Auth:

    is_admin = False
    is_authorised = False

    def __init__(self):
        self.login_ = login_input
        self.password_ = password_input
        self.repeat_pass = repeat_password_input
        self.post_ = post

    def register(self):
        pass

    def login(self):
        pass


class User(Auth):

    all_users = [{'login': 'admin', 'password': 'adminadmin'}]


class Post:

    def post(self):
        pass

    def get_users_posts(self):
        pass
