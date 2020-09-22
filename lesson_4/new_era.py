from datetime import datetime
import re
all_users = [{'login': 'yarik', 'password': '12345Qwe!', 'register_time:': '2020-09-22 18:31:10'}]

while True:
    login_input = input("Enter login: ")
    for i in all_users:
        if i["login"] == login_input:
            user_password = i["password"]
            print("This login already exists")

    password_input = input(
                "Password requirements:\nOne capital letter, one number and one special character. \n"
                "Also need the length of the password to be between 8 and 18.\n"
                "print 'q!' for exit\n"
                "Enter your password: ")
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
    match_re = re.compile(reg)
    res = re.search(match_re, password_input)
    if res:
        print("Valid Password")

    elif password_input == "q!":
        break
    else:
        print("Enter correct password")


    repeat_password_input = input("Repeat passport: ")
    post = input("Write a message: ")
    break




class Auth:
    ADMIN_LOGIN = "admin"
    ADMIN_PASSWORD = "adminadmin"

    is_admin = False
    is_authorised = False

    def __init__(self):
        self.login_ = login_input
        self.password_ = password_input
        self.repeat_pass = repeat_password_input
        self.post_ = post

    def register(self):
        if self.password_ == self.repeat_pass:
            all_users.append({"login": self.login_, "password": self.password_,
                              "register_time:": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        else:
            pass

    def login(self):
        for i in all_users:
            if i["login"] == self.login_ and i["password"] == self.password_:
                print('yes')
                self.is_authorised = True
            elif self.login_ == self.ADMIN_LOGIN and self.password_ == self.ADMIN_PASSWORD:
                print("admin")
                self.is_authorised = True
                self.is_admin = True
            else:
                self.register()


class User(Auth):

    #
    # class Post:

    def post(self):
        pass

    def get_users_posts(self):
        pass


a = User()
print(all_users)
a.login()
print(all_users)
a.register()
print(all_users)
