from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from waterapp.models import AddCompany,Products,Registration,AddtoCart
from django.contrib.auth.models import User
from django.contrib import messages


class index(TemplateView):
    template_name='Admin/index.html'
class Add_company(TemplateView):
    template_name='admin/add_company.html'
    def post(self, request, *args, **kwargs):
        companyname = request.POST['companyname']
        image = request.FILES['image']
        ob=FileSystemStorage()
        obj=ob.save(image.name,image)
        com=AddCompany()
        com.companyname=companyname
        com.logo=obj
        com.save()
        return redirect('/admin')

class ViewCompanies(TemplateView):
    template_name='admin/view_company.html'
    def get_context_data(self, **kwargs):
        view_company = AddCompany.objects.all()
        context = {
            'view_company':view_company
        }
        return context
class Remove(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        AddCompany.objects.get(id=id).delete()
        return redirect('/admin')
class EditCompany(TemplateView):
    template_name='admin/edit_company.html'
    def get_context_data(self, **kwargs):
        context = super(EditCompany, self).get_context_data(**kwargs)
        id3 = self.request.GET['id']
        pro = AddCompany.objects.get(id=id3)
        context['upd'] = pro
        return context
    def post(self, request, *args, **kwargs):
        id3 = self.request.GET['id']
        companyname = request.POST['companyname']
        image = request.FILES['image']
        qty=request.POST['qty']
        ob=FileSystemStorage()
        obj=ob.save(image.name, image)
        com=AddCompany.objects.get(id=id3)
       
        com.companyname=companyname
        com.logo=obj
        com.total_quantity=qty
        com.save()
        return redirect('/admin')

class Add_Products(TemplateView):
    template_name='admin/add_products.html'
    def get_context_data(self, **kwargs):
        context = super(Add_Products, self).get_context_data(**kwargs)
        pro = AddCompany.objects.all()
        context = {
            'name':pro
        }
        return context
    def post(self, request, *args, **kwargs):
        companyname = request.POST['companyname']
        size=request.POST['size']
        price=request.POST['price']
        image = request.FILES['image']
        qty=request.POST['qty']
        ob=FileSystemStorage()
        obj=ob.save(image.name,image)
        pd=Products()
        pd.companyname_id=companyname
        pd.size=size
        pd.price=price
        pd.total_quantity=qty

        pd.image=obj
        pd.save()
        return redirect('/admin', {'message': "Product Added"})

class ViewProducts(TemplateView):
    template_name='admin/view_products.html'
    def get_context_data(self, **kwargs):
        view_products = Products.objects.all()
        context = {
            'view_products':view_products
        }
        return context

class RemoveProduct(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        Products.objects.get(id=id).delete()
        return redirect('/admin')
class EditProduct(TemplateView):
    template_name='admin/edit_product.html'
    
    def get_context_data(self, **kwargs):
        context = super(EditProduct, self).get_context_data(**kwargs)
        id3 = self.request.GET['id']
        pro = Products.objects.get(id=id3)
        prod = AddCompany.objects.all()
        context = {
            'name':prod,
            'upd':pro
        }
        return context
    def post(self, request, *args, **kwargs):
        id3 = self.request.GET['id']
        companyname = request.POST['companyname']
        size=request.POST['size']
        price=request.POST['price']
        image = request.FILES['image']
        qty=request.POST['qty']

        ob=FileSystemStorage()
        obj=ob.save(image.name, image)
        pd=Products.objects.get(id=id3)
       
        pd.companyname_id=companyname
        pd.size=size
        pd.price=price
        pd.total_quantity=qty
        pd.image=obj
        pd.save()
        return redirect('/admin', {'message': "Product Updated"})

class RemoveUser(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        Registration.objects.get(id=id).delete()
        return redirect('/admin')
class ViewUsers(TemplateView):
    template_name='admin/view_users.html'
    def get_context_data(self, **kwargs):
        view_users = Registration.objects.all()
        context = {
            'view_users':view_users
        }
        return context
class ConfirmOrder(TemplateView):
    template_name='Admin/view_orders.html'
    def get_context_data(self, **kwargs):

        cart = AddtoCart.objects.filter(status="Added")
        context = {
            'cart_items':cart
        }
        return context
class Reject(View):
    def dispatch(self,request,*args,**kwargs):

        id = request.GET['id']
        AddtoCart.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'],{'message':"Removed"})
    
class OrderApprove(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = AddtoCart.objects.get(pk=id)
        user.status = 'Order Approved'
        user.save()
        return render(request, 'Admin/index.html', {'message': " Order Approved"})

        

