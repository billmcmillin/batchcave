from django.shortcuts import redirect, render
from converter.models import Conversion
from converter.modelsdir import batchEdits
from converter.forms import ConversionForm
import datetime

# Create your views here.
def home_page(request):
    return render(request, 'converter/home.html')

def index(request):
    Conversions = Conversion.objects.all()
    return render(request, 'conversions/index.html', {'Conversions': Conversions})

def create(request):

    if request.method == 'POST':
        form = ConversionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return redirect('conversions/error.html', {
            'msg': 'There is an error with the submission. All conversions must have a name, a selected type, and a file uploaded.'})
    else:
        form = ConversionForm()
        return render(request, 'conversions/create.html', {
        'form': form
    })

def detail(request, conversion_id):
    return HttpResponse("you're looking at the details of conversion %s." % conversion_id)

def results(request, conversion_id):
    return HttpResponse("you're looking at the results of conversion %s." % conversion_id)
