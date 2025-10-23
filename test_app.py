import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test the home page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to Flask Lab Project' in response.data
    assert b'Flask Lab Project' in response.data

def test_about_page(client):
    """Test the about page."""
    response = client.get('/about')
    assert response.status_code == 200
    assert b'About This Project' in response.data
    assert b'Technologies Used' in response.data

def test_contact_page(client):
    """Test the contact page."""
    response = client.get('/contact')
    assert response.status_code == 200
    assert b'Contact Us' in response.data
    assert b'Get in Touch' in response.data

def test_navigation_links(client):
    """Test that navigation links are present on all pages."""
    pages = ['/', '/about', '/contact']
    for page in pages:
        response = client.get(page)
        assert b'Home' in response.data
        assert b'About' in response.data
        assert b'Contact' in response.data

def test_404_page(client):
    """Test that invalid routes return 404."""
    response = client.get('/nonexistent')
    assert response.status_code == 404

def test_css_linked(client):
    """Test that CSS file is linked in pages."""
    response = client.get('/')
    assert b'style.css' in response.data

def test_home_features(client):
    """Test that home page shows feature cards."""
    response = client.get('/')
    assert b'Flask Framework' in response.data
    assert b'Docker Ready' in response.data
    assert b'CI/CD Pipeline' in response.data

def test_about_technologies(client):
    """Test that about page lists technologies."""
    response = client.get('/about')
    assert b'Flask' in response.data
    assert b'Docker' in response.data
    assert b'GitHub Actions' in response.data

def test_contact_info(client):
    """Test that contact page has project information."""
    response = client.get('/contact')
    assert b'GitHub Repository' in response.data
    assert b'fa22-bse-057' in response.data
