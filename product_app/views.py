from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from .models import Product

def shop_list(request):
    all_products = Product.objects.all() # slice notation, [start:stop]
    products_quantity = Product.objects.count()
    latest_products_1 = Product.objects.all()[0:3]
    latest_products_2 = Product.objects.all()[3:6]
    return render(request,"shop-list.html",{'all_products':all_products,
                                            'num':products_quantity,
                                            'latest_products_1':latest_products_1,
                                            'latest_products_2':latest_products_2})
def blog(request):
    return render(request,'main-blog.html')
def handle_uploaded_file(f,image_name):
    with open("media/"+image_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def handle_uploaded_file_latest_img(f,image_name):
    with open("media/"+image_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def create_item(request):
    if request.method == 'POST':
        valid = Product.objects.create(p_desc="An Iphone with smashed screen",
                                   p_name="Broken Iphone",
                                   p_price=340,
                                   slug="broken-iphone33")
        data = request.FILES
        handle_uploaded_file(request.FILES['ImageFile'],str(data['ImageFile']))
        handle_uploaded_file_latest_img(request.FILES['ImageFile_1'],str(data['ImageFile_1']))
        print("Image File is : ",data['ImageFile'])
        print(type(data['ImageFile']))
        print("Image File is : ", data['ImageFile_1'])
        print(type(data['ImageFile_1']))
        Product.objects.filter(pk=11).update(p_image=data['ImageFile'],
                                             p_latest_img=data['ImageFile_1'])
        if valid:
            return HttpResponse('Item created')
    return render(request, 'upload_image.html')
def shop_details(request,slug):
    product = get_object_or_404(Product,slug=slug)
    product_images = Product.objects.all()
    print("product is : ",product)
    return render(request,'shop-details.html',
                  {'product':product,
                   'product_images':product_images})