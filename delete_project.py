from view_projects import view
def delete(user_id):
    all_projects = view(user_id)
    project_name = input('\nSelect one projct to delete : ')
    for project in all_projects:
        user_project = project.strip("\n")
        user_project = user_project.split(":")
        if user_project[1] == project_name and user_id==user_project[0]:
            all_projects.remove(project)
            break
    else:
        print("this project name doesn't exist ,, please try again")
    w = open("projects_data.txt", "w")
    w.writelines(all_projects)
    w.close()
