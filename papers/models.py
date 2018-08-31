from django.db import models
from django.contrib.auth import get_user_model


# Paper implementation containing all the paper fields
class Paper(models.Model):
    title = models.CharField(max_length=50)

    # Author is a foreign key so field has to be filled by a author object.
    author = models.ManyToManyField(get_user_model())

    date = models.DateTimeField('date published')
    abstract = models.TextField(default=' ', max_length=500)
    BibTex = models.TextField(default=' ', max_length=200)
    PaperPDF = models.FileField(default=' ', upload_to='media/')
    PeerPDF = models.FileField(default=' ', upload_to='media/')

    # string function that returns the paper title when this class is printed.
    def __str__(self):
        return self.title

    def get_Report(self, filters):
        #gets info for the report based on the filters.
        return self