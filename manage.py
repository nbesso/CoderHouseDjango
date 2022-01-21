#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Proyecto1.settings')
    try:
        from django.core.management import execute_from_command_line
        print("Este es un conflicto")
        print("Comentarios Conflicots")
        hola = "Commentario"
        variable = "Variable 2"
        variable2 = "Variable 3"
        print("Este es un conflicto para la segunda prueba")
        print("Este es un conflicto para la segunda prueba")
        print("Este es un conflicto para la segunda prueba")
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Este no debe ser un problema para de conflicto
    main()
