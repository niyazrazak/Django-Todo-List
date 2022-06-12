from django.shortcuts import redirect, render
from .models import Todo


# Create your views here.

def index(request):
    todo = Todo.objects.all()
    if request.method == 'POST':
        new_todo = Todo(
            title=request.POST['title']
        )
        new_todo.save()
        return redirect('/')
    context = {'todo': todo}
    return render(request, 'index.html', context)

def delete(request, pk):
	todo = Todo.objects.get(id=pk)
	todo.delete()
	return redirect('/')
