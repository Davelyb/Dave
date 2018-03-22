from django.db import models

# Create your models here.

import datetime

from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):  
        return self.question_text

    def was_published_recently(self):
        return ( self.pub_date >= ( timezone.now() - datetime.timedelta(days=1) ) )\
        and ( self.pub_date <= timezone.now() )

        # return ( self.pub_date >= ( timezone.now() - datetime.timedelta(days=1) ) )


class Choice(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)