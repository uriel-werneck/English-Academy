from django.shortcuts import render
from .models import SchoolClass


# Create your views here.
def classes(request):
    if request.method == "POST":
        pass
    all_classes = SchoolClass.objects.all()
    context = {'classes': all_classes}
    return render(request, 'classes/classes.html', context=context)

def class_by_id(request, pk):
    if request.method == "POST":
        pass
    filtered_class = SchoolClass.objects.get(id=pk)
    context = {'class': filtered_class}
    return render(request, 'classes/class_by_id.html', context=context)