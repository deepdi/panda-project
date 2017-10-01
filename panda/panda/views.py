from django.http import HttpResponse
from panda import models as m
from django.template import Context, loader 
 
def index(request):
    allPandas = m.Identity.objects.all()
    template = loader.get_template('index.html')

    context = {
        'panda_list': allPandas
    }

    return HttpResponse(template.render(context))
  
def naman(request):
    template = loader.get_template('naman.html')
    return HttpResponse(template.render())
