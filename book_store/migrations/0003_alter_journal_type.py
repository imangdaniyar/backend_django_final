# Generated by Django 4.0.4 on 2022-05-24 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0002_journal_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='type',
            field=models.CharField(choices=[(0, 'Bullet'), (1, 'Food'), (2, 'Travel'), (3, 'Sport')], default=0, max_length=100),
        ),
    ]
