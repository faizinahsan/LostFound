# Generated by Django 2.1.2 on 2018-12-08 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181203_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='imgBlogDefault.jpg', upload_to='image_blog'),
        ),
    ]
