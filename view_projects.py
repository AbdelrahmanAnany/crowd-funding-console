# from project import menu

def view(user_id):

    try:
        users_projects = open("projects_data.txt", "r")
    except Exception as e:
        print(e)
    else:
        projects = users_projects.readlines()
        for project in projects:
            user_project = project.strip("\n")
            projinfo = user_project.split(":")
            print(projinfo)
        users_projects.close()
        return projects
