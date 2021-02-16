from decimal import Decimal
from django.conf import settings
from product_app.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, a, quantity=1, update_quantity=False):
        product_id = str(a.id)
        announce = "default"
        if product_id not in self.cart:
            print("\n")
            announce = "New ",a.p_name," is added in the cart"
            self.cart[product_id] = {'p_name':str(a.p_name),
                                     'p_price':str(a.p_price),
                                     'p_desc': str(a.p_desc),
                                    'quantity': 0,
                                     'update_quantity':update_quantity} #cart already own Product attributes
        if update_quantity:
            print("\n")
            print("update status : ",update_quantity)
            pre_update = self.cart[product_id]['quantity']
            self.cart[product_id]['quantity'] = quantity
            announce = a.p_name + " is changed from "+str(pre_update)+" to "+str(self.cart[product_id]['quantity'])
        else:
            print("\n")
            before_added = self.cart[product_id]['quantity']
            self.cart[product_id]['quantity'] += quantity
            after_added = self.cart[product_id]['quantity']
            announce = a.p_name+" recently added "+str(quantity)+", had "+str(before_added)+" before, now is "+str(after_added)
        self.save()
        return announce

    def save(self):
        print("\n")
        print("saved cart : ",self.cart)
        print("self.session[settings.CART_SESSION_ID] : ",self.session[settings.CART_SESSION_ID])
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        print("\n")
        product_id = str(product.id)
        print("product id to be removed : ",product_id)
        print("the cart : ",self.cart)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        print("cart values = ",self.cart.values())
        for item in self.cart.values():
            item['price'] = Decimal(item['p_price'])
            print("price = ",item['price'])
            item['total_price'] = item['price'] * item['quantity']
            print("total price = ",item['total_price'])
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        print("\n")
        print("Now in get_total_price")
        return sum(Decimal(item['p_price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
