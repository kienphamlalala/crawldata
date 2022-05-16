# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Dttheohieunang(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null = False , primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    brand = models.TextField(db_column='Brand', blank=True, null=True)  # Field name made lowercase.
    display = models.TextField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    hdh = models.TextField(db_column='HDH', blank=True, null=True)  # Field name made lowercase.
    camera_sau = models.TextField(db_column='Camera_sau', blank=True, null=True)  # Field name made lowercase.
    camera_truoc = models.TextField(db_column='Camera_truoc', blank=True, null=True)  # Field name made lowercase.
    chip = models.TextField(db_column='Chip', blank=True, null=True)  # Field name made lowercase.
    ram = models.TextField(db_column='Ram', blank=True, null=True)  # Field name made lowercase.
    rom = models.TextField(db_column='Rom', blank=True, null=True)  # Field name made lowercase.
    sim = models.TextField(db_column='Sim', blank=True, null=True)  # Field name made lowercase.
    battery = models.TextField(db_column='Battery', blank=True, null=True)  # Field name made lowercase.
    gia = models.IntegerField(db_column='Gia', blank=True, null=True)  # Field name made lowercase.
    danhgia = models.IntegerField(db_column='Danhgia', blank=True, null=True)  # Field name made lowercase.
    soluong = models.IntegerField(db_column='SoLuong', blank=True, null=True)  # Field name made lowercase.
    link = models.TextField(db_column='Link', blank=True, null=True)  # Field name made lowercase.
    tencuahang = models.TextField(db_column='TenCuaHang', blank=True, null=True)  # Field name made lowercase.
    hieunang_gia = models.IntegerField(db_column='Hieunang/Gia', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'dtTheoHieuNang'
