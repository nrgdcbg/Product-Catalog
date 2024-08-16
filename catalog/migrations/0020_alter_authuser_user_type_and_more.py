# Generated by Django 4.0.4 on 2022-05-23 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_rename_reviews_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Product Manager'), (3, 'Customer Manager'), (2, 'Customer'), (4, 'Reviewer')], null=True),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='profilepicture',
            field=models.ImageField(blank=True, default='/default_pfp.png', null=True, upload_to=''),
        ),
    ]
