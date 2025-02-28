import pytest
from http import HTTPStatus
from app.debug_app import create_app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_request(client):
    """Test a GET request with query parameters."""
    response = client.get('/test?param1=value1&param2=value2')
    data = response.get_json()

    assert response.status_code == HTTPStatus.OK
    assert data['method'] == 'GET'
    assert data['url'] == 'http://localhost/test?param1=value1&param2=value2'
    assert data['args'] == {'param1': 'value1', 'param2': 'value2'}

def test_post_request_json(client):
    """Test a POST request with JSON data."""
    json_data = {'key1': 'value1', 'key2': 'value2'}
    response = client.post('/test', json=json_data)
    data = response.get_json()

    assert response.status_code == HTTPStatus.OK
    assert data['method'] == 'POST'
    assert data['json'] == json_data

def test_post_request_form(client):
    """Test a POST request with form data."""
    form_data = {'param1': 'value1', 'param2': 'value2'}
    response = client.post('/test', data=form_data)
    data = response.get_json()

    assert response.status_code == HTTPStatus.OK
    assert data['method'] == 'POST'
    assert data['form'] == form_data

def test_put_request(client):
    """Test a PUT request with form data."""
    form_data = {'param1': 'value1', 'param2': 'value2'}
    response = client.put('/test', data=form_data)
    data = response.get_json()

    assert response.status_code == HTTPStatus.OK
    assert data['method'] == 'PUT'
    assert data['form'] == form_data

def test_delete_request(client):
    """Test a DELETE request."""
    response = client.delete('/test')
    data = response.get_json()

    assert response.status_code == HTTPStatus.OK
    assert data['method'] == 'DELETE'

def test_invalid_path(client):
    """Test a request to an invalid path."""
    response = client.get('/invalid/path')
    data = response.get_json()

    assert response.status_code == HTTPStatus.OK
    assert data['method'] == 'GET'
    assert data['url'] == 'http://localhost/invalid/path'
