from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = { 'today':datetime.today() }

# # Create your views here.
# def home (request):
#     return render(request , 'home/welcome.html', {'today': datetime.today()})

@login_required(login_url='/admin')
def authorized(request):
    return render(request , 'home/authorized.html', {})