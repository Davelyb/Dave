from django.test import TestCase

# Create your tests here.

import datetime

from django.utils import timezone 

from .models import Question

from django.urls import reverse


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question.objects.create(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1,seconds=1)
        old_question = Question.objects.create(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)   


def create_question(question_text, **kwargs):
    time = timezone.now() + datetime.timedelta(**kwargs)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        print('111 test_no_question')

        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        print('222 test_past_question')

        create_question(question_text='Past question.', days=-30)
        response = self.client.get(reverse('polls:index'))

        print('123')
        print(response.context['latest_question_list'])

        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            # []
            ['<Question: Past question.>']
        )


    def test_future_question(self):
        print('333 test_future_question')

        create_question(question_text="Future question.", days=1)
        response = self.client.get(reverse('polls:index'))

        print('1'*15)
        print(response.context['latest_question_list'])

        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            []
        )

    def test_future_question_and_past_question(self):
        print('444 test_future_question_and_past_question')

        create_question(question_text="Past question1.", days=-30)
        create_question(question_text="Past question2.", days=-29)
        response = self.client.get(reverse('polls:index'))

        print('5'*15)
        print(response.context['latest_question_list'])

        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            # ['<Question: Pase question.>']
            ['<Question: Past question2.>', '<Question: Past question1.>']
        )


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):

        future_question = create_question(question_text="Future question.", days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
		
    def hahaha(self):

        future_question = create_question(question_text="Future question.", days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):

        past_question = create_question(question_text="Past question.", days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        #self.assertEqual(response.status_code, 200)
