from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from waterapp.models import Registration,Products,AddtoCart
from django.contrib.auth.models import User
from django.contrib import messages


class index(TemplateView):
    template_name='user/index.html'

class Profile(TemplateView):
    template_name='user/profile.html'
    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        id1 = self.request.user.id
        pro = Registration.objects.get(user_id=id1)
        context['profile'] = pro
        return context
class ProductsView(TemplateView):
    template_name='user/view_products.html'
    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        pro = Products.objects.all()
        context = {
            'products':pro
        }
        return context
class single_product(TemplateView):
    template_name='user/single_product.html'
    def get_context_data(self, **kwargs):
        context=super(single_product, self).get_context_data(**kwargs)
        id1=self.request.GET['id']
        view_pro = Products.objects.get(id=id1)
        context = {
            'view_pro':view_pro
        }
        return context


#################################

class Add_Cart(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.POST['id']  #shop-single html pagil ninu eduthath type hidden line
        qty=request.POST['quantity']
        prod=Products.objects.get(id=id)
        companyname=prod.companyname_id
        Tquantity=int(prod.total_quantity)-int(qty)
        price=prod.price
        total=int(qty)*int(price)
        prod.total_quantity=int(prod.total_quantity)-int (qty)
        prod.save()
        re = Registration.objects.get(user_id=self.request.user.id)
        ca=AddtoCart()
        ca.products_id=id 
        ca.user_id=re.id
        ca.status = 'Added'
        ca.payment = 'NULL'
        ca.price=total
        ca.quantity=qty
        ca.company_id=companyname
        # ca.Tquantity=Tquantity
        ca.save()       
        return redirect(request.META['HTTP_REFERER'],{'message':"Item selected"})
        # return redirect('/user')
class CartView(TemplateView):
    template_name="user/cart.html"
    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)  
        user = Registration.objects.get(user_id=self.request.user.id)      
        cart = AddtoCart.objects.filter(status='Added',user_id=user.id)
        sum=0
        for i in cart:
            sum=sum+int(i.price)

        context["totalvalue"] = sum

        context['cart'] = cart
        return context

class Remove(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        id2= request.GET['id2']
        cart= AddtoCart.objects.get(id=id)
        qty=cart.quantity
        prod=Products.objects.get(id=id2)
        prod.total_quantity=int(prod.total_quantity)+int(qty)
        prod.save()
        AddtoCart.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'],{'message':"Item remove"})

class checkout(TemplateView):
    template_name='user/checkout.html'
    def get_context_data(self, **kwargs):
        context = super(checkout, self).get_context_data(**kwargs) 
        user = Registration.objects.get(user_id=self.request.user.id)      
        cart = AddtoCart.objects.filter(status='Added',user_id=user.id)
        sum=0
        for i in cart:
            sum=sum+int(i.price)

        context["totalvalue"] = sum
        context['user'] = user
        context['booked_items'] = cart
        return context

class Thankyou(TemplateView):
    template_name ='user/thankyou.html'
class StatusView(TemplateView):
    template_name="User/order_status.html"
    def get_context_data(self, **kwargs):
        context = super(StatusView, self).get_context_data(**kwargs)  
        user = Registration.objects.get(user_id=self.request.user.id)      
        cart = AddtoCart.objects.filter(status="Order Approved",user_id=user.id)
        total = 0
        for i in cart:
            total = total + int(i.price)
        context['asz'] = total
        context['cart'] = cart
        return context
class Payment(TemplateView):
    template_name="User/payment.html"
    def get_context_data(self, **kwargs):
        context = super(Payment, self).get_context_data(**kwargs)  
        user = Registration.objects.get(user_id=self.request.user.id)      
        cart = AddtoCart.objects.filter(status="Order Approved",user_id=user.id)
        total = 0
        for i in cart:
            total = total + int(i.price)
        context['asz'] = total
        context['cart'] = cart
        return context
    
class chpayment(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        user = Registration.objects.get(user_id=self.request.user.id)      
        cart = AddtoCart.objects.filter(status="Order Approved",user_id=user.id)
        print(cart)
        for i in cart:
            i.payment = 'paid'
            i.status = 'paid'
            i.save()
        # for i in asg:
        #     i.status = 'paid'
        #     i.save()
        return render(request,'User/thanks.html',{'message':" payment Success"})