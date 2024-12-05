from flask import request, Response

def auth_middleware(app):
    @app.before_request
    def require_auth():
        if request.path not in ['/login', '/favicon.ico']:  # Allow specific paths
            auth = request.authorization
            if not auth or auth.username != 'user' or auth.password != 'password':
                return Response(
                    'Authentication required', 401,
                    {'WWW-Authenticate': 'Basic realm="Login Required"'}
                )
