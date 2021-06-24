from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=8)

    def __str__(self):
        return "{} , {}".format(self.name, self.code)


class Address(models.Model):
    street_name = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=8)
    city = models.CharField(max_length=100)

    def __str__(self):
        return "{}, {} ,{}".format(self.street_name, self.postal_code, self.city)


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{} ,{} ,{}".format(self.first_name, self.last_name,self.address)


class Book(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    published_counties = models.ManyToManyField(Country, null=True)

    def __str__(self):
        return "{} ,{} ,{} ,{}".format(self.title, self.author,self.rating,self.published_counties)

    class Meta:  # overwrite db_table value by definig this class
        db_table = "books"


# ----------------------------------------------------------------------



class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return "{} {}".format(self.name, self.price)


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return "{}".format(self.id)

#rProduct.objects,create(name="phone',price=22)
#rashmi.product.add(objproductname)