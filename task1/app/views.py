from django.shortcuts import render
from django.conf import settings
import csv

def inflation_view(request):
    template_name = 'inflation.html'
    with open (settings.RUS_INFL, encoding = 'utf-8') as f:
        f_read = csv.reader(f,delimiter = ';')
        infl = list(f_read)

    # чтение csv-файла и заполнение контекста
    context = {'infl_list':infl, 'empty': '-'}

    return render(request, template_name,
                  context)