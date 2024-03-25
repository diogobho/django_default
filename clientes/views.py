from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import clienteForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cliente_lista(request):
    clientes = Cliente.objects.all()
    return render(request, 'pessoas.html', {'clientes': clientes})

@login_required
def clientes_new(request):
    form = clienteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('clientes_list')
    return render(request, 'cliente_form.html', {'form': form})

@login_required
def clientes_update(request, id):
    cliente = get_object_or_404(Cliente, id=id)  # Corrigido aqui
    form = clienteForm(request.POST or None, request.FILES or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('clientes_list')
    return render(request, 'cliente_form.html', {'form': form})

@login_required
def clientes_delete(request, id):
    cliente = get_object_or_404(Cliente, id=id)  # Corrigido aqui
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes_list')
    return render(request, 'cliente_delete_confirm.html', {'cliente': cliente})