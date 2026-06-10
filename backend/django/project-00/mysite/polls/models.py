import datetime
from django.utils import timezone

from django.db import models
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self) -> bool:
        now = timezone.now()
        # return self.pub_date >= now - datetime.timedelta(days=1)
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently???",
    )
    def was_published_recently(self) -> bool:
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question: Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text: str = models.CharField(max_length=200)
    votes: int = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
