from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

def blog(request):
	pop_articles = Article.objects.order_by('-views')[:5]
	article_list = Article.objects.order_by('-date_create')[:]
	page = request.GET.get('page', 1)

	paginator = Paginator(article_list, 4)
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	return render_to_response('blog.html', {
											'pop_articles': pop_articles,
											'articles': articles,
											})
