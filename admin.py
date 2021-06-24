from django.contrib import admin
from . models import Order,Product,User,Book,Author,Address,Country

class UserAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name']

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price']

class OrderAdmin(admin.ModelAdmin):
    list_display=["user","quantity"]

# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Country)




