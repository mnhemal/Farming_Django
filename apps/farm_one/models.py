from django.db import models



from utils.mixin import BaseModelMixin


# Create your models here.

class FarmOne(BaseModelMixin):
    """
    Farm One Database Schema
    """
    ph = models.FloatField(name="ph", null=True, blank=True)
    temperature = models.FloatField(name="temperature", null=True, blank=True)
    humidity = models.FloatField(name="humidity", null=True, blank=True)


    def __str__(self):
        return "ID: " + str(self.id) + ", PH: " + str(self.ph) + ", TEMPERATURE: " + str(self.temperature) + ", HUMIDITY: " + str(self.turbidity)



class Subject(BaseModelMixin):
    """
    Subject Database Schema
    """
    name = models.CharField(name="name", max_length=256, null=True, blank=True)
    code = models.CharField(name="code", max_length=256, null=True, blank=True)
    # is_active = models.BooleanField(name="is_active", default=True)

    def __str__(self):
        return "ID: " + str(self.id) + ", NAME: " + str(self.name) + ", CODE: " + str(self.code)


class FarmoneSubject(BaseModelMixin):
    """
    FarmoneSubject Database Schema
    """
    farmone = models.ForeignKey(FarmOne, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    # is_active = models.BooleanField(name="is_active", default=True)

    def __str__(self):
        return "ID: " + str(self.id) + ", FARMONE: " + str(self.farmone) + ", SUBJECT: " + str(self.subject)


