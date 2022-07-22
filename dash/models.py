from django.db import models


# Create your models here.
class RaspberryInfo(models.Model):
    time = models.PositiveIntegerField(default=0)
    M1B1 = models.PositiveSmallIntegerField(default=0)
    M1B2 = models.PositiveSmallIntegerField(default=0)
    M1B3 = models.PositiveSmallIntegerField(default=0)
    M2B1 = models.PositiveSmallIntegerField(default=0)
    M2B2 = models.PositiveSmallIntegerField(default=0)
    M2B3 = models.PositiveSmallIntegerField(default=0)
    M3B1 = models.PositiveSmallIntegerField(default=0)
    M3B2 = models.PositiveSmallIntegerField(default=0)
    M3B3 = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = "Raspberry Info"
        verbose_name_plural = "Raspberries Info"


    def __str__(self):
        return f"{self.id},{self.time},{self.M1B1},{self.M1B2},{self.M1B3},\
{self.M2B1},{self.M2B2},{self.M2B3},\
{self.M3B1},{self.M3B2},{self.M3B3}"

    def getmachinetimes(self):
        return [self.M1B1 + self.M1B2 + self.M1B3,
                self.M2B1 + self.M2B2 + self.M2B3,
                self.M3B1 + self.M3B2 + self.M3B3
                ]
