from django.shortcuts import redirect, render
from converter.models import Conversion
from converter.modelsdir import batchEdits
from converter.forms import ConversionForm
import datetime
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return render(request, 'converter/home.html')

def index(request):
    try:
        Conversions = Conversion.objects.all()
        return render(request, 'conversions/index.html', {'Conversions': Conversions})
    except:
        return redirect('error')

def create(request):

    if request.method == 'POST':
        form = ConversionForm(request.POST, request.FILES)
        try:
            form.is_valid()
            form.save()
            return redirect('index')
        except:
            return redirect('error')
    else:
        form = ConversionForm()
        return render(request, 'conversions/create.html', {
        'form': form
    })

def error(request):
    return render(request, 'conversions/error.html', {
        'msg': 'There is an error with the submission. All conversions must have a name, a selected type, and a file uploaded.'})

def detail(request, conversion_id):
    return HttpResponse("you're looking at the details of conversion %s." %
conversion_id)

def download(request, conversion_id):
    convo = Conversion.objects.get(pk=conversion_id)
    response = HttpResponse(convo.Output)
    response['content_type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=%s' % convo.Name
    return response

def results(request, conversion_id):
    return HttpResponse("you're looking at the results of conversion %s." %
conversion_id)
