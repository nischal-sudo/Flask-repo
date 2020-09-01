from models.user import UserModel
#User class
def authenticate(username,password):
    user = UserModel.find_by_username(username)#classname.def.(parameter of def)
    if user and user.password == password:#user.password is connected within def itself
        return user

def identity(payload):
    user_id = payload["identity"]#payload of identity
    return UserModel.find_by_id(user_id) # find_by_id of payload("identity")
