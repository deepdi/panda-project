from django.db import models as m
                                                                                          
                                                                                          
class Identity(m.Model):                                                                      
    id_no = m.IntegerField(primary_key = True)
    name = m.CharField(max_length = 256)                                                 
    dob = m.DateField('Date created')                                      
                                                                                          
                                                                                          
