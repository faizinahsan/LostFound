# Generated by Django 2.1.2 on 2018-11-13 02:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('udpdateDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(default='imgProfileDefault.jpg', upload_to='profile_pics')),
                ('phone', models.CharField(max_length=13)),
                ('line', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
