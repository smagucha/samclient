from django.shortcuts import render, redirect
from .forms import productform
from .models import stock
def home(request):
	return render(request, 'stock/home.html')

def addproduct(request):
	form = productform(request.POST)
	if request.method =='POST':
		form = productform(request.POST)
		if form.is_valid():
			form.save()
			form = productform()
		return redirect('product-list')
	else:
  		form = productform()
	return render(request, 'stock/addproduct.html', {'form': form})

def addcategory(request):
	form = categoryform(request.method='POST')
	if request.method=='POST':
		form = categoryform(request.method='POST')
		if form.is_valid():
			form.save()
			form =categoryform()
		return redirect('addproduct')
	else:
		form = categoryform()
	return render(request, 'stock/addcategory.html', {'form': form})

def productlist(request):
	product=stock.objects.all()
	return render(request, 'stock/product-list.html',{'product':product})

def updateproduct(request,id):
	obj = stock.objects.get(id=id)
	form = productform(request.POST or None, instance= obj)
	if form.is_valid():
  		form.save()
  		form= productform()
  		return redirect('datacenter')
	return render(request, 'stock/updateproduct.html', {'obj':obj,'form': form})

def deleteproduct(request, id):
	delobj =stock.objects.get(id=id)
	if request.method == 'POST':
	    delobj.delete()
	    return redirect('datacenter')
	context = {
	    'delobj': delobj
	}
	return render(request, 'stock/deleteproduct.html', context)



def stockin(request):
	product=stock.objects.all()
	return render(request, 'stock/stock-in.html',{'product':product})

def stockaudit(request):
	product=stock.objects.all()
	return render(request, 'stock/stockaudit.html',{'product':product})

def stockout(request):
	product=stock.objects.all()
	return render(request, 'stock/stock-out.html',{'product':product})

def history(request):
	return render(request, 'stock/history.html')

def dashboard(request):
	return render(request, 'stock/dashboard.html')

def more(request):
	return render(request, 'stock/more.html')

def datacenter(request):
	product=stock.objects.all()
	return render(request, 'stock/datacenter.html',{'product':product})

def labelprint(request):
	return render(request, 'stock/labelprint.html')

def paysetting(request):
	return render(request, 'stock/paysetting.html')




