# Generated by Django 5.0.4 on 2024-04-26 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['-name'], 'verbose_name': 'Publisher', 'verbose_name_plural': 'Publishers'},
        ),
    ]
