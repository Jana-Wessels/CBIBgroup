from django.db import models
from django.contrib.auth import get_user_model


# Paper implementation containing all the paper fields
class Paper(models.Model):
    Title = models.CharField(max_length=100)
    # Author is a foreign key so field has to be filled by a author object.
    Author = models.ManyToManyField(get_user_model())
    PublicationType = models.TextField(default=' ', max_length=50, verbose_name="Publication")
    Publisher = models.TextField(default=' ', max_length=50)
    NumOfPages = models.TextField(default=' ', max_length=50, verbose_name="Pages")
    Date = models.DateTimeField('date published')
    Abstract = models.TextField(default=' ', max_length=2000)
    BibTex = models.TextField(default=' ', max_length=500)
    PaperPDF = models.FileField(default=' ', upload_to='media/', verbose_name="Research Paper")
    PeerPDF = models.FileField(default=' ', upload_to='media/', verbose_name="Peer Review")

    # string function that returns the paper title when this class is printed.
    def __str__(self):
        return self.Title

    def get_Report(self, filters):
        #gets info for the report based on the filters.
        return self