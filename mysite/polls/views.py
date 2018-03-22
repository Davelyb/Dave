from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Question, Choice

# from django.template import loader

from django.shortcuts import render, get_object_or_404

from django.http import Http404, HttpResponseRedirect

from django.urls import reverse

from django.views import generic

from django.utils import timezone

import datetime


# test test test


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        timedelta = timezone.now() - datetime.timedelta(days=1)
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        # return Question.objects.filter(pub_date__gte=timedelta).filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())
        # return Question.objects.filter(pub_date__lte=timezone.now() - datetime.timedelta(days=5, seconds=1))


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



# def index(request):
#   latest_question_list = Question.objects.order_by('-pub_date')[:5]
#   # template = loader.get_template('polls/index.html')
#   context = {
#       'latest_question_list': latest_question_list,
#   }
#   # return HttpResponse(template.render(context, request))
#   return render(request, 'polls/index.html', context)


# def index(request):
#   latest_question_list = Question.objects.order_by('-pub_date')[:5]
#   output = '<br />'.join([q.question_text for q in latest_question_list])
#   return HttpResponse(output)

# def index(request):
#     return HttpResponse("Hello, django! I'm in shanghai now.")


# def detail(request, question_id):
#   # try:
#   #   question = Question.objects.get(id=question_id)
#   # except Question.DoesNotExist:
#   #   raise Http404('Question does not exist')
    
#   question = get_object_or_404(Question, id=question_id)
#   return render(request, 'polls/detail.html', {'question': question})

# def detail(request, question_id):
#   return HttpResponse("You are viewing questiong %s." % question_id)


# def results(request, question_id):
#   response = "You're looking at the results of question %s."
#   return HttpResponse(response % question_id)


# def results(request, question_id):
#   question = get_object_or_404(Question, id=question_id)
#   return render(request, 'polls/results.html', {'question': question})


# def vote(request, question_id):
#   response = "You're voting on question %s."
#   return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "你还没有选中任何选项！"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def index(request):        
    home = Question.objects.all()
    context = {
        'home': home,
    }
    return render(request, 'home.html', context)