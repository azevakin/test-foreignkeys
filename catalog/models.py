from django.db import models


class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.TextField()
    category = models.ForeignKey(Category, db_constraint=False)
    unit = models.ForeignKey(Unit, db_constraint=False)

    def __str__(self):
        return self.name
