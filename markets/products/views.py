from django.http import JsonResponse
from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, CartProductForm


def index(request):
    request.session.save()
    products = Product.objects.all()
    form = CommentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        pass
    context = {'products': products,
               'form': form}
    print(request.session.keys())
    return render(request, 'index.html', context)


def product(request, product_id):
    request.session.save()
    product = get_object_or_404(Product, id=product_id)
    form = CommentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        pass
    context = {'product': product,
               'form': form,
               'Cform': CartProductForm}
    return render(request, 'product.html', context)


@login_required
def add_comment(request, product_id):
    pass


def cart(request):
    if request.session.get('cart', False):
        pr = request.session['cart']
    else:
        pr = []
    pr = list(map(lambda x: (get_object_or_404(Product, id=x[0]), int(x[1])), pr))
    context = {'products': pr}
    print(pr)
    return render(request, 'cart.html', context)


def add_cart(request, product_id):
    product_exist = Product.objects.filter(id=product_id).exist()
    if request.method == "POST" and product_exist:
        count = request.POST['count']
        if request.session.get('cart', False):
            request.session['cart'] += [(product_id, count)]
        else:
            request.session['cart'] = [(product_id, count)]
        return JsonResponse({"norm": 'norm'}, status=200)
    else:
        return JsonResponse({"norm": 'norm'}, status=400)
