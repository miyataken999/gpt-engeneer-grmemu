from src.repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, name, email):
        self.user_repository.create_user(name, email)