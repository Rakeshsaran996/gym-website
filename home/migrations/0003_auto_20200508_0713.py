# Generated by Django 3.0.5 on 2020-05-08 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200414_0809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='State',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
        migrations.AddField(
            model_name='contact',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='City',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='First_name',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Last_name',
            field=models.CharField(max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Zip',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_no',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
