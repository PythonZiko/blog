# Generated by Django 4.2.7 on 2023-12-06 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_options_blog_avtor_alter_blog_rasm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='rasm',
            field=models.ImageField(blank=True, help_text='Maqola uchun rasm', null=True, upload_to='blog_rasmlari/'),
        ),
    ]