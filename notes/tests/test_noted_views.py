import pytest
from django.contrib.auth.models import User
from notes.models import Notes


@pytest.mark.django_db
def test_list_endpoint_return_list(client):
    userr = User.objects.create_user('kavatha', 'admin@gmail.com', 'django1234')
    client.login(username = userr.username, password='django1234')

    note = Notes.objects.create(title='sample title', text='sample text', user=userr)
    note = Notes.objects.create(title='another sample title', text='sample text', user=userr)
    response = client.get(path='/smart/notes/')
    assert response.status_code == 200
    content = str(response.content)
    assert 'sample title' in content
    assert 'another sample title' in content
    print(content)
    assert 0 == content.count('<div>')