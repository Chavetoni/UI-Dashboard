# 1. Create a tests.py file in your client_portal app directory:
# client_portal/tests.py

from django.test import TestCase, Client
from django.urls import reverse

class URLTests(TestCase):
    
    def setUp(self):
        # Create a test client
        self.client = Client()
        
    def test_index_url(self):
        """Test the root URL redirects correctly."""
        response = self.client.get('/')
        # Since index redirects to dashboard for authenticated users and login for unauthenticated
        # We expect a redirect (302) since we're not authenticated
        self.assertEqual(response.status_code, 302)
        
    def test_login_url(self):
        """Test the login URL loads correctly."""
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        
    def test_dashboard_url(self):
        """Test the dashboard URL requires authentication."""
        response = self.client.get('/dashboard')
        # Should redirect to login since we're not authenticated
        self.assertEqual(response.status_code, 302)

    def test_project_detail_url(self):
        """Test the project detail URL requires authentication."""
        response = self.client.get('/projects/1/')
        # Should redirect to login since we're not authenticated
        self.assertEqual(response.status_code, 302)
