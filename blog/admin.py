from django.contrib import admin
from .models import Post
from .models import Person
from .models import Article
from .models import Reporter
# Register your models here.
admin.site.register(Post)
admin.site.register(Article)
admin.site.register(Person)
admin.site.register(Reporter)