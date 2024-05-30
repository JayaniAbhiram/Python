class User:
    pass

# CONSTRUCTOR

class User:
    def __init__(self):
        print("this is a constructoe")

        


user1 = User()

user1.id = 12
user1.name = "abhi"

print(user1.name)
    

# THIS IS THE SECOND WAY

class User:
    username = "abbhi"
    id =12

print(User.username)