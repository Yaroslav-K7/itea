# Создать подобие социальной сети. Описать классы, которые должны
# выполнять соответствующие функции. Добавить проверку на валидность
# пароля (содержание символов и цифр), проверка на уникальность логина
# пользователя. Человек заходит, и имеет возможность зарегистрироваться
# (ввод логин, пароль, подтверждение пароля), далее входит в свою учетную
# запись. Добавить возможность выхода из учетной записи, и вход в новый
# аккаунт. Создать класс User, который будет разделять роли админа и
# простого пользователя (этот вопрос можно решить с помощью флага
# is_admin, либо наследованием). При входе под обычным пользователем мы
# можем добавить новый пост, с определённым содержимым, так же пост
# должен содержать дату публикации. Под учётной записью администратора
# мы можем увидеть всех пользователей нашей системы, дату их регистрации,
# и их посты.
all_users = [{"login": "yarik", 'password': '12345Qwe@'}]


class Login:
    def __init__(self):
        self.admin_pass = "adminadmin"
        self.admin_log = "admin"
        self.is_admin = False
        self.is_authorised = False

    def enter_to_(self):
        self.enter_login = input("Enter your login:")
        for i in all_users:
            if i["login"] == self.enter_login:
                self.user_password = i["password"]
            elif self.enter_login == self.admin_log:
                self.user_password = self.admin_pass
            else:
                self.user_password = None
        return self.enter_login, self.user_password

    def enter_password(self):
        if self.user_password is not None:
            self.password = input(
                "Password requirements:\nOne capital letter, one number and one special character. \n"
                "Also need the length of the password to be between 8 and 18.\n"
                "print 'q!' for exit\n"
                "Enter your password: ")
            print(self.user_password)
            if self.password == self.admin_pass:
                self.is_admin = True
            elif self.password == self.user_password:
                self.is_authorised = True
        else:
            self.user_password = self.password
            self.password_repeat = input("Please, repeat password: ")
            if self.password_repeat != self.user_password:
                pass



class User:
    pass

