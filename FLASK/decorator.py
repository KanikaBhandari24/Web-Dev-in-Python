def dec(function):
    def wrapper():
        time.sleep(2)
        function()
    return wrapper

import time 
@dec #decorator from the above
def hello():
    print("hello")
hello()

def bye():
    print("Bye")
bye()
