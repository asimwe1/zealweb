#Patrick prophet001
#Jado tuyishime001

from django.db import models

# Create your models here.
class Document(models.Model):
	id=models.AutoField(primary_key=True)
	#title=models.CharField(max_length=15)
	TYPE_MEDIA=(('B',"BOOKS"),('N',"MEDIA"),)
	description = models.CharField(max_length=255,blank=True)
	document = models.FileField(upload_to='documents/')
	uploaded_at=models.DateTimeField(auto_now_add=True)
	typedoc=models.CharField(max_length=1,choices=TYPE_MEDIA)

	def __str__(self):
		return self.description
	def get_docs(self):
		return (self.id,self,description, self.TYPE_MEDIA,self.typedoc,self,uploaded_at)
	def get_books(self):
		if(self.typedoc=='B'):
			return(self.id,self.description,self.uploaded_at)
		else:
			return
	def get_media(self):
		if(self.typedoc=='N'):
			return(self.id,self.description,self.uploaded_at)
		else:
			return
	def open_book(self):
		return(self.document)