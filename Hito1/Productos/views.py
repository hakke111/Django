from django.shortcuts import render
from Productos.models import Producto

def project_index(request):
    Productos = Producto.objects.all()
    context = {
        'Productos': Productos
    }
    return render(request, 'productos_index.html', context)