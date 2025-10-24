from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

class SecurityHeadersMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['X-Frame-Options'] = getattr(settings, 'SEC_HDR_X_FRAME_OPTIONS', 'DENY')
        response['X-Content-Type-Options'] = 'nosniff'
        response['Referrer-Policy'] = getattr(settings, 'SEC_HDR_REFERRER_POLICY', 'same-origin')
        response['Strict-Transport-Security'] = getattr(settings, 'SEC_HDR_HSTS', 'max-age=31536000; includeSubDomains')
        response['Content-Security-Policy'] = getattr(settings, 'SEC_HDR_CSP', "default-src 'self'")
        return response
