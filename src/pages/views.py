from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import transaction
from .models import JournalEntry

def homePageView(request):
	entries = reversed(
		JournalEntry.objects.order_by('date')
	)

	### OWASP A04 - Uncomment to ensure no unauthorized private journal entries are sent to the front end ###
	# if request.user.username:
	# 	entries = [e for e in entries if e.public or e.author == request.user]
	# else:
	# 	entries = [e for e in entries if e.public]

	return render(request, 'pages/index.html', {'entries': entries})

def writeView(request):
	entry = JournalEntry(author=request.user, text=request.POST['entry_text'])
	if request.POST['public'] == "false":
		entry.public = False
	entry.save()
	return redirect("home")

### OWASP A01 - Uncomment to ensure anonymouse users can't access this endpoing at all ###
# @login_required
def deleteView(request):
	eid = request.GET['eid']
	entry = JournalEntry.objects.filter(id=eid).first()

    ### OWASP A01 - Uncomment to ensure user is the author of the journal entry being deleted ###
	# if not entry.author == request.user:
	# 	return redirect("home")

	entry.delete()
	return HttpResponse('Item deleted! <a href="/">Back to home</a>')