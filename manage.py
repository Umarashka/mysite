#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line
    if sys.argv.__len__() == 3:
        if sys.argv[2] == '8000':
            sys.argv[2] = '0.0.0.0:8000'
    execute_from_command_line(sys.argv)
