import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpiringToken',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('key', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Key')),
                ('expires', models.DateTimeField(verbose_name='Expires in')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_token',
                                              to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'db_table': 'expiring_authtoken',
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
                'abstract': False,
            },
        ),
    ]
