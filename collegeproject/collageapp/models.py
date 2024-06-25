from django.db import models
class College(models.Model):
    cid=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=200)
    clocation=models.CharField(max_length=200)
    totalstudent=models.IntegerField()
    numdepartment=models.IntegerField()
    def __str__(self):
        return self.cname