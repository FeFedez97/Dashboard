from django.db import models


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

    status = models.PositiveIntegerField(default=0)
    failure_id = models.ForeignKey(to='FailuresList', on_delete=models.DO_NOTHING)

