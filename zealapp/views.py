from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

# Create your views here.
def model_form_upload(request):
	form = DocumentForm(request.POST,request.FILES)
	if request.method == 'POST':
		form = DocumentForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			form = DocumentForm()
	return render(request,'model_form_upload.html',{'form':form})
def index(request):
	text="""<h1> Welcome to new Web!</h1>"""
	return HttpResponse(text)
def defix(request):
	return render(request,'upload.html')
def newUpload(request):
	form = UploadFileForm(request.POST or None)
	if request.method=='POST':
		form =UploadFileForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('index')
		else:
			form =UploadFileForm()
	return render(request,'upload.html',{'form':form})
def handle_uploadFileForm(f):
	with open('file/name.txt','wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)