# Generated by Django 3.1.2 on 2020-10-28 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0006_auto_20201028_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='month_bought_at',
            field=models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=9),
        ),
    ]