
from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm

def todo_lists(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_lists.html', {'todos': todos})

def todo_object(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todos/todo_object.html', {'todo': todo})

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form})

def todo_edit(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/todo_form.html', {'form': form, 'is_edit': True})

def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    render(request, 'todos/todo_delete.html', {'todo': todo})
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')