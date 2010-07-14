from django.template import Context, loader
from bsnet.brainstorm.models import Topic, Response
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
	latest_bs_list = Topic.objects.all().order_by('-pub_date')[:5]
	return render_to_response('brainstorms/index.html', {'latest_bs_list': latest_bs_list})


def details(request, topic_id):
	topic = get_object_or_404(Topic, pk=topic_id)
	return render_to_response('brainstorms/details.html', {'topic': topic})
