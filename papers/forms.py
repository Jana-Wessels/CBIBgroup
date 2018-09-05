from django import forms
from .models import Paper

class UploadPaper(forms.ModelForm):

    class Meta:
        model = Paper
        fields = ('Title', 'Author', 'PublicationType', 'Publisher', 'NumOfPages', 'Abstract', 'BibTex', 'PaperPDF', "PeerPDF",)


