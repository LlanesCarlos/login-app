from django.shortcuts import render
from django.shortcuts import redirect
from .models import Article
from .forms import ArticleForm


def index(request):
    articles = Article.objects.all()
    params = {
        'articles': articles,
    }
    return render(request, 'article/index.html', params)


def create(request):
    params = {
        'form': ArticleForm(),
    }
    if (request.method == 'POST'):
        title = request.POST['title']
        content = request.POST['content']
        article = Article(title=title, content=content)
        article.save()
        return redirect(to='/blog')
    else:
        return render(request, 'article/create.html', params)


def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    params = {
        'id': article_id,
        'article': article,
    }
    return render(request, 'article/detail.html', params)


def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    if (request.method == 'POST'):
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()
        return redirect(to='/blog')
    else:
        form = ArticleForm(initial={
            'title': article.title,
            'content': article.content,
            })
        params = {
            'id': article_id,
            'form': form,
        }
        return render(request, 'article/edit.html', params)


def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    if (request.method == 'POST'):
        article.delete()
        return redirect(to='/blog')
    else:
        params = {
            'id': article_id,
            'article': article,
        }
        return render(request, 'article/delete.html', params)
