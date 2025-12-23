import requests 

base_url = "https://web-agr.chitai-gorod.ru/web/api/"
key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIzMTg1NzkyLCJpYXQiOjE3NjY1MDg5NjYsImV4cCI6MTc2NjUxMjU2NiwidHlwZSI6MjAsImp0aSI6IjAxOWI0YzIzLWIzZDYtN2JkNC1hNTg2LTU4ZDJlNTlkMzk5NyIsInJvbGVzIjoxMH0.t7ZI5HZV4DC8Zm3qF70y-qh9Muyx8N0gGuDJQVZiwos"

def test_find_book_positive():
    headers = {"Authorization": f"Bearer {key}"}
    params = {"phrase": "Возлюби+болезнь+свою"}
    
    response = requests.get(f"{base_url}v2/search/facet-search", headers=headers, params=params)
    assert response.status_code == 200 


def test_add_book_positive():
    headers = {"Authorization": f"Bearer {key}"} 
    body = {"id":2633292}

    response = requests.post(f"{base_url}v2/search/facet-search", headers=headers, params=params)
    assert response.status_code == 200 


def test_chenge_number_book_positive():
    headers = {"Authorization": f"Bearer {key}"}
    body = {["id": 225454798,
        "quantity": 3]}
    response = requests.post(f"{base_url}v2/search/facet-search", headers=headers, params=params)
    assert response.status_code == 200 
    

def test_invalid_characters_negative():
    headers = {"Authorization": f"Bearer {key}"}
    params = {"phrase": "%26******^"}

    response = requests.get(f"{base_url}v2/search/facet-search", headers=headers, params=params)
    assert response.status_code == 401


def test_incorrect_id_negative():
    headers = {"Authorization": f"Bearer {key}"} 
    body = {"id":263329}

    response = requests.post(f"{base_url}v2/search/facet-search", headers=headers, params=params)
    assert response.status_code == 401

    
