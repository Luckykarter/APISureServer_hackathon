# database models
from django.db import models


class Guarantee(models.Model):
    dealNumber = models.CharField(max_length=100, default='')
    customer = models.CharField(max_length=80, default='')
    moduleType = models.CharField(max_length=80, default='')
    stepId = models.CharField(max_length=6, default='')
    mode = models.CharField(max_length=80, default='')
    stepStatus = models.CharField(max_length=100, default='')

    Currency = models.CharField(max_length=3, default='')
    Amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def add_entry(self, info_bar: dict):
        self.dealNumber = info_bar.get("dealNumber")
        self.customer = info_bar.get("customer")
        self.moduleType = info_bar.get("moduleType")
        self.stepId = info_bar.get("stepId")
        self.mode = info_bar.get("mode")
        self.stepStatus = info_bar.get("stepStatus")

    def set_amount(self, data: dict):
        try:
            amount_section = data["GuaranteeApplicationDetails"]["UndertakingAmount"]["UndertakingAmount"]
            self.Amount = amount_section["Amount"]
            self.Currency = amount_section["CurrencyCode"]
        except KeyError:
            pass

    def __str__(self):
        return 'Guarantee Deal: {}; Customer: {}'.format(self.dealNumber, self.customer)

class Project(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    beneficiary = models.CharField(max_length=80, default='')
    created = models.CharField(max_length=10, default='')
    currency = models.CharField(max_length=3, default='')
    customerId = models.CharField(max_length=80, default='')
    effDate = models.CharField(max_length=10, default='')
    expDate = models.CharField(max_length=10, default='')
    loanId = models.CharField(max_length=80, default='')
    performaceId = models.CharField(max_length=80, default='')
    period = models.IntegerField(default=0)
    projectId = models.CharField(max_length=80, default='')
    warrantyId = models.CharField(max_length=80, default='')


    def __str__(self):
        return "Project ID: {} Amount: {} {}".format(self.projectId, self.currency, self.amount)


