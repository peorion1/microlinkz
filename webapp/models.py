from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CPU(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    cores = models.PositiveIntegerField()
    clock_speed = models.DecimalField(max_digits=5, decimal_places=2)
    socket = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product.name} - CPU"

class GPU(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    vram = models.PositiveIntegerField()
    memory_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product.name} - GPU"

class RAM(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    capacity = models.PositiveIntegerField()
    speed = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - RAM"

class Storage(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    capacity = models.PositiveIntegerField()
    storage_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product.name} - Storage"

class PowerSupply(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    wattage = models.PositiveIntegerField()
    efficiency_rating = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product.name} - Power Supply"

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateField()

    def __str__(self):
        return f"Order for {self.product.name}"

