from app.utils import get_user_by_username

def test_username():
    username = "test_user"
    email = "test@example.com"
    result = get_user_by_username(username, email)
    assert isinstance(result, str)
