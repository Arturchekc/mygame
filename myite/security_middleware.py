from django.utils.deprecation import MiddlewareMixin

class SecurityHeadersMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        response['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; object-src 'none'"
        response['X-Frame-Options'] = 'SAMEORIGIN'
        response['X-Content-Type-Options'] = 'nosniff'
        response['Referrer-Policy'] = 'no-referrer-when-downgrade'
        response['Permissions-Policy'] = 'geolocation=(), camera=(), microphone=()'
        return response
