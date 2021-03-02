from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('product-list', views.productlist, name='product-list'),
	path('stock-in', views.stockin, name='stock-in'),
	path('stock-out', views.stockout, name='stock-out'),
	path('stockaudit', views.stockaudit, name='stockaudit'),
	path('dashboard', views.dashboard, name='dashboard'),
	path('history', views.history, name='history'),
	path('more', views.more, name='more'),
	path('datacenter', views.datacenter, name='datacenter'),
	path('labelprint', views.labelprint, name='labelprint'),
	path('paysetting', views.paysetting, name='paysetting'),
	path('addproduct',views.addproduct, name='addproduct'),
	path('updateproduct/<int:id>/update', views.updateproduct,name='updateproduct'),
	path('deleteproduct/<int:id>/update', views.deleteproduct,name='deleteproduct')
 ]
