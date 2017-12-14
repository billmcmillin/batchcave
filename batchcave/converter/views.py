from django.shortcuts import redirect, render
from converter.models import Conversion
from converter.modelsdir import batchEdits
from converter.forms import ConversionForm
import datetime
from django.core.exceptions import ValidationError

# Create your views here.
def home_page(request):
    return render(request, 'converter/home.html')

def index(request):
    Conversions = Conversion.objects.all()
    return render(request, 'conversions/index.html', {'Conversions': Conversions})

def create(request):

    if request.method == 'POST':
        form = ConversionForm(request.POST, request.FILES)
        try:
            form.is_valid()
            form.save()
            return redirect('index')
        except Exception as e:
            return render(request, 'conversions/create.html', {"error": e})
    else:
        form = ConversionForm()
        return render(request, 'conversions/create.html', {
        'form': form
    })


def detail(request, conversion_id):
    return HttpResponse("you're looking at the details of conversion %s." % conversion_id)

def results(request, conversion_id):
    return HttpResponse("you're looking at the results of conversion %s." % conversion_id)
