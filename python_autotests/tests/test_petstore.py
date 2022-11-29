import requests
import pytest

def test_statuscode():
    response = requests.get("https://petstore.swagger.io/v2/pet/228")
    assert response.status_code == 200

def test_piece_of_budy():
    response = requests.get("https://petstore.swagger.io/v2/pet/228")
    assert response.json()['name'] == 'python'