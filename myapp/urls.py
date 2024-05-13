from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.home,name="myapp_home"),
    path('reg/',views.reg,name="myapp_reg"),
    path('log/',views.log,name="myapp_log"),
    path('pro/<str:username>',views.profile,name="myapp_profile"),
    path('allpro/',views.allprofile,name="myapp_allprofile"),
    path('adm/',views.admin,name="myapp_admin"),
    path('pur/',views.purchase,name="myapp_purchase"),
    path('ap/',views.allproducts,name="myapp_allproducts"),
    path('view/<int:id>',views.all,name="myapp_all"),
    path('admnview/<int:id>',views.adm_cat_prod,name="myapp_admn_cat_prod"),
    path('access/',views.access,name="myapp_access"),
    path('accessview/',views.accessview,name="myapp_accessview"),
    path('cartv/',views.cartview,name="myapp_cartview"),
    path('addcart/<int:id>',views.addcart,name="myapp_addcart"),
    path('editpro/<str:username>',views.edit_prof,name="myapp_editpro"),
    path('dltpro/<str:username>',views.dlt_prof,name="myapp_dltpro"),
    path('products/',views.admin_prod,name="myapp_adminproduct"),
    path('cats/',views.admin_cat,name="myapp_admincat"),
    path('editp/<int:id>',views.edit_product,name="myapp_edit_prod"),
    path('dltp/<int:id>',views.deleteprod,name="myapp_dlt_prod"),
    path('editc/<int:id>',views.edit_cat,name="myapp_edit_cat"),
    path('dltc/<int:id>',views.deletecat,name="myapp_dlt_cat"),
    path('dltcartitem/<int:id>',views.deletecartitem,name="myapp_dlt_cartitem"),
    path('checkout/',views.checkout,name="myapp_checkout"),
    path('orderv/',views.orderview,name="myapp_orderview"),
    path('canclord/<int:id>',views.cancel_order,name="myapp_cancel_order"),
    path('listv/',views.viewlist,name="myapp_viewlist"),
    path('search/',views.search,name="myapp_search"),
    path('searchcat/',views.searchcat,name="myapp_searchcat"),
    path('fullp/',views.fullpro,name="myapp_fullpro"),
    path('prooo/',views.prooo,name="myapp_prooo"),
    

 ]