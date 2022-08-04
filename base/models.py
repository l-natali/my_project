from django.db import models


class Category(models.Model):
    title = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)


class Dishes(models.Model):
    title = models.CharField(unique=True, max_length=50, db_index=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=360)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} {self.price}\n{self.description}'

    class Meta:
        ordering = ('price',)


class Events(models.Model):
    title = models.CharField(unique=True, max_length=50, db_index=True)
    price = models.DecimalField(max_digits=3, decimal_places=0)
    description = models.TextField(max_length=1000)
    img = models.ImageField(unique=True, upload_to='uploads/')

    def __str__(self):
        return f'{self.title} {self.price}\n{self.description}'


class Gallery(models.Model):
    position = models.SmallIntegerField(unique=True)
    img = models.ImageField(unique=True, upload_to='uploads/')

    class Meta:
        ordering = ('position',)


class Specials(models.Model):
    title = models.CharField(unique=True, max_length=50, db_index=True)
    description = models.TextField(max_length=1000)
    img = models.ImageField(unique=True, upload_to='uploads/')

    def __str__(self):
        return f'{self.title} {self.description}'
