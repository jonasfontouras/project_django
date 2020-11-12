from django.db import models



# Create your models here.
class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )


class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    introduction = models.TextField('Descrição', blank=True, max_length=200)
    description = models.TextField('Texto', blank=True)
    start_date = models.DateField('Data de início', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    objects = CourseManager()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('courses:details', (), args=[self.slug])

    class Meta:
        db_table = 'curso'

    def __str__(self):
        return self.name
