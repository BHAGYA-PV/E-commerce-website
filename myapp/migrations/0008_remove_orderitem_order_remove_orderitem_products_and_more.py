# Generated by Django 4.2.5 on 2023-09-23 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='products',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Orderitem',
        ),
    ]
