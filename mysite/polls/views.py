from django.shortcuts import render, get_object_or_404
from polls.models import Name

# Create your views here.
def index(request):
    latest_name_list = Name.objects.all()
    context = {'latest_name_list':latest_name_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    name = get_object_or_404(Name, pk=question_id)
    return render(request, 'polls/detail.html', {'name':name})

 



    