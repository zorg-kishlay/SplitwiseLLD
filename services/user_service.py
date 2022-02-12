from models.user import User
from services.user_service_interface import UserServiceInterface


class UserService(UserServiceInterface):
    users = {}
    
    def add_user(self, id, name):
        user = User()
        user.setId(id)
        user.setName(name)
        self.__class__.users[id]=user
        return user