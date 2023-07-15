from django.shortcuts import render, redirect
from myApp.models import Contact
from django.contrib import messages
from datetime import datetime
from django.views import View
from .forms import CustomerRegistrationForm, ProductForm, CustomerProfileForm
from .models import Customer, Product, Cart, OrderPlaced
from django.db.models import Q
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'address.html', {'add': add, 'active': 'btn-primary'})


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
        return render(request, 'index.html')
    return render(request, 'contact.html')


def BorrowProduct(request):
    img = Product.objects.all()
    return render(request, 'BorrowProduct.html', {'img': img})


def Become_supplier(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ProductForm()
    return render(request, 'Become_supplier.html', {'form': form})


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'signup.html', {'form': form})


def password_reset(request):
    return render(request, 'password_reset.html')


def password_reset_confirm(request):
    return render(request, 'password_reset_confirm.html')


def change_password(request):
    return render(request, 'change_password.html')


def passwordchangedone(request):
    return render(request, 'passwordchangedone.html')


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'product_detail.html', {'product': product})


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'profile.html', {'form': form, 'active': 'btn-primary'})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_no = form.cleaned_data['phone_no']
            another_phone_no = form.cleaned_data['another_phone_no']
            aadhar_card_no = form.cleaned_data['aadhar_card_no']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, email=email, phone_no=phone_no, another_phone_no=another_phone_no,
                           aadhar_card_no=aadhar_card_no, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations!! Profile Updated Successfully')
            return render(request, 'profile.html', {'form': form, 'active': 'btn-primary'})


def search(request):
    query = request.GET['query']
    equip = Product.objects.filter(title__icontains=query)
    params = {'equip': equip}
    return render(request, 'search.html', params)


#
# def add_to_cart(request):
#     user = request.user
#     product_id = request.GET.get('prod_id')
#     product = Product.objects.get(id=product_id)
#     Cart(user=user, product=product).save()
#     return redirect('/cart')


def add_to_cart(request):
    return render(request, 'add_to_cart.html')


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.rent_price)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount': amount
        }
        return JsonResponse(data)


def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        # print(cart)
        amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.rent_price)
                amount += tempamount
            return render(request, 'add_to_cart.html', {'carts': cart, 'amount': amount})
        else:
            return render(request, 'empty_cart.html')


def static_Product_Detail(request):
    return render(request, 'staticProductDetail.html')


def static_Product_Detail1(request):
    return render(request, 'staticProductDetail1.html')
