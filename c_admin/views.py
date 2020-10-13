from django.shortcuts import render
from django.views import View

from .forms import CategoryForm

from categories.models import MainCategory, Category
from products.models import Product

class IndexView(View):

    def get(self, request, *args, **kwargs):

        return render(request, "c_admin/index.html", {})
        

class NotFound404(View):

    def get(self, request, *args, **kwargs):

        return render(request, "c_admin/404.html", {})

class CreateCategoryView(View):

    def get(self, request, *args, **kwargs):
        form = CategoryForm

        context = { 
            'form' : form,
        }
        return render(request, "c_admin/add-category.html", context)

class AllCategoriesSelectionView(View):

    def get(self, request, *args, **kwargs):
        mains = MainCategory.objects.all()

        return render(request, "c_admin/select_main_cat.html", { 'mains' : mains})

class CategorySelectView(View):

    def get(self, request, id, *args, **kwargs):
        cats = Category.objects.filter(sub_category_of__id=id)

        return render(request, 'c_admin/category_select.html', { 'cats' : cats})


        
class ProductsListView(View):
    
    def get(self, request, id, *args, **kwargs):

        products = Product.objects.filter(category__id=id, confirmed=True)
        all_prods = products.count()
        pending_products = Product.objects.filter(category__id=id, confirmed=False).count()

        context = { 
            'all' : all_prods,
            'items' : products, 
            'pending' : pending_products,
        }

        return render(request, "c_admin/products.html", context)