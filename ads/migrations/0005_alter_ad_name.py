# Generated by Django 4.0.4 on 2022-05-29 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_ad_name_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]