# Generated by Django 4.1.3 on 2022-11-22 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiFamilia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('parentesco', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('fecha_cumpleanios', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Familiar2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('parentesco', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('fecha_cumpleanios', models.DateField()),
            ],
        ),
    ]
