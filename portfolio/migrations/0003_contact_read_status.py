# Generated by Django 4.2.5 on 2023-10-10 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_contact_message_envoye'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='read_status',
            field=models.BooleanField(default=False),
        ),
    ]
