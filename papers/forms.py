from django import forms
from .models import Paper

class UploadPaper(forms.ModelForm):

    class Meta:
        model = Paper
        fields = ('title', 'author', 'abstract', 'BibTex', 'PaperPDF', "PeerPDF",)


