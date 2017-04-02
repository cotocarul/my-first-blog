from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.


from django.http import HttpResponse

# Create your views here.
def functiaInBlog(request):
    return HttpResponse("<h1> Din Blog, Te iubesc, Doamne!"
                        "Chiar daca Tu nu-mi dai putere!</h1>"
                        "<h3>Bine</h4>")
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})