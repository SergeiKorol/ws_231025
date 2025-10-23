import requests

#Создать задачу, Проставить отметку о выполнении и проверить что completed ==True

def test_task():
    # создаю
    body = {"title":"generated","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]
        
    assert response.status_code == 202

    # редактирую
    body = {"completed":True}
    requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)

    # Проверяю что значение completed изменилось

    response = requests.get(f"https://todo-app-sky.herokuapp.com/{id}")
    completed = response.json()["completed"]

    assert response.status_code == 200
    assert completed == True
