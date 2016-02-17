from django.shortcuts import render
from .forms import CadastroForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.send_mail()
            form = CadastroForm()
    else:
        form = CadastroForm()
    context = {
        'form':form
    }
    return render(request,'index.html',context)
