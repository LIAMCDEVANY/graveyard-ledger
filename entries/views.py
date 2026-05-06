from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Entry
from .forms import EntryForm


def home(request):
    return render(request, 'home.html')


def signup(request):
    error_message = ''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('entry-index')

        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()

    return render(request, 'registration/signup.html', {
        'form': form,
        'error_message': error_message
    })


@login_required
def entry_index(request):
    entries = Entry.objects.filter(user=request.user)

    return render(request, 'entries/index.html', {
        'entries': entries
    })


@login_required
def entry_detail(request, entry_id):
    entry = Entry.objects.get(
        id=entry_id,
        user=request.user
    )

    return render(request, 'entries/detail.html', {
        'entry': entry
    })


@login_required
def entry_create(request):

    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)

            new_entry.user = request.user
            new_entry.save()

            return redirect('entry-index')

    else:
        form = EntryForm()

    return render(request, 'entries/create.html', {
        'form': form
    })


@login_required
def entry_update(request, entry_id):

    entry = Entry.objects.get(
        id=entry_id,
        user=request.user
    )

    if request.method == 'POST':
        form = EntryForm(
            request.POST,
            instance=entry
        )

        if form.is_valid():
            form.save()

            return redirect(
                'entry-detail',
                entry_id=entry.id
            )

    else:
        form = EntryForm(instance=entry)

    return render(request, 'entries/update.html', {
        'form': form,
        'entry': entry
    })


@login_required
def entry_delete(request, entry_id):

    entry = Entry.objects.get(
        id=entry_id,
        user=request.user
    )

    if request.method == 'POST':
        entry.delete()

        return redirect('entry-index')

    return render(request, 'entries/delete.html', {
        'entry': entry
    })