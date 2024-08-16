from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(AuthUser)
admin.site.register(ProductManager)
admin.site.register(Product)
admin.site.register(ProductCatalog)
admin.site.register(ProductPhotos)
admin.site.register(ProductVideos)
admin.site.register(Catalog)
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(SupplierProduct)
admin.site.register(Reviewer)
admin.site.register(Review)