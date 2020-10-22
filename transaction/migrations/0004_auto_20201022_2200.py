# Generated by Django 3.1.2 on 2020-10-22 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_auto_20201022_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='Current_Choice',
        ),
        migrations.AddField(
            model_name='transaction',
            name='currency',
            field=models.CharField(choices=[('bitcoin', 'Bitcoin'), ('ethereum', 'Ethereum'), ('chainlink', 'Chainlink'), ('litecoin', 'Litecoin'), ('pokadot', 'Pokadot'), ('yearnfinance', 'YearnFinance')], default='bitcoin', max_length=12),
        ),
    ]
