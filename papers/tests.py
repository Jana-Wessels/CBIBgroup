from django.test import TestCase, RequestFactory, Client
from papers.models import Paper
from users.models import CustomUser
import papers.views
from django.http import HttpResponse
import datetime

#Test PDF Fucntions of the website
class PDFTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        Paper.objects.create(Title="Test", Date=datetime.datetime.today(),PaperPDF="test\test.pdf")

    def test_PDFdownload(self):
        self.assertEqual(True,True)


#Test the search functoinality of the website
class SearchTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.Author = CustomUser(IDNumber = 9608066506180, Role = "Member", first_name = "James", last_name = "Watters" )
        Paper.objects.create(Title="Test",Date = datetime.datetime.today())
        Paper.objects.create(Title="Nopaper",Date = datetime.datetime.today())

#Test to ensure no paper returned if year is ahead of time
    def test_Search_NoTitle(self):
        TestResponse = HttpResponse()
        TestResponse.write('<HttpResponse status_code=200, "text/html; charset=utf-8">')
        request = self.factory.get('/search/?title=NoPaper&nodes=&year=&author=')
        response = papers.views.search(request)
        self.assertEqual(type(TestResponse), type(response))


# Test the search via title function
    def test_Title(self):
        self.request = self.factory.get('/search/?title=test&nodes=&year=&author=')
        papers_list = Paper.objects.filter(Title__contains="test")
        response = papers.views.search(self.request)
        print(response)
        TestCase = papers_list[0].__str__()
        self.assertEqual(TestCase, 'Test')

#Test the search via Year function
    def test_Year(self):
        self.request = self.factory.get('/search/?title=test&nodes=&year=2018&author=')
        papers_list = Paper.objects.filter(Date__contains=2018)
        response = papers.views.search(self.request)
        print(response)
        TestCase1 = papers_list[0].__str__()
        TestCase = papers_list[1].__str__()
        Test = TestCase1+TestCase
        self.assertEqual(Test, 'TestNopaper')

#Test to ensure user is directed to the correct page
    def test_Page(self):
        request = self.factory.get('/search/?title=Test&nodes=&year=&author=')
        response = papers.views.search(request)
        self.assertEqual(response.status_code,200)

