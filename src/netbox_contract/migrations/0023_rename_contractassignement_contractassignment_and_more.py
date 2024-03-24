# Generated by Django 4.2.10 on 2024-03-24 11:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('extras', '0107_cachedvalue_extras_cachedvalue_object'),
        ('contenttypes', '0002_remove_content_type_name'),
        (
            'netbox_contract',
            '0022_alter_contract_internal_partie_alter_contract_parent',
        ),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContractAssignement',
            new_name='ContractAssignment',
        ),
        migrations.RenameIndex(
            model_name='contractassignment',
            new_name='netbox_cont_content_3bf04f_idx',
            old_name='netbox_cont_content_ff787b_idx',
        ),
    ]
