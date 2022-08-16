from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Account, Contestant


def voting(request, has_registered, first_name=None, last_name=None, voter_class=None, voter_section=None):
    all_contestants = Contestant.objects.all()
    headboy_contestants = Contestant.objects.filter(position='Head Boy')
    headgirl_contestants = Contestant.objects.filter(position='Head Girl')
    vice_headboy_contestants = Contestant.objects.filter(position='Vice Head Boy')
    vice_headgirl_contestants = Contestant.objects.filter(position='Vice Head Girl')
    sports_captain_contestants = Contestant.objects.filter(position='Sports Captain')
    vice_sports_captain_contestants = Contestant.objects.filter(position='Vice Sports Captain')

    votes = 0
    for contestant in all_contestants:
        votes += contestant.votes
    context = {
        'has_registered': has_registered,
        'votes': int(votes/6),
        'headboy_contestants': headboy_contestants,
        'headgirl_contestants': headgirl_contestants,
        'vice_headboy_contestants': vice_headboy_contestants,
        'vice_headgirl_contestants': vice_headgirl_contestants,
        'sports_captain_contestants': sports_captain_contestants,
        'vice_sports_captain_contestants': vice_sports_captain_contestants,
        'first_name': first_name,
        'last_name': last_name,
        'voter_class': voter_class,
        'voter_section': voter_section,
        'classes': ['6', '7', '8', '9', '10', '11', '12'],
        'section': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

    }

    return render(request, 'voting.html', context)


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        voter_class = request.POST['voter_class']
        voter_section = request.POST['voter_section']
        is_registered = Account.objects.filter(first_name=first_name, last_name=last_name, voter_class=voter_class, voter_section=voter_section).exists()
        if is_registered:
            voter = Account.objects.get(first_name=first_name, last_name=last_name, voter_class=voter_class, voter_section=voter_section)
            if voter.contestant.exists():
                messages.success(request, 'You have already voted!, change your votes if required')
            else:
                messages.success(request, 'You are already registered, vote now!')
        else:
            voter = Account()
            voter.first_name = first_name
            voter.last_name = last_name
            voter.voter_class = voter_class
            voter.voter_section = voter_section
            voter.save()
        url = f'/voting/1/{first_name}/{last_name}/{voter_class}/{voter_section}/'
        return redirect(url)


def contestant(request):
    if request.method == 'POST':
        headboy = request.POST['headboy']
        headgirl = request.POST['headgirl']
        vice_headboy = request.POST['vice_headboy']
        vice_headgirl = request.POST['vice_headgirl']
        sports_captain = request.POST['sports_captain']
        vice_sports_captain = request.POST['vice_sports_captain']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        voter_class = request.POST['voter_class']
        voter_section = request.POST['voter_section']
        headboy_contestant = Contestant.objects.get(contestant_name=headboy)
        headboy_contestant.votes += 1
        headboy_contestant.save()
        headgirl_contestant = Contestant.objects.get(contestant_name=headgirl)
        headgirl_contestant.votes += 1
        headgirl_contestant.save()
        vice_headboy_contestant = Contestant.objects.get(contestant_name=vice_headboy)
        vice_headboy_contestant.votes += 1
        vice_headboy_contestant.save()
        vice_headgirl_contestant = Contestant.objects.get(contestant_name=vice_headgirl)
        vice_headgirl_contestant.votes += 1
        vice_headgirl_contestant.save()
        sports_captain_contestant = Contestant.objects.get(contestant_name=sports_captain)
        sports_captain_contestant.votes += 1
        sports_captain_contestant.save()
        vice_sports_captain_contestant = Contestant.objects.get(contestant_name=vice_sports_captain)
        vice_sports_captain_contestant.votes += 1
        vice_sports_captain_contestant.save()
        voter = Account.objects.get(first_name=first_name, last_name=last_name, voter_class=voter_class, voter_section=voter_section)
        if voter.contestant is not None:
            for i in voter.contestant.all():
                i.votes -= 1
                i.save()
        voter.contestant.clear()
        voter.contestant.add(headboy_contestant)
        voter.contestant.add(headgirl_contestant)
        voter.contestant.add(vice_headboy_contestant)
        voter.contestant.add(vice_headgirl_contestant)
        voter.contestant.add(sports_captain_contestant)
        voter.contestant.add(vice_sports_captain_contestant)
        voter.save()
        return render(request, "voting_successful.html")


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        if username == 'test' and password == 'uma11000':
            return redirect('/voting/0/')
        else:
            return HttpResponse("invalid credentials")
    else:
        return render(request, "login.html")












