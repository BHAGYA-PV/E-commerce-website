# Generated by Django 4.2.5 on 2023-09-23 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('order placed', 'order placed'), ('shipped', 'shipped'), ('out for delivery', 'out for delivery'), ('Delivered', 'Delivered'), ('cancel', 'cancel')], default='Order placed', max_length=100),
        ),
    ]
