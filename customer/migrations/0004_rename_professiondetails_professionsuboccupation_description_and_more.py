# Generated by Django 4.1.3 on 2022-12-08 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_personalprofile_country'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProfessionDetails',
            new_name='ProfessionsubOccupation_Description',
        ),
        migrations.RenameField(
            model_name='profession',
            old_name='professionName',
            new_name='subOccupation_Description',
        ),
        migrations.RenameField(
            model_name='professionsuboccupation_description',
            old_name='detailsName',
            new_name='ProfessionsubOccupation_Description',
        ),
        migrations.AddField(
            model_name='profession',
            name='Occupation_Description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
