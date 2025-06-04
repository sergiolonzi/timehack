from django.test import TestCase
from ninja.testing import TestClient
from timehack_app.views import router
from timehack_app.models import ListOfTasks
from django.contrib.auth.models import User


class ViewTest(TestCase):

    def setUp(self):
        user = User.objects.create_user("", "", "")
        user.save()
        list_of_tasks = ListOfTasks()
        list_of_tasks.name = "name"
        list_of_tasks.user = user
        list_of_tasks.description = "description"
        list_of_tasks.save()



    def test_get_list_of_tasks(self):
        client = TestClient(router)
        response = client.get("/list-of-tasks/1")
        self.assertEqual(response.status_code, 200)
        
        expected_response = {
				  "id": 1,
				  "name": "name",
				  "description": "description",
				  "user": {
				    "id": 1,
				    "username": "",
				    "email": ""
				  }
				}
        print(response.json())
        self.assertEqual(response.json(), expected_response)

