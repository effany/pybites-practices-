from functools import wraps

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    @wraps(func)
    def login(*args, **kwargs):
        user = args[0]
        if user in loggedin_users:
            return f'welcome back {user}'
        elif user in known_users and user not in loggedin_users:
            return f'please login'
        else:
            return 'please create an account'
    return login




@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    return 
