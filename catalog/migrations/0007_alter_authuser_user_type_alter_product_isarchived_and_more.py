# Generated by Django 4.0.4 on 2022-05-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_authuser_user_type_alter_supplier_isarchived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Reviewer'), (1, 'Product Manager'), (2, 'Customer'), (3, 'Customer Manager')], null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='isarchived',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='isarchived',
            field=models.BooleanField(default=False),
        ),
    ]
