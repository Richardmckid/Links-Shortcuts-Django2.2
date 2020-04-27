from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# lets create our index view first 
@login_required
def index(request):
    return render(request, 'links_app/index.html')