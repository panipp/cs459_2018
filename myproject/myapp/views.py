from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from .models import Product
from django.views import generic
from django.views.generic.detail import DetailView


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def product_list(request):
    num=1
    text = "<style type=\"text/css\">body{background: #ead6bd;color: #00142f;font-size: 40px;}#head{padding: 60px;text-align: center;background: #504e63;color: white;font-size: 50px;}</style><div id=\"head\">List of Product</div>"
    for i in Product.objects.all():
        text=text+"<div style=\"padding-left: 500px;padding-top: 15px;\">"+str(num)+". "+str(i)+"<br /></div>"
        num+=1
    return HttpResponse(text)

# Use web api
# def product_detail(request):
#     num=1
#     detail = "<style type=\"text/css\">body{background: #ead6bd;color: #00142f;font-size: 40px;}#head{padding: 60px;text-align: center;background: #504e63;color: white;font-size: 50px;}</style><div id=\"head\">Product Detail</div>"
#     for i in Product.objects.all():
#         detail=detail+"<div style=\"text-align: center;padding: 25px; display: block;background: #a88661;color: white;margin-top:10px;\">Product "+str(num)+" : "+str(i)+"<br />Price : "+str(i.price)+" Baht<br />Category : "+str(i.category)+"<br />QR code<br /><img id=\'barcode\' src=\"https://api.qrserver.com/v1/create-qr-code/?data="+str(i.name)+"&amp;\" width=\"100\" height=\"100\" /><br /></div>"
#         num+=1
#     return HttpResponse(detail)

def product_detail(request):
    num=1
    detail = "<style type=\"text/css\">body{text-align: center;background: #ead6bd;color: #00142f;font-size: 30px;}#head{padding: 60px;text-align: center;background: #504e63;color: white;font-size: 50px;}</style> \
    <div id=\"head\">Product Detail</div>\
    <script src=\"https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js\"></script> \
    <script src=\"https://cdn.rawgit.com/davidshimjs/qrcodejs/gh-pages/qrcode.min.js\"></script> "
    for i in Product.objects.all():
        detail=detail+"<div style=\"padding: 25px; display: block;background: #a88661;color: white;margin-top:10px;\">\
        Product "+str(num)+" : "+str(i)+"<br />Price : "+str(i.price)+" Baht<br />\
        Category : "+str(i.category)+"<br />QR code<br />\
        <div align=\"center\" id=\""+str(i.name)+"\"></div>\
        <script type=\"text/javascript\"> new QRCode(document.getElementById(\""+str(i.name)+"\"),{ text:\""+str(i.name)+"\",width:100,height:100});</script></div>"
        num+=1
    return HttpResponse(detail)

def item(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request,'item.html',context)

def details(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request,'details.html',context)

def test(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request,'testbase.html',context)

class ProductListView(generic.ListView):
    model = Product
    template_name = 'listitem.html'
    queryset = Product.objects.all()
    # queryset = Product.objects.filter(category='V')
    # paginate_by = 4
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ProductListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['name'] = 'Hi'
        return context

class ProductDetailView(DetailView):

    model = Product
    template_name = 'detailitem.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context