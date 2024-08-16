from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.indexPage, name='indexPage'),
    path('dashboard/', views.dashboardPage, name='dashboardPage'),
    path('login', views.loginPage, name='loginPage'),
    path('logout/', views.logOutPage, name="logout"),
    path('register/', views.registerPage, name='registerPage'),
    path('register/manager/', views.registerManagerPage, name='registerManagerPage'),
    path('change-password', views.changePasswordPage, name='changePasswordPage'),
    path('change-password/success', views.changePasswordSuccessPage, name='changePasswordSuccessPage'),

    path('manage/', views.managePage, name='managePage'),
    path('suppliers/', views.suppliersPage, name='suppliersPage'),
    path('suppliers/add', views.supplierAddPage, name='supplierAddPage'),
    path('suppliers/<int:id>/archive', views.archiveSupplier, name='archiveSupplier'),
    path('suppliers/<int:id>/edit', views.supplierEditPage, name='supplierEditPage'),
    path('suppliers/<int:id>/products', views.supplierProductsPage, name='supplierProductsPage'),
    path('suppliers/<int:id>/products/add', views.supplierProductsAddPage, name='supplierProductsAddPage'),
    path('suppliers/<int:id>/products/<int:pd>/archive', views.archiveSupplierProduct, name='archiveSupplierProduct'),
    path('suppliers/<int:id>/products/<int:pd>/edit', views.supplierProductsEditPage, name='supplierProductsEditPage'),

    path('products/', views.productsPage, name='productsPage'),
    path('products/add', views.productsAddPage, name='productsAddPage'),
    path('products/<int:id>', views.productReviewsPage, name='productReviewsPage'),
    path('products/<int:id>/edit', views.productsEditPage, name='productsEditPage'),
    path('products/<int:id>/archive', views.archiveProduct, name='archiveProduct'),
    path('products/<int:id>/media', views.productsMediaPage, name='productsMediaPage'),

    path('products/<int:id>/addreview/', views.reviewsAddPage, name='reviewsAddPage'),
    path('products/search-results/', views.searchProduct, name='searchProduct'),
    

    path('categories/', views.categoriesPage, name='categoriesPage'),
    path('categories/add', views.categoriesAddPage, name='categoriesAddPage'),
    path('categories/<int:id>/edit', views.categoriesEditPage, name='categoriesEditPage'),

    path('profile/', views.profilePage, name='profilePage'),
    path('profile/edit', views.profileEditPage, name='profileEditPage'),
    path('profile/change-password', views.profileChangePassPage, name='profileChangePassPage'),
    path('myreviews', views.myReviewsPage, name='myReviewsPage'),
    path('myreviews/<int:id>/edit', views.reviewsEditPage, name='reviewsEditPage'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)