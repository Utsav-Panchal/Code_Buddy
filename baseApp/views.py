from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import upload_file_form
from .models import Upload_mutiple_files_model
# Create your views here.

def index(request):
    if request.POST:
        saved_text = request.POST.get('text_Area', None)
        fun(saved_text)
        return render(request, "copypaste.html", {'saved_text': saved_text})
    else:
        with open("file.txt", 'r') as save_file:
            data = save_file.read()
        return render(request, "copypaste.html", {'saved_text': data})


def fun(data):
    with open('file.txt', 'w') as file:
        file.write(data)


def handle_uploaded_file(f):
    with open('file.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_image_view(request):
    queryset = Upload_mutiple_files_model.objects.all()

    if request.POST and request.POST.get('remove') and queryset:
        print("came here", "YEweeeeeeeeeeeeeeeeeehh")
        Upload_mutiple_files_model.objects.all().delete()
        return HttpResponseRedirect('/img')



    if queryset:
        file_count = queryset[0].file
        file_size = round(len(file_count) /1024 / 1024, 3)
        context = {
            'file_data': file_count,
            'file_size': file_size,
        }
        return render(request, 'upload_image.html', context)
    else:
        form = upload_file_form(request.POST or None)

        if request.method == 'POST':
            form = upload_file_form(request.POST, request.FILES)
            if form.is_valid():
                a = form.cleaned_data['file']
                print(a)
                print(len(a), "length")
                form.save()
                print("Success")
                return HttpResponseRedirect("/img")
        return render(request, 'upload_image.html', {'form': form})


def handler404(request, exception):
    context = {}
    return render(request, '404error.html', locals(), context, status=404)


def handler500(request, exception):
    context = {}
    return render(request, '500error.html', locals(), context, status=500)
