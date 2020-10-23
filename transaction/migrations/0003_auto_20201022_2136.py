# Generated by Django 3.1.2 on 2020-10-22 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_auto_20201022_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='currency',
        ),
        migrations.AddField(
            model_name='transaction',
            name='Current_Choice',
            field=models.CharField(choices=[('BTC', 'Bitcoin'), ('ETH', 'Ethereum'), ('LINK', 'Chainlink'), ('LTC', 'Litecoin'), ('DOT', 'Pokadot'), ('YFI', 'YearnFinance')], default='BTC', max_length=4),
        ),
    ]