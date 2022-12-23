import register
from project import menu


def login_app():
    user_email = input("Email : ")
    password = input("Password : ")
    try:
        user_file = open('users_data.txt', 'r')
    except Exception as e:
        print(e)
    else:
        users = user_file.readlines()
        for user in users:
            userdata = user.strip("\n")
            userinfo = userdata.split(":")

            if userinfo[3] == user_email and userinfo[4] == password:
                print("logged in successfully")
                menu(userinfo[0])
                break
        else:
            print("invalid data, please register first: ")
            register.registeration()
