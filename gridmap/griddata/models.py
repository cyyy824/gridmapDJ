from django.db import models

# Create your models here.


class GridNode(models.Model):

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    @staticmethod
    def init_data():
        gridnodes = []

        gns = []
        for node in gridnodes:
            gns.append(GridNode(name=node)) 
        GridNode.objects.bulk_create(gns)

class GridMember(models.Model):

    name = models.CharField(max_length=24)
    mobile = models.CharField(max_length=11,blank=True)
    gridnode = models.ForeignKey(GridNode, on_delete=models.CASCADE,related_name="gridmembers")

    def __str__(self):
        return self.name+','+self.mobile

    @staticmethod
    def init_data():
        pass



class GridArea(models.Model):

    areajson = models.TextField()
    gridnode = models.OneToOneField(GridNode,on_delete=models.CASCADE, related_name='gridarea')

    def __str__(self):
        return self.areajson

    @staticmethod
    def init_data():
        pass
    
class GridSupport(models.Model):
    
    police = models.CharField(max_length=64,blank=True)
    hospital = models.CharField(max_length=64,blank=True)
    firestation = models.CharField(max_length=64,blank=True)
    subdistrict = models.CharField(max_length=128,blank=True)
    facilitie = models.IntegerField(blank=True,null=True)

    gridnode = models.OneToOneField(GridNode,on_delete=models.CASCADE, related_name='gridsupport')

    

    @staticmethod
    def init_data():
        pass