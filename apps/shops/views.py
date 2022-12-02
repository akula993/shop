from django.shortcuts import render
from django.views.generic import ListView

from apps.shops.models import Category


def home(request):
    categorys = Category.objects.all()
    cl = Category.objects.filter(top='True')
    context = {
        'categorys': categorys,
        'cl': cl,
    }
    return render(request, 'shop/index.html', context)


class CategoryListView(ListView):
    model = Category
