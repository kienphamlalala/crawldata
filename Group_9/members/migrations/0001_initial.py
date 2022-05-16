# Generated by Django 4.0.4 on 2022-05-03 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dt3',
            fields=[
                ('id', models.IntegerField(blank=True, db_column='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('brand', models.TextField(blank=True, db_column='Brand', null=True)),
                ('display', models.TextField(blank=True, db_column='Display', null=True)),
                ('hdh', models.TextField(blank=True, db_column='HDH', null=True)),
                ('camera_sau', models.TextField(blank=True, db_column='Camera_sau', null=True)),
                ('camera_truoc', models.TextField(blank=True, db_column='Camera_truoc', null=True)),
                ('chip', models.TextField(blank=True, db_column='Chip', null=True)),
                ('ram', models.TextField(blank=True, db_column='Ram', null=True)),
                ('rom', models.TextField(blank=True, db_column='Rom', null=True)),
                ('sim', models.TextField(blank=True, db_column='Sim', null=True)),
                ('battery', models.TextField(blank=True, db_column='Battery', null=True)),
                ('gia', models.IntegerField(blank=True, db_column='Gia', null=True)),
                ('danhgia', models.FloatField(blank=True, db_column='Danhgia', null=True)),
                ('soluong', models.IntegerField(blank=True, db_column='SoLuong', null=True)),
                ('link', models.TextField(blank=True, db_column='Link', null=True)),
                ('tenhang', models.TextField(blank=True, db_column='Tenhang', null=True)),
            ],
            options={
                'db_table': 'dt3',
                'managed': False,
            },
        ),
    ]