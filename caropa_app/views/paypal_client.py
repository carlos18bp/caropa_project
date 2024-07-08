from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment, LiveEnvironment
from django.conf import settings

class PayPalClient:
    """
    Initializes the PayPal client with the appropriate environment
    based on the settings (sandbox or live).

    Attributes:
        environment (SandboxEnvironment|LiveEnvironment): The PayPal environment (sandbox or live).
        client (PayPalHttpClient): The PayPal HTTP client initialized with the specified environment.
    """

    def __init__(self):
        """
        Initializes the PayPalClient instance.
        Chooses the environment based on the PAYPAL_MODE setting.
        """
        if settings.PAYPAL_MODE == 'sandbox':
            self.environment = SandboxEnvironment(
                client_id=settings.PAYPAL_CLIENT_ID, 
                client_secret=settings.PAYPAL_CLIENT_SECRET
            )
        else:
            self.environment = LiveEnvironment(
                client_id=settings.PAYPAL_CLIENT_ID, 
                client_secret=settings.PAYPAL_CLIENT_SECRET
            )
        self.client = PayPalHttpClient(self.environment)
