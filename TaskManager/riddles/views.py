from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Riddle, Option


def riddles_index(request):
    return render(request, 'base.html', {"latest_riddles": Riddle.objects.order_by("-pub_date")[:5]})


def detail(request, riddle_id):
    return render(request, "answer.html", {"riddle": get_object_or_404(Riddle, pk=riddle_id)})


def answer(request, riddle_id):
    riddle = get_object_or_404(Riddle, pk=riddle_id)
    try:
        option = riddle.option_set.get(pk=request.POST['option'])
    except (KeyError, Option.DoesNotExist):
        return render(request, 'answer.html', {'riddle': riddle, 'error_message': 'Option does not exist'})
    else:
        if option.correct:
            return render(request, "base.html", {"latest_riddles": Riddle.objects.order_by('-pub_date')[:5],
                                                  "message": "Nice! Choose another one!"})
        else:
            return render(request, 'answer.html', {'riddle': riddle, 'error_message': 'Wrong Answer!'})
