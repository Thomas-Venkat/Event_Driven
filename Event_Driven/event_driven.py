from functions import notify_friends, send_mail
from event_systems import register_event, dispatch

# services.py
def create_user(username: str, password: str):
    # User(username, password).save()
    print("User was saved", username, password)
    dispatch('user registered', username)




# main.py/bootstrap.py
register_event("user registered", send_mail)
register_event("user registered", notify_friends)

create_user("Thomas", "aadhumyworld")