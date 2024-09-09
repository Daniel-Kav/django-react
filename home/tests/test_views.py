from django.contrib.auth.models import User
import pytest


def test_home_view(client):
    print("Testing view for home page...")
    response = client.get(path='/')
    assert response.status_code == 200

def test_signup_view(client):
    response = client.get(path='/signup/')
    assert response.status_code == 200
    assert 'home/register.html' in response.template_name

@pytest.mark.django_db
def test_signup_authentication(client):
    userr = User.objects.create_user('kavatha', 'admin@gmail.com', 'django1234')
    client.login(username = userr.username, password='django1234')

    response = client.get(path = '/signup/', follow  = True)    
    assert response.status_code == 200
    assert 'notes/notes_list.html' in response.template_name