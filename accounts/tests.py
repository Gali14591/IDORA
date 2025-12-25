from django.urls import reverse
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile

class EndToEndTests(APITestCase):
    def test_register_token_document_send_inbox_flow(self):
        # Register sender
        url = reverse('register')
        resp = self.client.post(url, {'phone': '+1000', 'role': 'citizen', 'password': 'S3cureP@ssw0rd!', 'password2': 'S3cureP@ssw0rd!'}, format='json')
        self.assertEqual(resp.status_code, 201)

        # Obtain token
        resp = self.client.post(reverse('token_obtain_pair'), {'username': '+1000', 'password': 'S3cureP@ssw0rd!'}, format='json')
        self.assertEqual(resp.status_code, 200)
        access = resp.data['access']

        # Upload a document
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        file = SimpleUploadedFile('hello.txt', b'Hello Test')
        resp = self.client.post('/api/documents/', {'title': 't', 'description': 'd', 'file': file})
        self.assertEqual(resp.status_code, 201)
        doc_id = resp.data['id']

        # Register recipient
        self.client.credentials()  # clear auth
        resp = self.client.post(url, {'phone': '+2000', 'role': 'citizen', 'password': 'S3cureP@ssw0rd!', 'password2': 'S3cureP@ssw0rd!'}, format='json')
        self.assertEqual(resp.status_code, 201)

        # Send document from sender to recipient
        # Re-auth as sender
        resp = self.client.post(reverse('token_obtain_pair'), {'username': '+1000', 'password': 'S3cureP@ssw0rd!'}, format='json')
        access = resp.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        resp = self.client.post('/api/sends/', {'recipient_phone': '+2000', 'document_id': doc_id, 'message': 'Please see'}, format='json')
        self.assertEqual(resp.status_code, 201)

        # Check inbox for recipient
        resp = self.client.post(reverse('token_obtain_pair'), {'username': '+2000', 'password': 'S3cureP@ssw0rd!'}, format='json')
        recipient_access = resp.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {recipient_access}')
        resp = self.client.get('/api/inbox/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['count'], 1)
