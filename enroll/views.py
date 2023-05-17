from itertools import product
from sre_parse import State
# from xml.etree.ElementTree import QName
# from django import views
from django.shortcuts import redirect, render
from .models import Customer, Product, orderplaced, cart, Reviews
from django.views import View
from .forms import registrationforms, Adressform, Reviewsform
from django.contrib import messages
from django.db.models import Q

from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


class homeview(View):
    def get(self, request):
        sofa = Product.objects.filter(Category='so')
        electronic = Product.objects.filter(Category='ele')
        T_shirt = Product.objects.filter(Category='Ts')
        Baby = Product.objects.filter(Category='by')
        Bags = Product.objects.filter(Category='bg')
        footwear = Product.objects.filter(Category='ft')
        jwellery = Product.objects.filter(Category='jw')
        Belt = Product.objects.filter(Category='be')
        Gift = Product.objects.filter(Category='gif')
        return render(request, 'enroll/home.html', {'sofa': sofa, 'electronic': electronic, 'T_shirt': T_shirt, 'baby': Baby, 'Bags': Bags, 'footwear': footwear, 'jwellery': jwellery, 'Belt': Belt, 'Gift': Gift})


class productdetailsview(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False

        if request.user.is_authenticated:
            item_already_in_cart = cart.objects.filter(
                Q(product=product.id) & Q(user=request.user)).exists()

        form = Reviewsform()
        user = request.user
        # Reviewform = Reviews.objects.get(Rat=pk)
        Review = Reviews.objects.filter(Rat=pk)
        # pd=Product.objects.
        # id=Reviews.objects.get(pk=pk)
        # print(id)
        # Review=Reviews.objects.get(pk=pk)
        return render(request, 'enroll/productdetails.html', {'product': product, 'item_already_in_cart': item_already_in_cart, 'form': form, 'Review': Review, 'active': 'btn-primary'})

    def post(self, request, pk):
        form = Reviewsform(request.POST)
        if form.is_valid():
            user = request.user
            # id=form.cleaned_data['ID']
            name = form.cleaned_data['Name']
            rating = form.cleaned_data['Rating']
            Desc = form.cleaned_data['Description']
            Cat = form.cleaned_data['Category']
            print(pk)
            reg = Reviews(Rat=pk, user=user, Name=name,
                          Rating=rating, Description=Desc, Category=Cat)
            reg.save()
        return render(request, 'enroll/productdetails.html', {'form': form, 'active': 'btn-primary'})


class electronicview(View):
    def get(self, request, data=None):
        if data == None:
            electronic = Product.objects.filter(Category='ele')
        elif data == 'below':
            electronic = Product.objects.filter(
                Category='ele').filter(Selling_price__lte=30000)
        elif data == 'above':
            electronic = Product.objects.filter(
                Category='ele').filter(Selling_price__gte=30000)
        return render(request, 'enroll/electronic.html', {'electronic': electronic})


class registrationformsview(View):
    def get(self, request):
        form = registrationforms()
        return render(request, 'enroll/register.html', {'form': form})

    def post(self, request):
        form = registrationforms(request.POST)
        if form.is_valid():
            messages.success(request, 'Registration Successfully')
            form.save()
        return render(request, 'enroll/register.html', {'form': form})


def profile(request):
    if request.method == "POST":
        form = Adressform(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['Name']
            city = form.cleaned_data['City']
            pincode = form.cleaned_data['Pin_code']
            State = form.cleaned_data['State']
            reg = Customer(user=user, Name=name, City=city,
                           Pin_code=pincode, State=State)
            reg.save()
    else:
        form = Adressform()
    return render(request, 'enroll/profile.html', {'form': form, 'active': 'btn-primary'})


def Adress(request):
    user = request.user
    customer = Customer.objects.filter(user=user)
    return render(request, 'enroll/Adress.html', {'customer': customer, 'active': 'btn-primary'})


def addtocart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    cart(user=user, product=product).save()
    return redirect('/cart1')


def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        carts = cart.objects.filter(user=user)
        amount = 0.0
        ship = 30.0
        totalamount = 0.0
        pamount = 0
        cart_product = [p for p in cart.objects.all() if p.user == user]
        if carts:
            for p in cart_product:
                pamount = (p.quentity * p.product.Discount_price)
                amount = amount+pamount
            totalamount = amount+ship
            return render(request, 'enroll/Addcart.html', {'cart': carts, 'totalamount': totalamount, 'amount': amount})
        else:
            return render(request, 'enroll/empty.html')


def empty(request):
    return render(request, 'enroll/empty.html')


def placeorder(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_item = cart.objects.filter(user=user)
    return render(request, 'enroll/placeorder.html', {'add': add, 'cart_item': cart_item})


def payment(request):
    user = request.user
    custid = request.GET.get("custid")
    customer = Customer.objects.get(id=custid)
    Cart = cart.objects.filter(user=user)
    for c in Cart:
        orderplaced(user=user, customer=customer,
                    product=c.product, quentity=c.quentity).save()
        c.delete()
    return redirect("order")


def login_cart(request):
    return render(request, 'enroll/login_cart.html')


def order_details(request):
    user = request.user
    order = orderplaced.objects.filter(user=user)
    return render(request, 'enroll/orders_details.html', {'order': order})

# def Review(request):
#     if request.method == "POST":
#         form = Reviewsform(request.POST)
#         if form.is_valid():
#             user = request.user
#             name = form.cleaned_data['Name']
#             rating = form.cleaned_data['Rating']
#             Desc = form.cleaned_data['Desc']
#             reg = Reviews(user=user, Name=name,Rating=rating, Description=Desc)
#             reg.save()
#     else:
#         form = Reviewsform()
#     return render(request, 'enroll/Review.html', {'form': form, 'active': 'btn-primary'})


def Recommendation(request):

    user = request.user

# Rating add in product
    rev1=Reviews.objects.all()
    d1={}
    for i in rev1:
        if i.Rat not in d1:
            d1[i.Rat]=[i.Rating]
        else:
            rem=d1[i.Rat]
            rem.append(i.Rating)
            d1[i.Rat]+=rem
    
    d2={}
    for key,val in d1.items():
        d2[key]=sum(val)//len(val) 
    
    print(d2)

    

    @property
    def get_queryset(self):
        for key,val in d2.items():
            pd=Product.objects.filter(id=key)
            pd=pd(rating=val)
            pd.save()
    # get_queryse()

    # r=Product(rating=)

    


# for recommendation sysytem
    pd=Product.objects.all()

    rev=Reviews.objects.filter(user=user)
    
    rev=rev.filter(Rating__gte=0)

    arr=[]
    d={}

    for i in rev:
        if i.Rat not in arr:
            arr.append(i.Rat)
            if i.Category not in d:
                d[i.Category]=[i.Rating]
            else:
                rem=d[i.Category]
                rem.append(i.Rating)
                d[i.Category]+=[]
    # print(d)
    d1={}
    for val,num in d.items():
        if len(num)>=3:
            d1[val]=sum(num)//len(num)
    # print(d1)

    cat=[]
    for val,num in d1.items():
        if num>=3:
            cat.append(val)
    
    
    arr=[]
    cjw=0
    cso=0
    cft=0
    cmb=0
    cele=0
    cts=0
    cby=0
    cbg=0
    cbe=0
    cgif=0


    for i in pd:
        if i.Category in cat:
            if i.Category=='jw' and cjw<6:
                cjw+=1
                arr.append(i)
            if i.Category =='cft' and cft<6:
                cft+=1
                arr.append(i) 
            if i.Category=='be' and cbe<6:
                cbe+=1
                arr.append(i)
            if i.Category =='mb' and cmb<6:
                cmb+=1
                arr.append(i) 
            if i.Category=='ele' and cele<6:
                cele+=1
                arr.append(i)
            if i.Category =='ts' and cts<6:
                cts+=1
                arr.append(i) 
            if i.Category=='by' and cby<6:
                cby+=1
                arr.append(i)
            if i.Category =='bg' and cbg<6:
                cso+=1
                arr.append(i) 
            if i.Category =='gif' and cgif<6:
                cgif+=1
                arr.append(i) 
    # arr=[]
    
    
    return render(request,"enroll/Recommendation.html",{'arr':arr})


# def contact(request):
#     return render(request,"enroll/Contact.html")

def about(request):
    return render(request,"enroll/About.html")

class jwelleryView(View):
    def get(self, request, data=None):
        if data == None:
            electronic = Product.objects.filter(Category='ele')
        elif data == 'below':
            electronic = Product.objects.filter(
                Category='ele').filter(Selling_price__lte=30000)
        elif data == 'above':
            electronic = Product.objects.filter(
                Category='ele').filter(Selling_price__gte=30000)
        return render(request, 'enroll/jwellery.html', {'electronic': electronic})


# def jwellery(request):
#     return render(request,"enroll/jwellery.html")

class BeltView(View):
    def get(self, request, data=None):
        if data == None:
            electronic = Product.objects.filter(Category='ele')
        elif data == 'below':
            electronic = Product.objects.filter(
                Category='ele').filter(Selling_price__lte=30000)
        elif data == 'above':
            electronic = Product.objects.filter(
                Category='ele').filter(Selling_price__gte=30000)
        return render(request, 'enroll/Belt.html', {'electronic': electronic})
    

class BabyclothesView(View):
    def get(self, request, data=None):
        if data == None:
            electronic = Product.objects.filter(Category='by')
        elif data == 'below':
            electronic = Product.objects.filter(
                Category='by').filter(Selling_price__lte=30000)
        elif data == 'above':
            electronic = Product.objects.filter(
                Category='by').filter(Selling_price__gte=30000)
        return render(request, 'enroll/Babyclothes.html', {'electronic': electronic})
    

# class ShoesView(View):
#     def get(self, request, data=None):
#         if data == None:
#             electronic = Product.objects.filter(Category='ele')
#         elif data == 'below':
#             electronic = Product.objects.filter(
#                 Category='ele').filter(Selling_price__lte=30000)
#         elif data == 'above':
#             electronic = Product.objects.filter(
#                 Category='ele').filter(Selling_price__gte=30000)
#         return render(request, 'enroll/Shoes.html', {'electronic': electronic})
    

class ComfortsofaView(View):
    def get(self, request, data=None):
        if data == None:
            electronic = Product.objects.filter(Category='so')
        elif data == 'below':
            electronic = Product.objects.filter(
                Category='so').filter(Selling_price__lte=30000)
        elif data == 'above':
            electronic = Product.objects.filter(
                Category='so').filter(Selling_price__gte=30000)
        return render(request, 'enroll/Comfortsofa.html', {'electronic': electronic})


class HandbagsView(View):
    def get(self, request, data=None):
        if data == None:
            electronic = Product.objects.filter(Category='bg')
        elif data == 'below':
            electronic = Product.objects.filter(
                Category='bg').filter(Selling_price__lte=30000)
        elif data == 'above':
            electronic = Product.objects.filter(
                Category='bg').filter(Selling_price__gte=30000)
        return render(request, 'enroll/Handbags.html', {'electronic': electronic})


class ShoesView(View):
    def get(self, request, data=None):
        if data == None:
            electronic = Product.objects.filter(Category='ft')
        elif data == 'below':
            electronic = Product.objects.filter(
                Category='ft').filter(Selling_price__lte=30000)
        elif data == 'above':
            electronic = Product.objects.filter(
                Category='ft').filter(Selling_price__gte=30000)
        return render(request, 'enroll/Shoes.html', {'electronic': electronic})
# def Belt(request):
#     return render(request,"enroll/Belt.html")



class giftView(View):
    def get(self, request, data=None):
        if data == None:
            Gift = Product.objects.filter(Category='gif')
        elif data == 'below':
            Gift = Product.objects.filter(
                Category='gif').filter(Selling_price__lte=30000)
        elif data == 'above':
            Gift = Product.objects.filter(
                Category='gif').filter(Selling_price__gte=30000)
        return render(request, 'enroll/gift.html', {'Gift': Gift})



def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'amankumarshah8102@gmail.com', ['amankumarshah8102@gmail.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			# return redirect ("enroll/home")
      
	form = ContactForm()
	return render(request, "enroll/contact.html", {'form':form})


def About(request):
    return render(request,'enroll/About.html')