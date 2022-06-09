d = {"user1": "pass1", "user2": "pass2", "user3": "pass3"}


class InvalidPassword(Exception):
    def __init__(self, msg="Error"):
        self.msg = msg

    def __str__(self):
        return self.msg


for i in range(3):
    try:
        u = input("Enter username :- ")
        p = input("Enter password :- ")
        v = d[u]
        if v == p:
            print("Welcome to ur system")
            print("Display menu driven")
            break
        else:
            raise InvalidPassword("Credentials are wrong")
    except (KeyError, InvalidPassword) as e:
        print("Please Enter Proper Credentials")
        print(e)
    except:
        print("Error occurred")
else:
    print("Your account is blocked for the rest of the day")
