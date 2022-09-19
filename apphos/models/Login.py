from django.db import models

class login(models.model):

    Usuario=models.CharField (primary_key=true) (max_length=10)
	Password=models.CharField (max_length=20)
	Rol=models.CharField (max_length=20)
	
