from django.shortcuts import render
from django.conf import settings
import csv

def inflation_view(request):
    template_name = 'inflation.html'
    with open (settings.RUS_INFL, encoding = 'utf-8') as f:
        f_read = csv.reader(f)
        infl = list(f_read)
        # print(list(f_read))

    # чтение csv-файла и заполнение контекста
    context = {'infl_list':infl}

    return render(request, template_name,
                  context)