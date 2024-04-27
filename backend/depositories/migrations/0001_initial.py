# Generated by Django 5.0.4 on 2024-04-27 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0002_alter_book_options_rename_author_id_book_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('location', models.CharField(max_length=125)),
                ('capacity', models.PositiveIntegerField()),
                ('current_capacity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BookDepository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('depository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='depositories.depository')),
            ],
            options={
                'unique_together': {('book', 'depository')},
            },
        ),
    ]