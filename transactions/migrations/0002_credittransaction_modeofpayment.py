# Generated by Django 4.2.4 on 2023-12-13 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='credittransaction',
            name='modeOfPayment',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
