from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-secret-key"

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",

    "apps.accounts",
    "apps.customers",
    "apps.radios",
    "apps.rentals",
    "apps.payments",
    "apps.repeaters",
    "apps.frequencies",
    "apps.alerts",
    "apps.reports",
]