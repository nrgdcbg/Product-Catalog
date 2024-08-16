from django import forms
from django.forms import ModelChoiceField, ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = AuthUser
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']


class EditUserForm(UserChangeForm):
    class Meta:
        model = AuthUser
        fields = ['username','first_name','last_name','email','password']
        labels = {
            'email' : 'Email Address'
        }

class EditReviewerForm(ModelForm):
    class Meta:
        model = Reviewer
        fields = ['name','contact', 'profilepicture','address']

        labels = {
            'contact' : 'Contact No.',
            'address' : 'Home Address',
        }
class EditProdManForm(ModelForm):
    class Meta:
        model = ProductManager
        fields = ['profilepicture']

class ProductForm(ModelForm):
    category = ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['name', 'stocks', 'reorderlvl', 'sellingprice', 'discount', 'category', 'description', 'isFeatured']

        labels = {
            'name': 'Product Name',
            'stocks': 'Product Stocks',
            'reorderlvl': 'Reorder Level',
            'sellingprice': 'Selling Price',
            'discount': 'Discount',
            'category': 'Product Category',
            'description': 'Product Description',
            'isFeatured': 'Set as featured'
        }

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'address', 'email', 'telephone', 'contactperson', 'displaypicture']

        labels = {
            'name': 'Supplier Name',
            'address': 'Supplier Address',
            'email': 'Supplier Email',
            'telephone': 'Supplier Telephone No.',
            'contactperson': 'Contact Person'    
        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

        labels = {
            'name': 'Category Name',
            'description': 'Category Description'
        }

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating','details'] 
        labels = {
            'details': 'Review Details',
        }
        
class SupplierProductForm(ModelForm):
    product = ModelChoiceField(queryset=Product.objects.all())

    class Meta:
        model = SupplierProduct
        fields = ['leadtime', 'supplierprice', 'discount', 'product']

        labels = {
            'leadtime': 'Product Lead Time',
            'supplierprice': 'Supplier Price',
            'discount': 'Product Discount',
            'product': 'Product'
        }

class ProductPhotoForm(ModelForm):
    class Meta:
        model = ProductPhotos
        fields = ['photo']