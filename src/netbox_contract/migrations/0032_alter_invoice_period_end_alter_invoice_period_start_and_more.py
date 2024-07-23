# Generated by Django 5.0.6 on 2024-07-23 19:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('netbox_contract', '0031_contract_invoice_template_invoice_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='period_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='period_start',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='template',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
