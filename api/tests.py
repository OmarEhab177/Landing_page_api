import inspect
from django.test import TestCase
from .models import Message

from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from config import settings
User = settings.base.AUTH_USER_MODEL
class MessageList(TestCase):
    """
    Normal TestCase
    """
    @classmethod
    def setUpTestData(cls) -> None:
        Message.objects.create(name='Omar', email='test@test.com')
    
    def test_message_name_content(self):
        message = Message.objects.get(id=1)
        expected_message_name = f'{message.name}'
        self.assertEqual(expected_message_name, 'Omar')

    def test_message_email_content(self):
        message = Message.objects.get(id=1)
        expected_message_email = f'{message.email}'
        self.assertEqual(expected_message_email, 'test@test.com')




TEST_RESULTS = []

class MessageListApi(APITestCase):
    """
    API Action Test
    """

    def test_create_message(self):

        response = self.client.post(reverse('message'), {"name": "Ahmed", "email": "test@test.com",}, format='json')

        is_passed = response.status_code == status.HTTP_201_CREATED

        TEST_RESULTS.append({
            'result': 'Passed' if is_passed else 'Failed',
            'test_name': inspect.currentframe().f_code.co_name,
            'test_description': "Trying to create message"
        })
        print(TEST_RESULTS)
    
    def test_retrive_message_detail(self):
        
        message = self.client.post(reverse('message'), {"name": "Eslam", "email": "eslam@test.com",}, format='json')
        is_passed = message.status_code == status.HTTP_201_CREATED

        if is_passed:
            response = self.client.get(reverse('message-detail', args=[str(message.id)]))

            is_passed = response.status_code == status.HTTP_200_OK

            TEST_RESULTS.append({
                'result': 'Passed' if is_passed else 'Failed',
                'test_name': inspect.currentframe().f_code.co_name,
                'test_description': "Trying to retrieve message detail"
            })
            print(TEST_RESULTS)
        else:
            print('message wasn\'t created')