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


@pytest.mark.django_db
def test_list_endpoint_return_list_only_authenticatd_user(client):
    # Create the first user and their notes
    userr = User.objects.create_user('kavatha', 'admin@gmail.com', 'django1234')
    kav = User.objects.create_user('kav', 'admin2@gmail.com', 'django1234')
    Notes.objects.create(title='kav title', text='sample text', user=kav)
    
    # Log in as 'userr'
    client.login(username=userr.username, password='django1234')

    # Create notes for 'userr'
    Notes.objects.create(title='sample title', text='sample text', user=userr)
    Notes.objects.create(title='another sample title', text='sample text', user=userr)

    # Get the response
    response = client.get(path='/smart/notes/')
    assert response.status_code == 200

    # Convert the content to string for analysis
    content = str(response.content)

    # Verify that 'userr' notes are in the content
    assert 'sample title' in content
    assert 'another sample title' in content

    # Verify that 'kav' notes are not in the content
    assert 'kav title' not in content

    # Print the content for debugging (optional)
    print(content)

    # Check that there are no <div> tags, or adjust this to the expected count of <div> tags
    div_count = content.count('<div>')
    assert div_count == 0, f"Expected 0 <div> tags but found {div_count}"
