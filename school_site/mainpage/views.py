from django.shortcuts import render_to_response
from .models import Article


def mainpage(request):

	article_newest = Article.objects.order_by('-date_create')[0]
	articles = Article.objects.order_by('-date_create')[1:5]
	pop_articles = Article.objects.order_by('-views')[:5]
	return render_to_response('main.html', {
											'article_newest': article_newest,
											'articles': articles,
											'pop_articles': pop_articles,
											})
