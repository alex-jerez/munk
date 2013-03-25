from django.shortcuts import render
from django.http import HttpResponseRedirect
from search.models import MunkSearchForm

def mainview(request):
  if request.method == 'POST':
      form = MunkSearchForm(request.POST)
      if form.is_valid():
	return HttpResponseRedirect('/results/')
  else:
      form = MunkSearchForm()
  return render(request, 'form1.html', {
    'form':form,
    })
