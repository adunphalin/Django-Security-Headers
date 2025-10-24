# Django Security Headers

A lightweight Django middleware that automatically adds recommended security headers
to protect your web application with zero configuration.

## Features
- Adds security headers such as CSP, HSTS, X-Frame-Options, X-Content-Type-Options
- Configurable via Django settings
- Works with any existing Django project

## Installation
```bash
pip install django-security-headers
```

## Usage
Add the middleware to your Django settings:
```python
MIDDLEWARE = [
    ...,
    'django_security_headers.middleware.SecurityHeadersMiddleware',
]
```

## Sponsor
If this project helps you, please consider sponsoring to support development.
