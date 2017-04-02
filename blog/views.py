from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

# Create your views here.
def functiaInBlog(request):
    return HttpResponse("<h1> Din Blog, Te iubesc, Doamne!"
                        "Chiar daca Tu nu-mi dai putere!</h1>"
                        "<h3>Bine</h4>")
def post_list(request):
    return render(request, 'blog/post_list.html', {})