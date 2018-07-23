from django.db import models
from django.urls import reverse
import datetime

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length = 60)

    def natural_key(self):
        return(self.name)

    def __str__(self):
        return self.name

class Contract_type(models.Model):

    contract_type = models.CharField(max_length = 60)

    def natural_key(self):
        return(self.contract_type)

    def __str__(self):
        return self.contract_type

class Currency(models.Model):

    currency_type = models.CharField(max_length = 60)

    def natural_key(self):
        return(self.currency_type)

    def __str__(self):
        return self.currency_type

class Contract(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    contract_type = models.ForeignKey(Contract_type, on_delete=models.CASCADE)
    currency_type = models.ForeignKey(Currency, on_delete=models.CASCADE)
    date_start= models.DateField(default=datetime.date.today)
    date_end = models.DateField(default=datetime.date.today)
    contract_value = models.DecimalField(max_digits=20, decimal_places=2)


    def __int__(self):
        return self.id

    # def get_absolute_url(self):
    #     return reverse("posts:detail", kwargs={"id": self.id})

    # class Meta:
    #     ordering = ["-timestamp", "-updated"]