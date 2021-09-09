from django.http import HttpResponse # Django Part 6 Code
from django.shortcuts import render # Django Part 7 Code

# This takes the home request from a user and gives them back a response of "Welcome user!"
def home(request):
    # user = request.user # Django Part 6 Code
    # return HttpResponse("<h1>Welcome {}!</h1>".format(user)) # Django Part 6 Code
    profiles = ["Nick", "Katie", "Tom", "Kim", "Andy", "Matt", "Ty", "Heather", "Marissa", "Connor"]
    context = { # Django Part 7 Code
        'profiles': profiles,
    }
    return render(request, "home.html", context) # Django Part 7 Code