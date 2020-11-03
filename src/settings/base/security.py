import os

SECRET_KEY = '3@2pg_7vw)mbg65dpu!5or&#xt=54dyjc-#**hd=d+&5y#g^e('

HOSTNAME = os.environ.get('BACKEND_HOSTNAME', '127.0.0.1')

ALLOWED_HOSTS = [
    HOSTNAME,
    os.environ.get('POD_IP')
]

CORS_ORIGIN_WHITELIST = [
    '{}://{}'.format(
        os.environ.get('FRONTEND_PROTOCOL', 'http'),
        os.environ.get('FRONTEND_HOSTNAME', 'localhost:3000')
    ),
]
