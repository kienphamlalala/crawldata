# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Dt3(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null = False , primary_key=True)  # Field name made lowercase.
    
    name = models.TextField(db_column='name', blank=True, null=True)  # Field name made lowercase.
    brand = models.TextField(db_column='brand', blank=True, null=True)  # Field name made lowercase.
    display = models.TextField(db_column='display', blank=True, null=True)  # Field name made lowercase.
    hdh = models.TextField(db_column='hdh', blank=True, null=True)  # Field name made lowercase.
    camera_sau = models.TextField(db_column='camera_sau', blank=True, null=True)  # Field name made lowercase.
    camera_truoc = models.TextField(db_column='camera_truoc', blank=True, null=True)  # Field name made lowercase.
    chip = models.TextField(db_column='chip', blank=True, null=True)  # Field name made lowercase.
    ram = models.TextField(db_column='ram', blank=True, null=True)  # Field name made lowercase.
    rom = models.TextField(db_column='rom', blank=True, null=True)  # Field name made lowercase.
    sim = models.TextField(db_column='sim', blank=True, null=True)  # Field name made lowercase.
    battery = models.TextField(db_column='battery', blank=True, null=True)  # Field name made lowercase.
    gia = models.IntegerField(db_column='price', blank=True, null=True)  # Field name made lowercase.
    danhgia = models.TextField(db_column='danhgia', blank=True, null=True)  # Field name made lowercase.
    soluong = models.IntegerField(db_column='sluong', blank=True, null=True)  # Field name made lowercase.
    link = models.TextField(db_column='link', blank=True, null=True)  # Field name made lowercase.
    #tenhang = models.TextField(db_column='Tenhang', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dienthoai3'

class Dt2(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null = False , primary_key=True)  # Field name made lowercase.
    
    name = models.TextField(db_column='name', blank=True, null=True)  # Field name made lowercase.
    brand = models.TextField(db_column='brand', blank=True, null=True)  # Field name made lowercase.
    display = models.TextField(db_column='display', blank=True, null=True)  # Field name made lowercase.
    hdh = models.TextField(db_column='hdh', blank=True, null=True)  # Field name made lowercase.
    camera_sau = models.TextField(db_column='camera_sau', blank=True, null=True)  # Field name made lowercase.
    camera_truoc = models.TextField(db_column='camera_truoc', blank=True, null=True)  # Field name made lowercase.
    chip = models.TextField(db_column='chip', blank=True, null=True)  # Field name made lowercase.
    ram = models.TextField(db_column='ram', blank=True, null=True)  # Field name made lowercase.
    rom = models.TextField(db_column='rom', blank=True, null=True)  # Field name made lowercase.
    sim = models.TextField(db_column='sim', blank=True, null=True)  # Field name made lowercase.
    battery = models.TextField(db_column='battery', blank=True, null=True)  # Field name made lowercase.
    gia = models.IntegerField(db_column='price', blank=True, null=True)  # Field name made lowercase.
    danhgia = models.TextField(db_column='danhgia', blank=True, null=True)  # Field name made lowercase.
    soluong = models.IntegerField(db_column='sluong', blank=True, null=True)  # Field name made lowercase.
    link = models.TextField(db_column='link', blank=True, null=True)  # Field name made lowercase.
    #tenhang = models.TextField(db_column='Tenhang', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dienthoai2'

class Dt1(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null = False , primary_key=True)  # Field name made lowercase.
    
    name = models.TextField(db_column='name', blank=True, null=True)  # Field name made lowercase.
    brand = models.TextField(db_column='brand', blank=True, null=True)  # Field name made lowercase.
    display = models.TextField(db_column='display', blank=True, null=True)  # Field name made lowercase.
    hdh = models.TextField(db_column='hdh', blank=True, null=True)  # Field name made lowercase.
    camera_sau = models.TextField(db_column='camera_sau', blank=True, null=True)  # Field name made lowercase.
    camera_truoc = models.TextField(db_column='camera_truoc', blank=True, null=True)  # Field name made lowercase.
    chip = models.TextField(db_column='chip', blank=True, null=True)  # Field name made lowercase.
    ram = models.TextField(db_column='ram', blank=True, null=True)  # Field name made lowercase.
    rom = models.TextField(db_column='rom', blank=True, null=True)  # Field name made lowercase.
    sim = models.TextField(db_column='sim', blank=True, null=True)  # Field name made lowercase.
    battery = models.TextField(db_column='battery', blank=True, null=True)  # Field name made lowercase.
    gia = models.IntegerField(db_column='price', blank=True, null=True)  # Field name made lowercase.
    danhgia = models.TextField(db_column='danhgia', blank=True, null=True)  # Field name made lowercase.
    soluong = models.IntegerField(db_column='sluong', blank=True, null=True)  # Field name made lowercase.
    link = models.TextField(db_column='link', blank=True, null=True)  # Field name made lowercase.
    #tenhang = models.TextField(db_column='Tenhang', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dienthoai1'
class Dt4(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null = False , primary_key=True)  # Field name made lowercase.
    
    name = models.TextField(db_column='name', blank=True, null=True)  # Field name made lowercase.
    brand = models.TextField(db_column='brand', blank=True, null=True)  # Field name made lowercase.
    display = models.TextField(db_column='display', blank=True, null=True)  # Field name made lowercase.
    hdh = models.TextField(db_column='hdh', blank=True, null=True)  # Field name made lowercase.
    camera_sau = models.TextField(db_column='camera_sau', blank=True, null=True)  # Field name made lowercase.
    camera_truoc = models.TextField(db_column='camera_truoc', blank=True, null=True)  # Field name made lowercase.
    chip = models.TextField(db_column='chip', blank=True, null=True)  # Field name made lowercase.
    ram = models.TextField(db_column='ram', blank=True, null=True)  # Field name made lowercase.
    rom = models.TextField(db_column='rom', blank=True, null=True)  # Field name made lowercase.
    sim = models.TextField(db_column='sim', blank=True, null=True)  # Field name made lowercase.
    battery = models.TextField(db_column='battery', blank=True, null=True)  # Field name made lowercase.
    gia = models.IntegerField(db_column='price', blank=True, null=True)  # Field name made lowercase.
    danhgia = models.TextField(db_column='danhgia', blank=True, null=True)  # Field name made lowercase.
    soluong = models.IntegerField(db_column='sluong', blank=True, null=True)  # Field name made lowercase.
    link = models.TextField(db_column='link', blank=True, null=True)  # Field name made lowercase.
    #tenhang = models.TextField(db_column='Tenhang', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'datadaloc'

class Dt5(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null = False , primary_key=True)  # Field name made lowercase.
    
    name = models.TextField(db_column='name', blank=True, null=True)  # Field name made lowercase.
    brand = models.TextField(db_column='brand', blank=True, null=True)  # Field name made lowercase.
    display = models.TextField(db_column='display', blank=True, null=True)  # Field name made lowercase.
    hdh = models.TextField(db_column='hdh', blank=True, null=True)  # Field name made lowercase.
    camera_sau = models.TextField(db_column='camera_sau', blank=True, null=True)  # Field name made lowercase.
    camera_truoc = models.TextField(db_column='camera_truoc', blank=True, null=True)  # Field name made lowercase.
    chip = models.TextField(db_column='chip', blank=True, null=True)  # Field name made lowercase.
    ram = models.TextField(db_column='ram', blank=True, null=True)  # Field name made lowercase.
    rom = models.TextField(db_column='rom', blank=True, null=True)  # Field name made lowercase.
    sim = models.TextField(db_column='sim', blank=True, null=True)  # Field name made lowercase.
    battery = models.TextField(db_column='battery', blank=True, null=True)  # Field name made lowercase.
    gia = models.IntegerField(db_column='price', blank=True, null=True)  # Field name made lowercase.
    danhgia = models.TextField(db_column='danhgia', blank=True, null=True)  # Field name made lowercase.
    soluong = models.IntegerField(db_column='sluong', blank=True, null=True)  # Field name made lowercase.
    link = models.TextField(db_column='link', blank=True, null=True)  # Field name made lowercase.
    #tenhang = models.TextField(db_column='Tenhang', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dienthoaiall'