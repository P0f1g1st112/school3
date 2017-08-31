from django.shortcuts import render_to_response


def about(request):
	return render_to_response('about_remont.html')
