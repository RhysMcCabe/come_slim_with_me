from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.db.models import Count, Q
from django.views.generic import ListView



def product_list(request, category_id=None):
    category = None
    products = Product.objects.all()
    ccat = Category.objects.annotate(num_products=Count('products'))
    
    if(category_id):
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)

    return render(request, 'products.html',
                    {'products': products,
                    'countcat':ccat})

class ProductSearchResultsView(ListView):
    model = Product
    context_object_name = 'all_products_list'
    template_name = 'product_search.html'

    def get_queryset(self):
        query = self.request.GET.get('p')
        return Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))



