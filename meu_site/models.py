from django.db import models
from django.utils import timezone
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")
    image = models.ImageField(verbose_name="Imagem", upload_to="projects")
    link = models.URLField(verbose_name="Endereço da Internet", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated = models.DateTimeField(auto_now=True, verbose_name="Data de Edição")
    
    # Criando a tabela e elementos do blog.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
   
