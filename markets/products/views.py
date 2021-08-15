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
        pr = dict()
    print(pr)
    pr = list(map(lambda x: (Product.objects.filter(id=int(x))[0], int(pr[x])), pr.keys()))
    print(pr)
    context = {'products': pr}
    return render(request, 'cart.html', context)


def add_cart(request, product_id):
    print(product_id)
    product_exist = Product.objects.filter(id=product_id)
    print(product_exist)
    if request.method == "POST" and product_exist:
        count = int(request.POST['count'])
        print(count)
        if request.session.get('cart', False):
            print(request.session['cart'].keys(), str(product_id), str(product_id) in request.session['cart'].keys())
            if str(product_id) in request.session['cart'].keys():
                print('!')
                request.session['cart'][str(product_id)] = request.session['cart'][str(product_id)] + count
                print(request.session['cart'][str(product_id)], count)
                print(request.session['cart'])
            else:
                request.session['cart'][str(product_id)] = count
        else:
            request.session['cart'] = {str(product_id): count}
        print(request.session['cart'])
        return JsonResponse({"norm": 'norm'}, status=200)
    else:
        return JsonResponse({"nenorm": 'nenorm'}, status=404)
