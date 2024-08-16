from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.db.models import Count, Min, Max, Avg
from .models import *
from .forms import *
from .filters import *
# Create your views here.
# basics


def indexPage(request):
    return redirect(dashboardPage)

@login_required(login_url='loginPage')
def dashboardPage(request):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    ## -------------------- ##

    featured = Product.objects.filter(isFeatured=True).annotate(reviewCount=Count('review__rating'))
    newest = Product.objects.order_by('-id')[:4].annotate(reviewCount=Count('review__rating'))
    bestselling = Product.objects.order_by('-rating')[:4].annotate(reviewCount=Count('review__rating'))
    context={"user":user, 'featured': featured, 'newest': newest, 'bestselling': bestselling,'profile':pr}

    return render(request, 'catalog/dashboard.html',context)

@login_required(login_url='loginPage')
def productsPage(request):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)

    products = Product.objects.annotate(reviewCount=Count('review__rating'))

    filter = ProductFilter(request.GET, queryset=products)
    products = filter.qs

    misc = products
    context = {'products': products, 'misc' : misc, 'filter': filter}

    return render(request, 'catalog/products.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboardPage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboardPage')

        context = {}
    return render(request, 'catalog/login.html')

def logOutPage(request):
    logout(request)
    return redirect('loginPage')

def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(False)
            user.user_type = 4
            user.save()
            username = form.cleaned_data.get('username')
            Reviewer.objects.create(
                user=user,
                name=user.username,
                )

            messages.success(request, 'Account was created for ' + username)

            return redirect('loginPage')

    context = {'form': form,}
    return render(request, 'catalog/register.html',context)

@login_required(login_url='loginPage')
def registerManagerPage(request):
    ## for navbar profile pic ## 
    us = request.user
    ut = us.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=us)
    elif ut == 1:
        pr= ProductManager.objects.get(user=us)
    ## -------------------- ##

    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(False)
            user.user_type = 1
            user.save()
            username = form.cleaned_data.get('username')
            ProductManager.objects.create(
                user=user,
                )
            
            messages.success(request, 'Account was created for ' + username)

    context = {'form': form,'profile':pr}
    return render(request, 'catalog/register-manager.html',context)

@login_required(login_url='loginPage')
def changePasswordPage(request):
    return render(request, 'catalog/change-pass.html')


@login_required(login_url='loginPage')
def changePasswordSuccessPage(request):
    return render(request, 'catalog/change-pass-success.html')

# general manager pages
@login_required(login_url='loginPage')
def managePage(request):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    ## -------------------- ##
    context = {'profile':pr}
    return render(request, 'catalog/manage.html',context)

# suppliers
@login_required(login_url='loginPage')
def suppliersPage(request):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    ## -------------------- ##

    suppliers = Supplier.objects.all()

    context = {'suppliers': suppliers,'profile':pr}
    return render(request, 'catalog/suppliers.html', context)

@login_required(login_url='loginPage')
def supplierAddPage(request):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    ## -------------------- ##

    form = SupplierForm(request.POST, request.FILES)

    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid:
            form.save()

            return redirect("productsPage")

    context = {'form': form,'profile':pr}
    return render(request, 'catalog/supplier-add.html', context)

@login_required(login_url='loginPage')   
def supplierProductsPage(request, id):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    ## -------------------- ##

    supplier = Supplier.objects.get(id=id)
    products = SupplierProduct.objects.filter(supplier__id=supplier.id)
    p = list(products)

    context = {'supplier': supplier, 'products': p,'profile':pr}
    return render(request, 'catalog/supplierProducts.html', context)

@login_required(login_url='loginPage')
def supplierProductsAddPage(request, id):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    ## -------------------- ##

    supplier = Supplier.objects.get(id=id)
    form = SupplierProductForm()

    if request.method == "POST":
        form = SupplierProductForm(request.POST)
        if form.is_valid():
            instance = form.save(False)
            instance.supplier = supplier
            instance.save()

            return redirect("supplierProductsPage", id=supplier.id)

    context = {'form': form, 'supplier':supplier,'profile':pr}
    return render(request, 'catalog/supplierProducts-add.html', context)

@login_required(login_url='loginPage')
def supplierProductsEditPage(request, id, pd):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    ## -------------------- ##

    supplier = Supplier.objects.get(id=id)
    product = SupplierProduct.objects.get(id=pd)
    form = SupplierProductForm(instance=product)

    if request.method == "POST":
        form = SupplierProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()

            return redirect("supplierProductsPage", id=supplier.id)

    context = {'form': form, 'supplier': supplier, 'product':product,'profile':pr}
    return render(request, 'catalog/supplierProducts-edit.html', context)

@login_required(login_url='loginPage')
def supplierEditPage(request, id):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    ## -------------------- ##

    supplier = Supplier.objects.get(id=id)
    form = SupplierForm(request.POST,request.FILES, instance=supplier)

    if request.method == "POST":
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()

            return redirect("suppliersPage")

    context = {'form': form, 'supplier': supplier,'profile':pr}
    return render(request, 'catalog/supplier-edit.html', context)

# products
@login_required(login_url='loginPage')
def productReviewsPage(request, id):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    ## -------------------- ##

    if user.user_type == 4:
        reviewer = Reviewer.objects.get(user=user)
    product = Product.objects.get(id=id)
    review = Review.objects.filter(product=product)
    supplierProducts = SupplierProduct.objects.filter(product=product)

    UpdateRating(product)
    productStars = GetStars(product.rating)

    reviewArray = []
    for i in range(len(review)):
        x = review[i]
        reviewArray.append((x,GetStars(x.rating)))

    misc = {
        'reviewCount' : len(review)
    }

    context = {'product': product, 'supplierProducts':supplierProducts, 'reviewArray' : reviewArray, 'productStars' : productStars, 'misc' : misc, 'profile':pr}
    # context = {'product': product, 'reviews':review, 'reviewer':reviewer}
    return render(request, 'catalog/productsample.html', context)

@login_required(login_url='loginPage')
def productsAddPage(request):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    ## -------------------- ##

    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("productsPage")

    context = {'form': form,'profile':pr}
    return render(request, 'catalog/products-add.html', context)

@login_required(login_url='loginPage')
def productsEditPage(request, id):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    ## -------------------- ##

    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            
            return redirect("productReviewsPage", id=product.id)

    context = {'form': form, 'product': product,'profile':pr}
    return render(request, 'catalog/products-edit.html', context)

@login_required(login_url='loginPage')
def productsMediaPage(request, id):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    ## -------------------- ##

    product = Product.objects.get(id=id)
    product_media = ProductPhotos.objects.filter(product__id=product.id)
    pm = list(product_media)

    form = ProductPhotoForm()
    if request.method == "POST":
        form = ProductPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.product = product
            instance.save()

            return redirect('productsMediaPage', id = product.id)

    context = {'product': product, 'pm': pm, 'form': form,'profile':pr}
    return render(request, 'catalog/products-media.html', context)

# reviews
@login_required(login_url='loginPage')
def reviewsAddPage(request,id):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    ## -------------------- ##

    product = Product.objects.get(id=id)
    reviewer = Reviewer.objects.get(user=request.user)
    if request.method == "POST":
        review = ReviewForm(request.POST)
        if review.is_valid():
            rev = review.save(False)
            rev.product=product
            rev.reviewer=reviewer
            rev.save()
            UpdateRating(product)
            return redirect("productReviewsPage", id=product.id)
    else:
        review = ReviewForm()
    context={'review':review,'product':product,'profile':pr}
    return render(request, 'catalog/reviews-add.html',context)

@login_required(login_url='loginPage')
def reviewsEditPage(request,id):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    ## -------------------- ##

    rev = Review.objects.get(id=id)
    # product = rev.product
    if request.method == "POST":
        review = ReviewForm(request.POST, instance=rev)
        if review.is_valid():
            review.save()
            UpdateRating(product)

            return redirect("myReviewsPage")
    else:
        review = ReviewForm(instance=rev)
    context={'review':review,'profile':pr}
    return render(request, 'catalog/reviews-edit.html',context)

# categories
@login_required(login_url='loginPage')
def categoriesPage(request):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    ## -------------------- ##

    categories = Category.objects.all()

    context = {'categories': categories,'profile':pr}
    return render(request, 'catalog/categories.html', context)

@login_required(login_url='loginPage')
def categoriesEditPage(request, id):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    ## -------------------- ##
    
    category = Category.objects.get(id=id)
    form = CategoryForm(instance=category)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()

            return redirect("categoriesPage")

    context = {'form': form, 'category': category,'profile':pr}
    return render(request, 'catalog/categories-edit.html', context)

@login_required(login_url='loginPage')
def categoriesAddPage(request):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    ## -------------------- ##
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('categoriesPage')

    context = {'form': form,'profile':pr}
    return render(request, 'catalog/categories-add.html', context)

# account
@login_required(login_url='loginPage')
def profilePage(request):
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    context={'user':user,'profile':pr}
    return render(request, 'catalog/profile.html',context)

@login_required(login_url='loginPage')
def profileEditPage(request):
    user = request.user
    ut = user.user_type
    
    if request.method == "POST":
        uform = EditUserForm(request.POST, instance=user)
        if ut == 4:
            pr= Reviewer.objects.get(user=user)
            pform = EditReviewerForm(request.POST, request.FILES,instance=pr)
            if uform.is_valid() and pform.is_valid():
                pform.save()
                uform.save()
                return redirect('profilePage')
        elif ut == 1:
            pr= ProductManager.objects.get(user=user)
            pform = EditProdManForm(request.POST, request.FILES,instance=pr)
            if uform.is_valid() and pform.is_valid():
                pform.save()
                uform.save()
       
    else:
        uform = EditUserForm(instance=user)
        if ut == 4:
            pr= Reviewer.objects.get(user=user)
            pform = EditReviewerForm(instance=pr)
        elif ut == 1:
            pr= ProductManager.objects.get(user=user)
            pform = EditProdManForm(instance=pr)
    context={'user':user,'uform':uform,'pform':pform,'profile':pr}
    return render(request, 'catalog/profile-edit.html',context)

@login_required(login_url='loginPage')
def profileChangePassPage(request):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    ## -------------------- ##

    pw = PasswordChangeForm(request.user)
    if request.method == "POST":
        pw = PasswordChangeForm(data=request.POST, user=request.user )
        if pw.is_valid():
            pw.save()
            update_session_auth_hash(request, pw.user)
           
        return redirect('profilePage')
    context = {"pw":pw,'profile':pr}
    return render(request, 'catalog/profile-changepass.html',context)

@login_required(login_url='loginPage')
def myReviewsPage(request):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    ## -------------------- ##

    reviewer = Reviewer.objects.get(user=user)
    review = Review.objects.filter(reviewer=reviewer)
    context={'reviews':review,'profile':pr}
    return render(request, 'catalog/myreviews.html',context)

  
  
# misc functions
def GetStars(rating):
    wholeNo = int(rating)
    decimals = rating % 1
    stars = [[],[],[]]
    starCount = 0

    # whole no
    for i in range(wholeNo):
        starCount += 1
        stars[0].append("*")

    # half stars
    if decimals >= .75:
        stars[0].append("*")
        starCount += 1
    elif decimals <= .25:
        pass
    else:
        stars[1].append("o")
        starCount += 1

    # empty stars
    for i in range(5 - starCount):
        stars[2].append("x")

    return stars

def UpdateRating(product):
    reviews = Review.objects.filter(product=product)
    sumRatings = 0
      
    for review in reviews:
        sumRatings += review.rating

    if len(reviews) != 0:
        product.rating = round(sumRatings / len(reviews),1)
    else:
        product.rating = 0
    product.save()

def archiveSupplier(request, id):
    supplier = Supplier.objects.get(id=id)
    supplier.isarchived = True
    supplier.save() 

    return redirect("suppliersPage")

def archiveSupplierProduct(request, id, pd):
    supplier = Supplier.objects.get(id=id)
    product = SupplierProduct.objects.get(id=pd)
    product.isarchived = True
    product.save()

    return redirect("supplierProductsPage", id=supplier.id)

def archiveProduct(request, id):
    product = Product.objects.get(id=id)
    product.isarchived = True
    product.save()

    return redirect("productsPage")

def searchProduct(request):
    ## for navbar profile pic ## 
    user = request.user
    ut = user.user_type
    if ut == 4:
        pr= Reviewer.objects.get(user=user)
    elif ut == 1:
        pr= ProductManager.objects.get(user=user)
    ## -------------------- ##

    if request.method == "POST":
        searched = request.POST['searched']
        product= Product.objects.filter(name__contains=searched)
    context={'search':searched,'prod':product,'profile':pr}
    return render(request, 'catalog/search.html',context)
