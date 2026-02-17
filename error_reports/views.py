from django.shortcuts import render
from django.http import JsonResponse
from .models import ErrorReport
from .forms import ErrorReportForm

# Create your views here.

def reporte_error(request):
    if request.method == 'GET':
        form = ErrorReportForm()
        return render(request, 'error_reports/reporte_error.html', {'form': form})
    
    elif request.method == 'POST':
        form = ErrorReportForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'ok',
                'mensaje': 'registro exitoso'
            })
        else:
            return JsonResponse({
                'status': 'error',
                'mensaje': 'algo salio mal',
                'errors': form.errors
            })

def obtener_reportes(request):
    reportes = ErrorReport.objects.all().values()
    return JsonResponse(list(reportes), safe=False)
