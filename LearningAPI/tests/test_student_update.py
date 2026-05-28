from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from LearningAPI.models import NssUser

class StudentPartialUpdateTests(APITestCase):
    """Tests for PATCH /students/{pk}/"""
    def test_patch_slack_handle_persists_to_database(self):
        user = User.objects.create_user(
            username='teststudent',
            password='testpass123'
        )
        nss_user = NssUser.objects.create(
            user=self.user,
            slack_handle='@old_handle',
            github_handle='old_github'
        )
        token = Token.objects.create(user=user)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        """PUT slack_handle should save the new value to the database."""
        response = client.put(
            f"/students/{nss_user.id}",
            {"slack_handle": "@newhandle"},
            format="json"
        )
        #  put your test code here
        # delete this line when you are done
        fail("Not Implemented yet")