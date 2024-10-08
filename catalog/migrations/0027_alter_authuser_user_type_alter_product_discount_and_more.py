# Generated by Django 4.0.4 on 2022-05-24 08:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0026_alter_authuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Reviewer'), (3, 'Customer Manager'), (2, 'Customer'), (1, 'Product Manager')], null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='reorderlvl',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='sellingprice',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='stocks',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='supplierproduct',
            name='discount',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='supplierproduct',
            name='leadtime',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='supplierproduct',
            name='supplierprice',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
