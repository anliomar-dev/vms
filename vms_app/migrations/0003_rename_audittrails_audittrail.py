# Generated by Django 5.1.5 on 2025-02-24 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vms_app', '0002_alter_audittrails_action_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AuditTrails',
            new_name='AuditTrail',
        ),
    ]
