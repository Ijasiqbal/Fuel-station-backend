# Generated by Django 4.2.4 on 2024-08-20 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading', '0012_alter_reading_card_alter_reading_cash_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reading',
            old_name='closingD',
            new_name='closingNozzle1',
        ),
        migrations.RenameField(
            model_name='reading',
            old_name='closingP',
            new_name='closingNozzle2',
        ),
        migrations.RenameField(
            model_name='reading',
            old_name='openingD',
            new_name='closingNozzle3',
        ),
        migrations.RenameField(
            model_name='reading',
            old_name='openingP',
            new_name='closingNozzle4',
        ),
        migrations.RemoveField(
            model_name='reading',
            name='nossle',
        ),
        migrations.AddField(
            model_name='reading',
            name='nossle3and4',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='reading',
            name='nozzle1and2',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='reading',
            name='nozzle3and4',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='reading',
            name='openingNozzle1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='reading',
            name='openingNozzle2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='reading',
            name='openingNozzle3',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='reading',
            name='openingNozzle4',
            field=models.FloatField(null=True),
        ),
    ]