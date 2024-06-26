import pytest
from fastapi.testclient import TestClient
from app.views import app

client = TestClient(app)

def test_add():
    payload = {"batchid" : "id0101",
               "payload" : [[1,2],[3,4]]}
    
    response = client.post('api/add', json= payload)
    assert response.status_code == 200
    data = response.json()
    assert data['batcid'] == 'id0101'
    assert data['response'] == [3,7]
    assert data['status'] == 'completed'
    assert 'started_at' in data 
    assert 'completed_at' in data

def test_add_check_empty_paylod():
    payload = {"batchid" : "id0101",
               "payload" : []}
    response = client.post('api/add', json= payload)
    assert response.status_code == 200
    data = response.json()
    assert data['batcid'] == 'id0101'
    assert data['response'] == []
    assert data['status'] == 'completed'
    assert 'started_at' in data 
    assert 'completed_at' in data
    
def test_add_invalide_payload():
    payload = {"batchid" : "id0101",
               "payload" : [[1,'n'], [3,4]]}
    response = client.post('api/add', json= payload)
    assert response.status_code == 422