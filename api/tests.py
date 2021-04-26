import inspect

from api.models import Message
from api.utils import send_test_csv_report

from config import settings
User = settings.base.AUTH_USER_MODEL

from rest_framework.test import APIClient, APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

TEST_RESULTS = []
RECIPIENTS = ['omarehap17@gmail.com']

class MessageListTestCase(APITestCase):
    def setUp(self) -> None:
        """
        This method is used for feeding the initial data that is required by every test method defined in the test case class
        """
        self.user = User.objects.create_user(username='test_user', password='adminpass')
        self.other_user = User.objects.create_user(username='other_user', password='adminpass')
        self.message = Message.objects.create(user=self.user, name='Ahmed', message='Ahmed Message')
        self.client = APIClient()
    
    @classmethod
    def tearDownClass(cls):
        User.objects.filter(username__in=['test_user', 'other_user']).delete()

    def test_create_message_with_un_authenticated_user(self):
        """
        In this Test Case we are testing the Message Create API using an unauthenticated user.
        """
        response = self.client.post(reverse('message'), {'name': 'user1', 'message': 'user1 message'}, format='json' )

        is_passed = response.status_code == status.HTTP_403_FORBIDDEN

        TEST_RESULTS.append({
            "result": "Passed" if is_passed else "Failed",
            "test_name": inspect.currentframe().f_code.co_name,
            "test_description": "Un-authenticated user cannot send message"
        })

    def test_get_other_user_message_detail(self):
        """
        In this Test Case we are testing the Message GET API, and trying to get message details of  a user using a different user credentials.
        """
        self.client.login(username='other_user', password='adminpass')

        response = self.client.get(reverse('message', args=[str(self.message.id)]))

        is_passed = response.status_code == status.HTTP_403_FORBIDDEN

        TEST_RESULTS.append({
            "result": "Passed" if is_passed else "Failed",
            "test_name": inspect.currentframe().f_code.co_name,
            "test_description": "Only the Owner can view the Message Detail"
        })

    def test_create_message_with_authanticated_user(self):
        self.client.login(username='test_user',password='adminpass')

        response = self.client.post(reverse('todo'), {'name':'User2', 'message':'user2 message'}, format='json')

        is_passed = response.status_code == status.HTTP_201_CREATED

        TEST_RESULTS.append({
            "result": "Passed" if is_passed else "Failed",
            "test_name": inspect.currentframe().f_code.co_name,
            "test_description": "Message sent successfullt"
        })

    def test_get_message_detail(self):
        self.client.login(username='test_user',password='adminpass')

        response = self.client.get(reverse('message', args=[str(self.message.id)]))

        is_passed = response.status_code == status.HTTP_200_OK

        TEST_RESULTS.append({
            "result": "Passed" if is_passed else "Failed",
            "test_name": inspect.currentframe().f_code.co_name,
            "test_description": "Message Detail Retrieved successfullt"
        })

class CSVReportTest(APITestCase):
    def test_send_csv(self):
        send_test_csv_report(
            test_results=TEST_RESULTS,
            recipients=RECIPIENTS
        )

