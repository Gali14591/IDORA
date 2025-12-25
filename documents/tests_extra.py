from django.urls import reverse
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile

class DocumentPermissionTests(APITestCase):
    def test_only_owner_sees_documents(self):
        # Register two users and upload a document by user1
        self.client.post(reverse('register'), {'phone': '+300', 'role': 'citizen', 'password': 'S3cureP@ssw0rd!', 'password2': 'S3cureP@ssw0rd!'}, format='json')
        r = self.client.post(reverse('token_obtain_pair'), {'username': '+300', 'password': 'S3cureP@ssw0rd!'}, format='json')
        token = r.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        file = SimpleUploadedFile('f.txt', b'hello')
        resp = self.client.post('/api/documents/', {'title':'t','description':'d','file':file})
        self.assertEqual(resp.status_code, 201)

        # Register second user and verify they see no documents
        self.client.credentials()
        self.client.post(reverse('register'), {'phone': '+400', 'role': 'citizen', 'password': 'S3cureP@ssw0rd!', 'password2': 'S3cureP@ssw0rd!'}, format='json')
        r2 = self.client.post(reverse('token_obtain_pair'), {'username': '+400', 'password': 'S3cureP@ssw0rd!'}, format='json')
        token2 = r2.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token2}')
        resp = self.client.get('/api/documents/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['count'], 0)
