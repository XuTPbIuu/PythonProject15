from django.shortcuts import render, redirect
from .models import Doc
from .forms import DocForm  # мы её создадим чуть ниже

def index(request):
    docs = Doc.objects.all()
    return render(request, 'core/index.html', {'docs': docs})

def upload_doc(request):
    if request.method == 'POST':
        form = DocForm(request.POST, request.FILES)
        if form.is_valid():
            # создаём, но не сохраняем сразу
            doc = form.save(commit=False)
            # берём загруженный файл
            uploaded = request.FILES['file_path']
            # вычисляем размер в Кб
            doc.size = uploaded.size // 1024
            doc.save()
            return redirect('index')
    else:
        form = DocForm()
    return render(request, 'core/upload.html', {'form': form})
