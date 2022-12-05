from django.shortcuts import render
from django.views.generic import ListView

from apps.shops.models import Category


def home(request):
    categorys = Category.objects.all()
    category = categorys.get_descendants(include_self=True)
    # categorys_true = Category.objects.filter(is_active='True')
    # categorys_false = Category.objects.filter(is_active='False')
    context = {
        'categorys': categorys,
        # 'categorys_true': categorys_true,
        # 'categorys_false': categorys_false,
        'category': category,
    }
    return render(request, 'shop/index.html', context)


class CategoryListView(ListView):
    model = Category
