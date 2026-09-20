import os
import secrets
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# کلید از محیط خوانده می‌شود؛ برای تمرین، در نبود آن تولید می‌شود.
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY") or secrets.token_urlsafe(50)

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]
CSRF_TRUSTED_ORIGINS = [
    "https://localhost:8000",
]

# آدرس پیش‌نمایش همین پروژه در Codespaces
codespace_name = os.environ.get("CODESPACE_NAME")
forwarding_domain = os.environ.get(
    "GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN",
    "app.github.dev",
)

if codespace_name:
    preview_host = f"{codespace_name}-8000.{forwarding_domain}"
    ALLOWED_HOSTS.append(preview_host)
    CSRF_TRUSTED_ORIGINS.append(f"https://{preview_host}")

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "library.apps.LibraryConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# این تکلیف از داده‌های داخل حافظه استفاده می‌کند.
DATABASES = {}

LANGUAGE_CODE = "fa"
TIME_ZONE = "Asia/Tehran"

USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"