from django.shortcuts import render
from wrr import models
# Create your views here.
def movie(request):
    mov_list=models.Movie.objects.all()
    print(mov_list)
    context={
        'mov_list':mov_list
    }
    return render(request,'show.html',context=context)
