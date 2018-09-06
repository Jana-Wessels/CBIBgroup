from django.test import TestCase, Client
from users.models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class UserLoginTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create(username = "temp",password="FishNerd12!",Role = "member")

#Tests to ensure a wrong username wont be logged in
    def test_nonmember(self):
        c = Client()
        logged_in = c.login(username="NonUser", password="FishNerd12!")
        self.assertEqual(logged_in, False)

# Tests to ensure a wrong password wont be logged in
    def test_wrongpassword(self):
        c = Client()
        logged_in = c.login(username="temp", password="wrongpassword!")
        self.assertEqual(logged_in, False)

# Tests to ensure a wrong username and password is not logged in
    def test_wrongpall(self):
        c = Client()
        logged_in = c.login(username="NonUser", password="wrongpassword!")
        self.assertEqual(logged_in, False)

# Tests to ensure correct username and password gets logged in
    def test_member_login(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        c = Client()
        logged_in = c.login(username='testuser', password='12345')
        self.assertEqual(logged_in, True)

# Tests Access Level == member
    def test_member(self):
        Role = self.user.Role
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.assertEqual(Role, "member")

class TestCaseNodeAdmin(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create(username = "temp",password="FishNerd12!",Role = "Node Admin")

#Tests Access Level for Admin Node
    def test_member(self):
        Role = self.user.Role
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.assertEqual(Role, "Node Admin")


class TestCaseGlobalAdmin(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create(username="temp", password="FishNerd12!", Role="Global Admin")

    # Tests Access Level for Admin Node
    def test_member(self):
        Role = self.user.Role
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.assertEqual(Role, "Global Admin")

class TestCaseAuthor(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create(username="temp", password="FishNerd12!", Role="Author")

    # Tests Access Level for Admin Node
    def test_member(self):
        Role = self.user.Role
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.assertEqual(Role, "Author")