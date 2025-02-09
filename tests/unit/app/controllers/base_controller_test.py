import json

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b'"flask_env":"test"' in response.data
    response_data = json.loads(response.data.decode())
    assert response_data['healthy'] == True
    assert response_data['flask_env'] == 'test'
