# Generated by Django 5.1.7 on 2025-03-15 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='low_stock_threshold',
            field=models.PositiveBigIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='stock_level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
