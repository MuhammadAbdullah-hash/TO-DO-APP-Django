# Generated by Django 3.1.4 on 2021-01-02 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_items_data_done'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items_data',
            old_name='done',
            new_name='is_done',
        ),
        migrations.AlterField(
            model_name='items_data',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
