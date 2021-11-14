from app import app
import cv2

def test1():
    response = app.test_client().get('/')
    assert response.status_code == 200
def test2():
    response = app.test_client().get('/home')
    assert response.status_code == 200

def test3():
    response = app.test_client().get('/upload')
    assert response.status_code == 200

