from django.shortcuts import render, get_object_or_404

# Create your views here.

from blog.models import BlogArticles

def test(request):
    my_list = [1,2,3,4]
    return render(request, "test.html", {"my_list":my_list})

def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog/titles.html", {"blogs": blogs})


def blog_body(request, article_id):
    #article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id)
    pub = article.publish
    return render(request, "blog/content.html", {"article":article, "publish":pub})




