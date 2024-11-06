# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Animal
from .forms import AnimalForm

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'adopta_modepran/animal_list.html', {'animals': animals})

# New edit_animal view
def edit_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animal_list')
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'adopta_modepran/animal_edit.html', {'form': form})

