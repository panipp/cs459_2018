"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import ProductListView
from myapp.views import ProductDetailView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('current_datetime/',views.current_datetime,name='current_datetime'),
    path('product_list/',views.product_list,name='product_list'),
    path('product_detail/',views.product_detail,name='product_detail'),
    path('item/',views.item,name='item'),
    path('details/',views.details,name='details'),
    path('tb/',views.test,name='tb'),
    path('glist/',ProductListView.as_view(),name='product-genericlist'),
    path('id/<int:pk>/', ProductDetailView.as_view(), name='product-genericdetail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
