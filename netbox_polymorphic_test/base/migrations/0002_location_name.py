# Generated by Django 4.0.7 on 2022-08-12 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.CharField(default='Temp', max_length=200),
            preserve_default=False,
        ),
    ]