from django.db import migrations


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("app2", "0001"),
    ]

    run_before = [
        ("app2", "0002"),
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop),
    ]
