from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from timetable.forms import TodoForm
from timetable.models import Todo


# Create your views here.
def index(request):
    todos = Todo.objects.order_by('day').all()
   
    return render(request, 'timetable/index.html', {'todos': todos})


def details(request, id):
    todos = Todo.objects.get(id=id)
    return render(request, 'timetable/details.html', {'todos': todos})



def add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm

    return render(request, 'timetable/add.html', {'form': form})



def update(request, id):
    todos = Todo.objects.get(id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST or None, instance=todos)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm(instance=todos)

    return render(request, 'timetable/add.html', {'form': form, 'todos': todos})


# step 1
# def delete(request, id):
#     todos = Todo.objects.get(id=id)
#     todos.delete()
#     return redirect('index')

# step 2

def delete(request, id):
    todos = Todo.objects.get(id=id)
    if request.method == 'POST':
        todos.delete()
        return redirect('index')
    return render(request, 'timetable/delete.html', {'todos': todos})



#search functionality
def search(request):
    if request.method == "POST":
        search = request.POST.get('output')
        todos = Todo.objects.all()  # Initial queryset containing all records
        
        if search:
            todos = todos.filter(Q(title__icontains=search) |
                                     Q(description__icontains=search) |
                                     Q(favorite__icontains=search) |
                                     Q(day__icontains=search) |
                                     Q(month__icontains=search)|
                                     Q(completed__icontains=search)|
                                     Q(id__icontains=search))
        
        if not todos.exists():
            return HttpResponse("No results found matching the search criteria.")
        
        return render(request, "timetable/index.html", {"todos": todos})
    else:
        return HttpResponse("An error occurred")
