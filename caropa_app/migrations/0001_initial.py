# Generated by Django 5.0.3 on 2024-06-08 14:52

import caropa_app.models.product_by_ref
import django.db.models.deletion
import django_attachments.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_attachments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductByRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=20, validators=[caropa_app.models.product_by_ref.validate_ref])),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.ManyToManyField(related_name='products', to='caropa_app.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='caropa_app.color')),
                ('gallery', django_attachments.fields.GalleryField(on_delete=django.db.models.deletion.CASCADE, related_name='products_with_attachment', to='django_attachments.library')),
                ('ref', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='caropa_app.productbyref')),
                ('product_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='caropa_app.productdetail')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='caropa_app.size')),
            ],
        ),
    ]
