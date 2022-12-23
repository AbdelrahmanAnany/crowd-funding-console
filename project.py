
def menu(user_id):
    print(
        "\n\n 1) Create Project \n 2) View All Projects \n 3) Edit Project \n 4) Delete Project \n 5) Search For Project \n 6) Back to Login \n 7) Back to Register \n 8) Exit")

    choice = input("\nPlease choose from menu :\n")
    if choice == "1":
        from create_project import create
        create(user_id)

    elif choice == "2":
        from view_projects import view
        view(user_id)

    elif choice == "3":
        from edit_project import edit
        edit(user_id)

    elif choice == "4":
        from delete_project import delete
        delete(user_id)

    elif choice == "5":
        from search_project import search
        search(user_id)

    elif choice == "6":
        from login import login_app
        login_app()

    elif choice == "7":
        from register import registeration
        registeration()

    elif choice == "8":
        print("See you! ")
        exit()

    else:
        print("\nPlease choose From menu")
    menu(user_id)
