from django.db import models


# Create your models here.
class BlogManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )


class Blog(models.Model):
    title = models.CharField('Título', max_length=100)
    slug = models.SlugField('Atalho')
    introduction = models.TextField('Introducão', blank=True)
    text = models.TextField('Texto', blank=True)
    image = models.ImageField(upload_to='blog/images', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    objects = BlogManager()

    class Meta:
        db_table = 'blog'

    def __str__(self):
        return self.title
