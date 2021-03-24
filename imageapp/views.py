from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentForm()
        obj = Document.objects.all()
    
    context = {
        'form': form,
        'obj': obj,
    }

    return render(request, 'imageapp/model_form_upload.html', context=context)