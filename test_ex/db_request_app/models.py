from django.db import models


class Requisite(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    payment_type = models.CharField(max_length=50)
    account_type = models.CharField(max_length=50)
    limit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'ID: {self.id}, User: {self.name} {self.surname} {self.patronymic}, \nPhone: {self.phone},\n ' \
               f'Payment type: {self.payment_type}, \nAccount type: {self.account_type}, \nLimit: {self.limit}'


class Order(models.Model):
    summ = models.DecimalField(max_digits=10, decimal_places=2)
    requisite = models.ForeignKey(Requisite, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)

    def __str__(self):
        return f'ID: {self.id}, \nSumm: {self.summ}, \nRequisites: {self.requisite}, \nStatus: {self.status}'
