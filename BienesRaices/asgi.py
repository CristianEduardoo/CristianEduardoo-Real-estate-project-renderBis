import os
# import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

# Un Middleware de autenticación
from channels.auth import AuthMiddlewareStack
import chat.routing


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BienesRaices.settings")

# Asegúrate de que las aplicaciones de Django estén completamente cargadas
# django.setup()

# application = get_asgi_application()
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(URLRouter(chat.routing.websocket_urlpatterns)),
    }
)