from django.urls import path
from waterapp.admin_views import index,Add_company,ViewCompanies,Remove,EditCompany,Add_Products,ViewProducts,EditProduct,RemoveProduct,RemoveUser,ViewUsers,ConfirmOrder,Reject,OrderApprove
urlpatterns = [
    path('', index.as_view(),name="index"),
    path('add_company',Add_company.as_view(),name="add_company"),
    path('view_users',ViewUsers.as_view()),
    path('add_products',Add_Products.as_view(),name="add_products"),
    path('viewcompanies',ViewCompanies.as_view()),
    path('remove',Remove.as_view()),
    path('edit',EditCompany.as_view()),
    path('viewproducts',ViewProducts.as_view()),
    path('editproduct',EditProduct.as_view()),
    path('removeproduct',RemoveProduct.as_view()),
    path('removeuser',RemoveUser.as_view()),
    path('confirmorder', ConfirmOrder.as_view()),
    path('reject',Reject.as_view()),
    path('approveorder',OrderApprove.as_view()),


]
def urls():
    return urlpatterns, 'admin','admin'