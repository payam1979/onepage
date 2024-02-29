from django.shortcuts import render

# Create your views here.
def index_view(request):
     context={'years':'2000 - present', 'title':'Business Intelligence Developer'}
     return render(request, 'index.html', context)

    