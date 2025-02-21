# Generated by Django 5.1.5 on 2025-02-21 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vms_app', '0029_alter_redemption_till_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucherrequest',
            name='request_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20),
        ),
    ]
