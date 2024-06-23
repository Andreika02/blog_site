from django.shortcuts import render
import random
# Create your views here.
def magic_number(request):
    if request.method == "POST":
        number = int(request.POST["number"])
        # print(type(number))
        # print(request.POST)
        random_number = random.randint(1,5)
        if number == random_number:
            result = "Win"
        else:
            result = f"Sorry, was anothet number: {random_number}, try again"
        return render(request, "core/magic_number.html", {"result":result})
    return render(request, "core/magic_number.html")
# render - отрисовка

def mysite(request):
    return render(request, "core/mysite.html")