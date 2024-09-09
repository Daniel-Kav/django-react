def test_home_view(client):
    print("Testing view for home page...")
    response = client.get(path='/')
    assert response.status_code == 200

def test_signup_view(client):
    response = client.get(path='/signup/')
    assert response.status_code == 200
    assert 'home/register.html' in response.template_name