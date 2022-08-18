from django.db import models
from django.utils.timezone import now


class CategoryList(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class FailuresList(models.Model):

    description = models.CharField(max_length=30)
    category = models.ForeignKey(to='CategoryList', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Failure"
        verbose_name_plural = "Failures"

    def __str__(self):
        return f'{self.id} {self.category}: {self.description}'


class RunRegister(models.Model):

    time_stamp = models.DateTimeField(auto_now=False, auto_now_add=False, default=now)
    status = models.PositiveIntegerField(default=0)
    failure_id = models.ForeignKey(to='FailuresList', on_delete=models.DO_NOTHING)
    duration = models.FloatField(default=0, null=True)
    line_speed = models.PositiveSmallIntegerField(blank=False, default=60)
    bottle_count = models.PositiveIntegerField(blank=False, default=0)
    bottle_rejections = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.id}) s:{self.status}, d:{self.duration}, {self.failure_id}'

