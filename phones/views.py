from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'

    data = Phone.objects.all()
    if request.method == 'POST':
        sort = request.POST.get('sort')
        if sort == "expensive":
            data = Phone.objects.order_by('-price')
        elif sort == "low_cost":
            data = Phone.objects.order_by('price')
        elif sort == "name":
            data = Phone.objects.order_by('name')
    
    context = {
        "phones" : data,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    product = Phone.objects.get(slug=slug)
    context = {
        "data" : product
    }
    return render(request, template, context)
