SECRET_KEY = ("key",)
ROOT_URLCONF = ("",)
INSTALLED_APPS = ["django.contrib.auth", "django.contrib.contenttypes", "demo_app"]
MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "orm-2-sql-visualizer.middleware.new_middleware",
)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}
USE_TZ = False
