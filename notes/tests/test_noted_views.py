import pytest
from django.contrib.auth.models import User
from notes.models import Notes
from .factories import UserFactory,NoteFactory

@pytest.fixture
def logged_user(client):
    # userr = User.objects.create_user('kavatha', 'admin@gmail.com', 'django1234')
    userr = UserFactory()
    client.login(username = userr.username, password='password')
    return userr

@pytest.mark.django_db
def test_list_endpoint_return_list(client, logged_user):
    note = Notes.objects.create(title='sample title', text='sample text', user=logged_user)
    note = Notes.objects.create(title='another sample title', text='sample text', user=logged_user)
    response = client.get(path='/smart/notes/')
    assert response.status_code == 200
    content = str(response.content)
    assert 'sample title' in content
    assert 'another sample title' in content
    print(content)
    assert 0 == content.count('<div>')


@pytest.mark.django_db
def test_list_endpoint_return_list_only_authenticatd_user(client, logged_user):
    # Create the first user and their notes
    # userr = User.objects.create_user('kavatha', 'admin@gmail.com', 'django1234')
    kav = User.objects.create_user('kav', 'admin2@gmail.com', 'django1234')
    NoteFactory(user=kav)
    
    # Log in as 'userr'
    # client.login(username=logged_user.username, password='django1234')

    # Create notes for 'userr'
    note =NoteFactory( user=logged_user)
    secondnote = NoteFactory( user=logged_user)

    # Get the response
    response = client.get(path='/smart/notes/')
    assert response.status_code == 200

    # Convert the content to string for analysis
    content = str(response.content)

    # Verify that 'userr' notes are in the content
    assert note.title in content
    assert secondnote.title in content

    # Verify that 'kav' notes are not in the content
    assert 'kav title' not in content

@pytest.mark.django_db
def test_create_endpoint(client, logged_user):
    form_data = {'title': 'title title','text': 'text title'}
    response = client.post(path='/smart/notes/new/', data=form_data, follow =True)

    assert response.status_code == 200
    assert 'notes/notes_form.html' in response.template_name