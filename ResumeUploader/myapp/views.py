from django.shortcuts import render
from .models import Resume
from .forms import ResumeForm

# Create your views here.
def show_page(request):
    form = ResumeForm()
    return render(request, 'myapp/show.html', {'form':form})
