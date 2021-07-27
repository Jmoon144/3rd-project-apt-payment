#from django.db                  import models
#from django.db.models.deletion  import CASCADE
#from django.db.models.fields    import CharField, DecimalField
#from django.contrib.auth.models import User
#
#class Payment(models.Model):
#    name = models.CharField(max_length=4)
#    pay  = models.DecimalField(max_digits=8, decimal_places=1, default=0)
#    user = models.ForeignKey(User, on_delete=CASCADE)
#
#    class Meta:
#        db_table = 'payment'
