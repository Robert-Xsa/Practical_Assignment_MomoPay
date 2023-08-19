# Generated by Django 4.2.4 on 2023-08-19 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('NAME', models.CharField(max_length=20)),
                ('CONTACT_NUMBER', models.CharField(max_length=10)),
                ('ADDRESS', models.CharField(max_length=100)),
                ('DOCTOR_NAME', models.CharField(max_length=20)),
                ('DOCTOR_ADDRESS', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('INVOICE_ID', models.AutoField(primary_key=True, serialize=False)),
                ('NET_TOTAL', models.FloatField(default=0)),
                ('INVOICE_DATE', models.DateField(auto_now_add=True)),
                ('CUSTOMER_ID', models.IntegerField()),
                ('TOTAL_AMOUNT', models.FloatField()),
                ('TOTAL_DISCOUNT', models.FloatField()),
            ],
            options={
                'db_table': 'invoices',
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('NAME', models.CharField(max_length=100)),
                ('PACKING', models.CharField(max_length=20)),
                ('GENERIC_NAME', models.CharField(max_length=100)),
                ('SUPPLIER_NAME', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'medicines',
            },
        ),
        migrations.CreateModel(
            name='MedicineStock',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('NAME', models.CharField(max_length=100)),
                ('BATCH_ID', models.CharField(max_length=20, unique=True)),
                ('EXPIRY_DATE', models.CharField(max_length=10)),
                ('QUANTITY', models.IntegerField()),
                ('MRP', models.FloatField()),
                ('RATE', models.FloatField()),
            ],
            options={
                'db_table': 'medicines_stock',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('NAME', models.CharField(max_length=100)),
                ('EMAIL', models.EmailField(max_length=254)),
                ('CONTACT_NUMBER', models.CharField(max_length=10)),
                ('ADDRESS', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'suppliers',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('VOUCHER_NUMBER', models.AutoField(primary_key=True, serialize=False)),
                ('INVOICE_NUMBER', models.IntegerField()),
                ('PURCHASE_DATE', models.DateField()),
                ('TOTAL_AMOUNT', models.FloatField()),
                ('PAYMENT_STATUS', models.CharField(choices=[('C', 'Completed'), ('N', 'Not Completed')], max_length=20)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchases.customer', verbose_name='CUSTOMER NAME')),
                ('Supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchases.supplier', verbose_name='SUPPLIER NAME')),
                ('medicines', models.ManyToManyField(to='purchases.medicinestock')),
            ],
            options={
                'db_table': 'purchases',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='Supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchases.supplier', verbose_name='SUPPLIER NAME'),
        ),
    ]
