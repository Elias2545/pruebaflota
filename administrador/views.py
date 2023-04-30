from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.
TEMPLATE_DIRS =(
    'os.path.join(BASE_DIR,"templates"),'
)

# Create your views here.
def index(request):                    #  <<==========
    return render(request,"index.html")      #  <<==========

def listar(request):
    return render(request,"moviles/listar.html")

def crear(request):
    return render(request,"moviles/crear.html")

def editar(request):
    return render(request,"moviles/editar.html")

