from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_GET, require_POST
def homePage(req):
    todo_objs=Todo.objects.order_by('id')
    form=TodoForm()
    context={'todo_list':todo_objs,'form':form}
    return render(req,'Todo/index.html',context)
@require_POST
def add(req):
    form=TodoForm()    
    task=req.POST['text']
    print(task)
    todo=Todo(text=task)
    todo.save()
    return redirect('homePage')

def complete(req,todo_id):
    todoObj=Todo.objects.get(pk=todo_id)
    todoObj.complete=True
    todoObj.save()
    return redirect('homePage')

def delCompleted(req):
    todo_objs=Todo.objects.order_by('id')
    for each in todo_objs:
        if each.complete is True: 
            each.delete()
            pass
        pass
    return redirect('homePage')
def delAll(req):
    todo_objs=Todo.objects.order_by('id')
    for each in todo_objs:
        each.delete()
    return redirect('homePage')
def delSingle(req,todo_id):
    todoObj=Todo.objects.get(pk=todo_id)
    todoObj.delete()
    return redirect('homePage')

    

    