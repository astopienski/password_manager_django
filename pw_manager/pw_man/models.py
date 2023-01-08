from django.db import models


class Databases(models.Model):
    db_id = models.AutoField(primary_key=True)
    db_name = models.CharField(unique=True, max_length=100)
    user = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'databases'


class Passwords(models.Model):
    pw_id = models.AutoField(primary_key=True)
    db = models.ForeignKey(Databases, on_delete=models.RESTRICT)
    pw_username = models.CharField(max_length=32)
    pw_password = models.CharField(max_length=64)
    pw_link = models.CharField(max_length=256)
    pw_note = models.CharField(max_length=128)

    class Meta:
        managed = True
        db_table = 'passwords'


