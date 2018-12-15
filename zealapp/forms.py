from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = ('description','typedoc','document')

class UploadFileForm(forms.ModelForm):
	class Meta:
		model = Document
		fields=('description','typedoc','document')