#from django.contrib.auth.models import User
#
#from rest_framework                  import status
#from rest_framework.authtoken.models import Token
#from rest_framework.test             import APITestCase
#
#from .models import Payment
#
#class AdminTestCase(APITestCase):
#    def setUp(self):
#        self.user  = User.objects.create_user(id=1, username='admin', password='0000', is_staff = True)
#        self.token = Token.objects.create(user=self.user)
#        self.api_authentication()
#
#        User.objects.create_user(id=2, username='0101', password='0000', is_staff = False)
#        User.objects.create_user(id=3, username='0102', password='0000', is_staff = False)
#        Payment.objects.create(id=1, name="0101", pay=1000, user_id=2)
#        Payment.objects.create(id=2, name="0102", pay=2000, user_id=3)
#
#    def api_authentication(self):
#        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
#
#    def test_public_list_authenticated(self):
#        response = self.client.get('/api/admin/')
#        self.assertEqual(response.status_code, status.HTTP_200_OK)
#        self.assertEqual(response.json(), [
#            {
#                'id'   : 1,
#                'name' : '0101',
#                'pay'  : '1000.0',
#                'user' : 2
#            },
#            {
#                'id'   : 2,
#                'name' : '0102',
#                'pay'  : '2000.0',
#                'user' : 3
#            },
#            ])
#
#    def test_public_list_un_authenticated(self):
#        self.client.force_authenticate(user=None)
#        response = self.client.get('/api/admin/')
#        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#
#class PublicTestCase(APITestCase):
#    def setUp(self):
#        self.user  = User.objects.create_user(id=1, username='0101', password='0000', is_staff = False)
#        self.token = Token.objects.create(user=self.user)
#        self.api_authentication()
#
#        User.objects.create_user(id=2, username='0102', password='0000', is_staff = False)
#        Payment.objects.create(id=1, name="0101", pay=1000, user_id=1)
#        Payment.objects.create(id=2, name="0102", pay=2000, user_id=2)
#
#    def api_authentication(self):
#        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
#
#    def test_public_list_authenticated(self):
#        response = self.client.get('/api/public/')
#        self.assertEqual(response.status_code, status.HTTP_200_OK)
#        self.assertEqual(response.json(), [
#            {
#                'name' : '0101',
#                'pay'  : '1000.0',
#            }
#            ])
#
#    def test_public_list_un_authenticated(self):
#        self.client.force_authenticate(user=None)
#        response = self.client.get('/api/public/')
#        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
