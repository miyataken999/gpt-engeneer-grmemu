import pytest
from src.services.user_service import UserService

def test_create_user():
    user_service = UserService()
    user_service.create_user("John Doe", "johndoe@example.com")
    assert len(user_service.user_repository.users) == 1