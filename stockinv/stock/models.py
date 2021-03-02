from django.db import models
class Catgory(models.Model):
	name=models.CharField(max_length=100)

class Manufacturer(models.Model):
	name=models.CharField(max_length=100)
	Brand = models.CharField(max_length=100)
	origin = models.CharField(max_length=100)
	vendor = models.CharField(max_length=100)
class stock(models.Model):
	name = models.CharField(max_length=100)
	measurement = models.CharField(max_length=100)
	storingmethod = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	cost=models.PositiveIntegerField()
	retailprice=models.PositiveIntegerField()
	size = models.PositiveIntegerField()
	color = models.CharField(max_length=100)
	LotNo=models.PositiveIntegerField()
	product_type=models.CharField(max_length=100)
	category= models.ForeignKey(Catgory,on_delete=models.CASCADE)
	manufacturer =models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.name)

