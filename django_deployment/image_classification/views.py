from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .inference.model_inference import classify
from django.conf import settings
from pathlib import Path
from .forms import UploadImageForm
# Create your views here.
# def home_view(request, *args, **kwargs):
#     result = None
#     if request.method == 'POST'and request.FILES['myfile']:
#         uploaded_file = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(uploaded_file.name, uploaded_file)
#         result = classify(settings.MEDIA_ROOT, uploaded_file.name)
      
#     context = {"result": result}
#     return render(request, 'home.html', context)

def home_view(request):
    form  = UploadImageForm(request.POST or None, request.FILES)
    result = None
    if form.is_valid():
        image_field = form.cleaned_data['image']
        form.save()
        result = classify(settings.MEDIA_ROOT, image_field.name)
    context = {
        'form': form,
        'result': result
    }

    return render(request, 'home.html', context)
