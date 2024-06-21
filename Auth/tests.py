from django.test import TestCase, Client
from django.urls import reverse
from .models import User
from django.contrib import messages
from Auth.forms import LoginForm, SignupForm

class LoginViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            first_name='test',
            last_name='user',
            email='testuser@example.com', 
            password='testpassword'
        )
        
    def test_get_login(self):
        response = self.client.get(reverse('Auth:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Auth/login.html')
        self.assertIsInstance(response.context['form'], LoginForm)

    def test_post_login_success(self):
        response = self.client.post(reverse('Auth:login'), {
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'remember_me': True
        })
        self.assertRedirects(response, reverse('Shop:home'))
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(str(messages_list[0]), 'Welcome test!')

    def test_post_login_failure(self):
        response = self.client.post(reverse('Auth:login'), {
            'email': 'wronguser@example.com',
            'password': 'wrongpassword',
        })
        self.assertRedirects(response, reverse('Auth:login'))
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(str(messages_list[0]), 'Login failed. Please check your username and password.')


class SignupViewTests(TestCase):
    
        def setUp(self):
            self.client = Client()
            
        def test_get_signup(self):
            response = self.client.get(reverse('Auth:signup'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'Auth/signup.html')
            self.assertIsInstance(response.context['form'], SignupForm)
    
        def test_post_signup_success(self):
            response = self.client.post(reverse('Auth:signup'), {
                'first_name': 'test',
                'last_name': 'user',
                'email': 'test@green.com',
                'password1': 'testpassword',
                'password2': 'testpassword'
            })
            self.assertRedirects(response, reverse('Auth:login'))
            messages_list = list(messages.get_messages(response.wsgi_request))
            self.assertEqual(len(messages_list), 1)
            self.assertEqual(str(messages_list[0]), 'test account has been created successfully. Please login to continue.')
        def test_post_signup_failure(self):
            response = self.client.post(reverse('Auth:signup'), {
                'first_name': 'test',
                'last_name': 'user',
                'email': 'test2@t.com',
                'password1': 'testpassword',
                'password2': 'testpassword'
            })
            self.assertRedirects(response, reverse('Auth:signup'))
            messages_list = list(messages.get_messages(response.wsgi_request))
            self.assertEqual(len(messages_list), 1)
            self.assertEqual(str(messages_list[0]), 'Please check your inputs')