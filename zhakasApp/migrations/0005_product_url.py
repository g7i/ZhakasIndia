# Generated by Django 2.2.1 on 2019-07-31 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhakasApp', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]