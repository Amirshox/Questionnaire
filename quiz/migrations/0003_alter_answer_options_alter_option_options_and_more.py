# Generated by Django 4.0.1 on 2022-01-15 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ('created_date',)},
        ),
        migrations.AlterModelOptions(
            name='option',
            options={'ordering': ('created_date',)},
        ),
        migrations.AlterModelOptions(
            name='poll',
            options={'ordering': ('-modified_date',)},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('created_date',)},
        ),
    ]
