import pytest
from app import app
from health_utils import calculate_bmi, calculate_bmr

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_bmr_calculation():
    
    male_bmr = calculate_bmr(175, 70, 30, "male")
    female_bmr = calculate_bmr(165, 55, 25, "female")
    assert round(male_bmr, 2) == 1695.67, f"Expected 1695.67 but got {male_bmr}"
    assert round(female_bmr, 2) == 1359.10, f"Expected 1359.10 but got {female_bmr}"

def test_bmr_endpoint(client):
   
    response = client.post('/bmr', json={
        'height': 175,
        'weight': 70,
        'age': 30,
        'gender': 'male'
    })
    assert response.status_code == 200, "Expected status code 200"
    data = response.get_json()
    assert 'bmr' in data, "Response missing 'bmr' key"
    assert round(data['bmr'], 2) == 1695.67, f"Expected BMR 1695.67 but got {data['bmr']}"
