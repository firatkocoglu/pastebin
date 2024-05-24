from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.utils.crypto import get_random_string
from django.utils.formats import localize
from django.http import Http404
from datetime import datetime, timedelta
from .forms import PlainTextForm
from .models import PlainText


# Create your views here.
def renderHome(request):
    context = {}
    context["form"] = PlainTextForm()
    return render(request, "home.html", context)


@csrf_exempt
def postText(request):
    if request.method == "POST":
        form = PlainTextForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            # PARSE FORM INPUTS
            text = form_data["text"]
            # THIS FORM DATA GIVES US HOW MANY DAYS THE TEXT SHOULD BE VALID. THIS DATA CAN ALSO BE NULL.
            expire_days = form_data["expiry"]
            # WE CALCULATE THE EXPIRATION DATE WITH GIVEN 'EXPIRE DAYS'. IF EXPIRE DAYS ARE NOT GIVEN THEN EXPIRY IS NONE (DOES NOT EXPIRE)
            expiry = (
                datetime.now() + timedelta(days=expire_days)
                if expire_days is not None
                else None
            )
            # GENERATE AN UNIQUE URL
            unique_url = get_random_string(length=10)
            # CREATE TEXT RECORD
            text = PlainText.objects.create(
                text=form_data["text"], link=unique_url, expiry=expiry
            )
            text.save()
    return HttpResponseRedirect(unique_url)


@csrf_exempt
def renderSuccess(request, link):
    text = get_object_or_404(PlainText, link=link)
    context = {"link": link}
    context["text"] = text.text
    context["id"] = text.id

    if text.expiry is None:
        context["expiry"] = "No expiry date."
    else:
        localized_now = localize(datetime.now())
        localized_expiry = localize(text.expiry)
        # EXPIRED TEXTS ARE NOT ACCESSIBLE
        if localized_now > localized_expiry:
            raise Http404
        else:
            context["expiry"] = text.expiry

    return render(request, "success.html", context)


@csrf_exempt
def deleteText(request):
    if request.method == "POST":
        id = request.POST.get("id")
        text = get_object_or_404(PlainText, pk=id)
        text.delete()
    return redirect(renderHome)
