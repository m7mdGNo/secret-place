# Generated by Django 3.2.5 on 2021-07-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
