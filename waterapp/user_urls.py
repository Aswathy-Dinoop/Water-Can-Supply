from django.urls import path
from waterapp.user_views import index,ProductsView,Profile,single_product,Add_Cart,CartView,Remove,checkout,Thankyou,StatusView,Payment,chpayment
urlpatterns = [
    path('', index.as_view(),name="index"),
    path('products',ProductsView.as_view()),
    path('myprofile',Profile.as_view(),),
    path('single_product',single_product.as_view()),
    path('AddtoCart',Add_Cart.as_view()),
    path('CartView',CartView.as_view()),
    path('Remove',Remove.as_view()),
    path('checkout',checkout.as_view()),
    path('Thankyouforbooking',Thankyou.as_view()),
    path('orderstatus',StatusView.as_view()),
    path('payment',Payment.as_view()),
    path('chpayment',chpayment.as_view())




#     path('remove_users',RemoveUsers.as_view(),name="remove_users"),
#     path('view_servicers',Viewservicers.as_view(),name="view_servicers"),
#     path('',ViewUsers.as_view(),name="view_users"),
]
def urls():
    return urlpatterns, 'user','user'