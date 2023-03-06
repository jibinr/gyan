from django.db import models

class Table1(models.Model):
    field1= models.CharField(max_length=100)
    field2 =models.CharField(max_length=100)
    field3 = models.CharField(max_length=100)

class Table2(models.Model):
    field1= models.CharField(max_length=100)
    field2= models.CharField(max_length=100)
    table1_fk = models.ForeignKey(Table1, on_delete=models.CASCADE, related_name='table2_records')
