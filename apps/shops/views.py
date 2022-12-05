from django.shortcuts import render
from django.views.generic import ListView

from apps.shops.models import Category


def home(request):
    categorys = Category.objects.all()
    category = categorys.get_descendants(include_self=True)
    categorys_true = Category.objects.filter(top='True')
    categorys_false = Category.objects.filter(top='False')
    context = {
        'categorys': categorys,
        'categorys_true': categorys_true,
        'categorys_false': categorys_false,
    }
    return render(request, 'shop/index.html', context)


class CategoryListView(ListView):
    model = Category
