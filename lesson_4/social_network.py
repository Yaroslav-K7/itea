from datetime import datetime
import re

ALL_USERS = [
    {'login': 'yarik', 'password': '12345Qwe!', 'is_admin': True, 'register_time:': '2020-09-22 18:31:10'}
]


class User:

    def __init__(self, username, password):
        self.username = username
        self.password_ = password
        self.is_authorised = False
        self.is_admin = False

    @staticmethod
    def is_password_match_requirements(password):
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
        match_re = re.compile(reg)
        res = re.search(match_re, password)
        if res:
            return True
        return False

    @staticmethod
    def is_password_correct(password, correct_password):
        if password == correct_password:
            return True
        return False

    def register(self):
        if self.is_password_match_requirements(self.password_):
            ALL_USERS.append(
                {"login": login_input, "password": self.password_,
                 "register_time:": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                 }
            )
            self.is_authorised = True
        else:
            raise Exception("You aren't authorised")

    def login(self):
        user = [user for user in ALL_USERS if user['login'] == self.username][0]
        correct_password = user.get('password')
        if self.is_password_correct(self.password_, correct_password):
            if user.get('is_admin'):
                self.is_authorised = True
                self.is_admin = True
            else:
                self.is_authorised = True
        else:
            raise Exception("You aren't login")

    def logout(self):
        if self.is_authorised:
            self.is_authorised = False
        else:
            raise Exception("You aren't login")

    def create_post(self, post):
        if self.is_authorised:
            user = [user for user in ALL_USERS if user['login'] == self.username][0]
            user.update({'post': post, 'post_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        else:
            raise Exception("You don't have a permission")

    def get_all_information_about_users(self):
        if self.is_admin:
            return ALL_USERS
        else:
            raise Exception("You don't have a permission")


# ---------------------------------------------------------------------------------------------

login_input = input("Enter login: ")
usernames = [user.get('login') for user in ALL_USERS]
if login_input not in usernames:
    print("Redirection to registration")
    for i in range(3):
        password_input = input(
            "Password requirements:\nOne capital letter, one number and one special character. \n"
            "Also need the length of the password to be between 8 and 18.\n"
            "print 'q!' for exit\n"
            "Enter your password: "
        )
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
        match_re = re.compile(reg)
        res = re.search(match_re, password_input)
        if not res:
            print("Incorrect password")
        else:
            repeat_password_input = input('Repeat your password: ')
            if password_input == repeat_password_input:
                user = User(login_input, password_input)
                user.register()
                break
            else:
                continue

        print(f"Your tries {i+1}/3")
else:
    for i in range(3):
        password_input = input("Enter your password: ")
        try:
            user = User(login_input, password_input)
            user.login()
        except Exception:
            print(f"Your tries {i+1}/3")
            continue
        else:
            post_input = input("Write your post: ")
            user.create_post(post_input)
            user.get_all_information_about_users()
            break

    else:
        print("Password attempts ended")
