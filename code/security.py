from models.user import UserModel

'''
users = [{'id':1, 'username':'hari', 'password':'Winter05'}]
username_mapping = {'hari':{'id':1, 'username':'hari', 'password':'Winter05'}}
userid_mapping = {1:{'id':1, 'username':'hari', 'password':'Winter05'}}
'''
#instead of doing that we can create a class
'''
users = [User(1,'hari','Winter05')]
username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

'''

#To Authenticate the user
def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
