# Generated by Django 4.0.4 on 2022-05-08 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dttheodanhgia',
            fields=[
                ('id', models.IntegerField(blank=True, db_column='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('brand', models.TextField(blank=True, db_column='Brand', null=True)),
                ('gia', models.IntegerField(blank=True, db_column='Gia', null=True)),
                ('danhgia', models.IntegerField(blank=True, db_column='Danhgia', null=True)),
                ('soluong', models.IntegerField(blank=True, db_column='SoLuong', null=True)),
                ('tencuahang', models.TextField(blank=True, db_column='TenCuaHang', null=True)),
                ('link', models.TextField(blank=True, db_column='Link', null=True)),
            ],
            options={
                'db_table': 'dtTheoDanhGia',
                'managed': False,
            },
        ),
    ]