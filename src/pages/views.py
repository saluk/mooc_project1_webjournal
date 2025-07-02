from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import transaction
from .models import JournalEntry, PrivateView

def homePageView(request):
	entries = reversed(JournalEntry.objects.order_by('date'))
	return render(request, 'pages/index.html', {'entries': entries})

def writeView(request):
	entry = JournalEntry(author=request.user, text=request.POST['entry_text'])
	entry.save()
	return redirect("home")
