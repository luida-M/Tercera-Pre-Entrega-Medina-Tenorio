#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import io
import sys
# Configurar la codificación para stdout y stderr 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') 
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import os 
import django 
from django.core.management import execute_from_command_line

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try: 
       execute_from_command_line(sys.argv) 
    except ImportError as exc: 
        raise ImportError( 
            "Couldn't import Django. Are you sure it's installed and " 
            "available on your PYTHONPATH environment variable? Did you " 
            "forget to activate a virtual environment?" 
        ) from exc
    
if __name__ == '__main__':
    main()
