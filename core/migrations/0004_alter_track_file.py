# Generated by Django 3.2.9 on 2022-01-25 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_track_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='file',
            field=models.FileField(help_text='Track file', upload_to='core/static/audio'),
        ),
    ]
