from django.http import HttpResponse
from django.shortcuts import redirect

def session_count(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 0

    return HttpResponse(str(request.session['count']))

def session_flush(request):
    request.session.flush()
    return redirect("/session_count")
