from register import registeration
from login import login_app


print("Please select either Registeration or login : \n 1) Registeration \n 2) Login \n 3) Exit")
choice = input(
    "If this is your first time to login to the app please select Registeration : \n")

if choice == "1":
    registeration()
elif choice == "2":
    login_app()
elif choice == "3":
    print("See you! ")
    exit()
