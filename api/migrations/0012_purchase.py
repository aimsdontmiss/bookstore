# Generated by Django 4.2.6 on 2024-01-12 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_delete_purchase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_items', models.JSONField(blank=True, default=list, verbose_name='PurchaseItems')),
                ('charge_id', models.CharField(max_length=360, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.customer')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.order')),
            ],
        ),
    ]