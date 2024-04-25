from django.db import models

# Create your models here.


class tblservice(models.Model):
    carservicename=models.CharField(max_length=10,null=True)
    servicedetails=models.CharField(max_length=10,null=True)
    servicedescription=models.CharField(max_length=10,null=True)
    servicetime=models.CharField(max_length=10,null=True)
    serviceamount=models.CharField(max_length=10,null=True)
class tblbooking(models.Model):
    firstname=models.CharField(max_length=10,null=True)
    lastname=models.CharField(max_length=10,null=True)
    address=models.CharField(max_length=10,null=True)
    service=models.ForeignKey(tblservice,null=True,on_delete=models.CASCADE)
    email=models.CharField(max_length=10,null=True)
    contactno=models.CharField(max_length=10,null=True)








class tbltechnician(models.Model):
    technicianname=models.CharField(max_length=10,null=True)
    staffnumber=models.IntegerField(null=True)
    staffexperience=models.CharField(max_length=10,null=True)
    staffdutytime=models.CharField(max_length=10,null=True)
    staffcode=models.CharField(max_length=10,null=True)
    staffamount=models.CharField(max_length=10,null=True)
    zip=models.IntegerField(null=True)




# Create your models here.
class tblbooking(models.Model):
    name=models.CharField(max_length=10,null=True)
    number=models.IntegerField(null=True)
    address=models.CharField(max_length=10,null=True)
    carname=models.CharField(max_length=10,null=True)
    carissue=models.CharField(max_length=10,null=True)
    service=models.CharField(max_length=10,null=True)
    bill=models.CharField(max_length=10,null=True)
