from django.db import models


# Create your models here.
class ProductManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )


class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    teste = models.CharField('Link Compra: ', max_length=300)
    description = models.TextField('Descrição', blank=True)
    image = models.ImageField(upload_to='core/images', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    objects = ProductManager()

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name
