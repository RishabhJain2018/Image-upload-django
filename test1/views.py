from django.shortcuts import render
from .models import ImageUpload
from .forms import ImageUploadForm
from django.http import HttpResponse
# Create your views here.
def imageupload(request):
	if request.method=="POST":
		print request.POST
		print request.FILES
		form = ImageUploadForm(request.POST, request.FILES)
		print form
		if form.is_valid():
			form.save()
			return HttpResponse("Image Uploaded !")
		return HttpResponse("Not Uploaded !")
	elif request.method=="GET":
		form = ImageUploadForm()
		return render(request, 'index.html', {'form':form} )
		