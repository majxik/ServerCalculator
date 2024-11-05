import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test the /calculate endpoint

# Test Add
def test_add(client):
    response = client.post('/calculate', json={'operation': 'add', 'num1': 1, 'num2': 2})
    assert response.status_code == 200
    assert response.json == {'result': 3}

# Test Subtract
def test_subtract(client):
    response = client.post('/calculate', json={'operation': 'subtract', 'num1': 3, 'num2': 2})
    assert response.status_code == 200
    assert response.json == {'result': 1}

# Test Multiply
def test_multiply(client):
    response = client.post('/calculate', json={'operation': 'multiply', 'num1': 3, 'num2': 2})
    assert response.status_code == 200
    assert response.json == {'result': 6}

# Test Divide
def test_divide(client):
    response = client.post('/calculate', json={'operation': 'divide', 'num1': 6, 'num2': 2})
    assert response.status_code == 200
    assert response.json == {'result': 3}

# Test Division by zero
def test_divide_by_zero(client):
    response = client.post('/calculate', json={'operation': 'divide', 'num1': 6, 'num2': 0})
    assert response.get_json() == {'error': 'Division by zero'}

# Test Invalid operation
def test_invalid_operation(client):
    response = client.post('/calculate', json={'operation': 'modulus', 'num1': 6, 'num2': 3})
    assert response.get_json() == {'error': 'Invalid operation'}

# Test Missing operation
def test_missing_operation(client):
    response = client.post('/calculate', json={'num1': 1, 'num2': 2})
    assert response.status_code == 400

# Test Missing num1
def test_missing_num1(client):
    response = client.post('/calculate', json={'operation': 'add', 'num2': 2})
    assert response.status_code == 400

# Test Missing num2
def test_missing_num2(client):
    response = client.post('/calculate', json={'operation': 'add', 'num1': 1})
    assert response.status_code == 400

# Test non-numeric num1
def test_non_numeric_num1(client):
    response = client.post('/calculate', json={'operation': 'add', 'num1': 'one', 'num2': 2})
    assert response.status_code == 400

# Test non-numeric num2
def test_non_numeric_num2(client):
    response = client.post('/calculate', json={'operation': 'add', 'num1': 1, 'num2': 'two'})
    assert response.status_code == 400

# Test corupted JSON
def test_corrupted_json(client):
    response = client.post('/calculate', data='{"operation": "add", "num1": 1, "num2": 2')
    assert response.status_code == 415