from django.template.response import TemplateResponse

# my imports
from .models import Reading


def home(request):
    data = Reading.objects.last()

    template = 'index.html'
    context = {
        'data': data
    }
    return TemplateResponse(request, template, context)