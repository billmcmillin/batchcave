from django.shortcuts import redirect, render
from converter.models import Conversion
from converter.modelsdir import batchEdits
from converter.forms import ConversionForm
import datetime

# Create your views here.
def home_page(request):
    return render(request, 'converter/home.html')

def index(request):
    return HttpResponse("you're looking at the index of conversion.")

def create(request):

    if request.method == 'POST':
        form = ConversionForm(request.POST, request.FILES)
        if form.is_valid():
            form.TimeExecuted = datetime.datetime.now()
            form.save()
            return redirect('home')
    else:
        form = ConversionForm()
        return render(request, 'conversions/create.html', {
        'form': form
    })

def detail(request, conversion_id):
    return HttpResponse("you're looking at the details of conversion %s." % conversion_id)

def results(request, conversion_id):
    return HttpResponse("you're looking at the results of conversion %s." % conversion_id)
