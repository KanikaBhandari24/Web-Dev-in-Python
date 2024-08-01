class user:
    def __init__(self, name):
        self.name=name
        self.logged_in=False

def authenticated(function):
    def wrapper(*args, **kwargs):
        if args[0].logged_in == True:
            function(args[0])
    return wrapper

@authenticated
def blog(user):
    print(f"This is {user.name}'s new blog post.")

new=user("kanika")
new.logged_in=True
blog(new) 
        