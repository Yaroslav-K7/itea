from datetime import datetime
import re

all_users = [{'login': 'Yarik', 'password': '12345Qwe@'}]


class User:
    admin_pas = "adminadmin"
    admin_log = "admin"
    is_admin = False
    is_authorised = False

    @staticmethod
    def login_to_social_network():

        global user_password
        login = input("Enter your login:")
        for i in all_users:
            if i["login"] == login:
                user_password = i["password"]
                print(user_password)

        while True:
            password = input(
                "Password requirements:\nOne capital letter, one number and one special character. \n"
                "Also need the length of the password to be between 8 and 18.\n"
                "print 'q!' for exit\n"
                "Enter your password: ")

            if password == user_password:
                User.is_authorised = True
                break

            else:
                password_repeat = input("Please, repeat password: ")
                if password_repeat != password:
                    print("Password mismatch")
                else:
                    print("Welcome to new social!")

                reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
                match_re = re.compile(reg)
                res = re.search(match_re, password)
                if res:
                    print("Valid Password")
                    all_users.append({"login": login, "password": password})
                    break

                elif password == "q!":
                    break
                elif password == User.admin_pas:
                    User.is_admin = True
                    break
                else:
                    print("Invalid Password")
            print(all_users)


User.login_to_social_network()
