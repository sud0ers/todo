from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from home.models import ToDo

def home(request):
    context = {'success':False}
    if request.method == "POST":
        # print("This is post")
        title = request.POST['title']
        desc = request.POST['desc']
        # print(title,desc)
        todo = ToDo(title=title, desc=desc)
        todo.save()
        # print("Data added")
        context = {'success':True}

    return render(request,'index.html',context)
    
def tasks(request):
    alltasks = ToDo.objects.all()
    context = {'tasks':alltasks}
    return render(request,'tasks.html',context)