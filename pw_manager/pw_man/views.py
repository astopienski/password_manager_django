from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import get_user
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from pw_man.models import *


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def index(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))


@login_required
def create_db(request):
    template = loader.get_template('create_db.html')
    return HttpResponse(template.render({}, request))


@login_required
def create_db_record(request):
    db_user_input = request.POST['db_name']
    user = get_user(request)

    db_exists = Databases.objects.filter(db_name=db_user_input).first()
    if db_exists:
        messages.error(request, "Eine Datenbank mit diesem Namen schon existiert!")
        return HttpResponseRedirect(reverse('create_db'))
    else:
        db = Databases(db_name=db_user_input, user=user)
        db.save()
        return HttpResponseRedirect(reverse('show_dbs'))


@login_required
def update_db(request, db_id):
    db = Databases.objects.get(db_id=db_id)
    context = {
        'db': db,
    }
    template = loader.get_template('update_db.html')
    return HttpResponse(template.render(context, request))


@login_required
def update_db_record(request, db_id):
    db_name = request.POST['db_name']

    db = Databases.objects.get(db_id=db_id)
    db.db_name = db_name
    db.save()
    return HttpResponseRedirect(reverse('show_dbs'))


@login_required
def delete_db(request, db_id):
    db = Databases.objects.get(db_id=db_id)
    context = {
        'db': db,
    }
    template = loader.get_template('delete_db.html')
    return HttpResponse(template.render(context, request))


@login_required
def delete_db_record(request, db_id):
    if request.POST.get and 'delete_db' in request.POST:
        db_delete = Databases.objects.get(db_id=db_id)
        db_delete.delete()
        messages.error(request, f"Die Datenbank Nr. {db_id} wurde gelöscht")
        return HttpResponseRedirect(reverse('show_dbs'))
    elif request.POST.get and 'back' in request.POST:
        return HttpResponseRedirect(reverse('show_dbs'))


@login_required
def show_dbs(request):
    user = get_user(request)
    dbs = Databases.objects.filter(user=user)
    context = {
        'dbs': dbs,
    }
    template = loader.get_template('databases.html')
    return HttpResponse(template.render(context, request))


@login_required
def show_passwords(request, db_id):
    pswds = Passwords.objects.filter(db=db_id)
    dbs = Databases.objects.filter(db_id=db_id)
    context = {
        'pswds': pswds,
        'dbs': dbs,
    }
    template = loader.get_template('passwords.html')
    return HttpResponse(template.render(context, request))


@login_required
def create_pw(request, db_id):
    template = loader.get_template('create_pw.html')
    return HttpResponse(template.render({}, request))


@login_required
def create_pw_record(request, db_id):
    username = request.POST['username']
    pw = request.POST['pw']
    link = request.POST['link']
    note = request.POST['note']

    db = Databases.objects.get(db_id=db_id)

    pw_save = Passwords(db=db, pw_username=username, pw_password=pw, pw_link=link, pw_note=note)
    pw_save.save()
    return HttpResponseRedirect(reverse('show_passwords', args=(db_id,)))


@login_required
def update_pw(request, db_id, pw_id):
    pswd = Passwords.objects.get(pw_id=pw_id)
    context = {
        'pswd': pswd,
    }
    template = loader.get_template('update_pw.html')
    return HttpResponse(template.render(context, request))


@login_required
def update_pw_record(request, db_id, pw_id):
    username = request.POST['username']
    pw = request.POST['pw']
    link = request.POST['link']
    note = request.POST['note']

    db = Databases.objects.get(db_id=db_id)
    pw_update = Passwords.objects.get(pw_id=pw_id)
    pw_update.pw_username = username
    pw_update.pw_password = pw
    pw_update.pw_link = link
    pw_update.pw_note = note
    pw_update.db = db
    pw_update.save()
    return HttpResponseRedirect(reverse('show_passwords', args=(db_id,)))



@login_required
def delete_pw(request, db_id, pw_id):
    pswd = Passwords.objects.get(pw_id=pw_id)
    context = {
        'pswd': pswd,
    }
    template = loader.get_template('delete_pw.html')
    return HttpResponse(template.render(context, request))


@login_required
def delete_pw_record(request, db_id, pw_id):
    if request.POST.get and 'delete_pw' in request.POST:
        pw_delete = Passwords.objects.get(pw_id=pw_id)
        pw_delete.delete()
        messages.error(request, f"Das Passwort Nr. {pw_id} wurde gelöscht")
        return HttpResponseRedirect(reverse('show_passwords', args=(db_id,)))
    elif request.POST.get and 'back' in request.POST:
        return HttpResponseRedirect(reverse('show_passwords', args=(db_id,)))