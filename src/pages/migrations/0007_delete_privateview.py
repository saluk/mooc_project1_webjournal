# Generated by Django 5.2.1 on 2025-07-03 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_journalentry_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PrivateView',
        ),
    ]
