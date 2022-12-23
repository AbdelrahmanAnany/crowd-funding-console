import re
# imports regular expressions
from user_id import *


def registeration(user_id=user_id()):
    first_name = input("Enter your First name : ")
    last_name = input("Enter your Last name : ")
    email = input("Enter your Email : ")
    password = input("Enter a Password : ")
    confirm_password = input("Confirm password : ")
    mobile_phone = input("Enter your Mobile phone : ")

    # Name Validation
    if first_name.isdigit() or not first_name:
        print("\nyour name is invalid ,, please enter a valid name")
        registeration(user_id)
    else:
        # Email Validation
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if (re.search(regex, email)):
            # Password Validation
            if password == confirm_password:
                # Mobile Phone Validation
                if re.match("^01[0125][0-9]{8}$", mobile_phone):
                    try:
                        users_data = open("users_data.txt", "a")
                    except Exception as e:
                        print(e)
                    else:
                        user_data = f"{user_id}:{first_name}:{last_name}:{email}:{password}:{mobile_phone}\n"
                        users_data.write(user_data)
                        users_data.close()

            else:
                print("\nYour password is invalid, please enter a valid password :")
                registeration(user_id)
        else:
            print("Invalid Email, please try again")
            registeration(user_id)
