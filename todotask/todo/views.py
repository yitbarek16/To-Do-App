from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    tasks=Task.objects.all()
    return render(request,"index.html",{'tasks':tasks})
    pass
@login_required
def add_task(request):
    if request.method=='POST':
        title= request.POST['title']
        description=request.POST['description']
        Task.objects.create(title=title,description=description)
        return redirect('index')
    return render(request,'add_task.html')
    pass
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'delete_task.html', {'task': task})
    pass

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
