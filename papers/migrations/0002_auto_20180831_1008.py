# Generated by Django 2.1 on 2018-08-31 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='PaperPDF',
            field=models.FileField(default=' ', upload_to='PaperFolder/'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='PeerPDF',
            field=models.FileField(default=' ', upload_to='PeerFolder/'),
        ),
    ]
