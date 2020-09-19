from datetime import datetime
import re


class Users:
    admin_pas = "adminadmin"
    admin_log = "admin"
    is_admin = False
    all_users = []

    @staticmethod
    def login_to_social_network():

        login = input("Enter your login:")
        if login in Users.all_users:
            print(Users.all_users, login, "!!!!!!")
            #???

        elif login not in Users.all_users:

            while True:
                print(Users.all_users)

                password = input("Password requirements:\nOne capital letter, one number and one special character. \n"
                                 "Also need the length of the password to be between 8 and 18.\n"
                                 "print 'q!' for exit\n"
                                 "Enter your password: ")

                reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
                match_re = re.compile(reg)
                res = re.search(match_re, password)
                if res:
                    print("Valid Password")
                    Users.all_users.append([login, password])
                    break
                elif password == "q!":
                    break
                elif password == Users.admin_pas:
                    Users.is_admin = True

                else:
                    print("Invalid Password")


Users.login_to_social_network()
print(Users.all_users)
