def user_id():
    with open(r"users_data.txt", 'r') as fp:
        x = len(fp.readlines())
        return x+1
user_id()