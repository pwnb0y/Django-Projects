from django.shortcuts import render
from .forms import ImageForm
from .models import Image

# Create your views here.
def index_page(request):
    if request == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
         form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'garden/index.html',{'form':form, 'img':img})