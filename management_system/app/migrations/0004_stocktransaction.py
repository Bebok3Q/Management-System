# Generated by Django 5.1.7 on 2025-03-15 19:19

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_inventory_low_stock_threshold_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('restock', 'Restock'), ('sale', 'Sale'), ('adjustment', 'Manual Adjustment')], max_length=20)),
                ('quantity', models.IntegerField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='app.product')),
            ],
        ),
    ]
