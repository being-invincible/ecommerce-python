#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djecommerce.settings.development')
    try:
        from django.core.management import execute_from_command_line
        from django.core.management.commands.runserver import Command as runserver
        runserver.default_port = "9000"
    except ImportError as exc:
        raise ImportError(
            "Error is starting Django APP"
        ) from exc
    execute_from_command_line(sys.argv)
