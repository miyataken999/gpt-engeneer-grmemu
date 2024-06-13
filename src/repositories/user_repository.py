from src.models.user import User

class UserRepository:
    def __init__(self):
        self.users = []

    def create_user(self, name, email):
        user = User(name, email)
        self.users.append(user)