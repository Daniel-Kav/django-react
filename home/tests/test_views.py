def test_home_view(client):
    print("Testing view for home page...")
    response = client.get(path='/')
    assert response.status_code == 200