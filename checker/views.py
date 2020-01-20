import asyncio
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render
from django.http import JsonResponse
from .models import Url
from .tasks import check_url, check_urls


@login_required
def index(request):
    urls = Url.objects.all()
    return render(request, 'index.html', { 'urls': urls })

@require_POST
@login_required
def check(request):
    url_ids = request.POST.getlist('urls')
    urls = list(Url.objects.filter(id__in=url_ids))
    results = asyncio.new_event_loop().run_until_complete(check_urls(urls))
    return JsonResponse(results, safe=False)
