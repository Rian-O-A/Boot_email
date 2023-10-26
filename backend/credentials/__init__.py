import os
from dotenv import load_dotenv

load_dotenv()

cred = {
    "type": os.environ["FIREBASE_TYPE"],
    "project_id": os.environ["FIREBASE_PROJECT_ID"],
    "private_key_id": os.environ["FIREBASE_PRIVATE_KEY_ID"],
    "private_key": os.environ["FIREBASE_PRIVATE_KEY"].replace(r"\n", "\n"),
    "client_email": os.environ["FIREBASE_CLIENT_EMAIL"],
    "client_id": os.environ["FIREBASE_CLIENT_ID"],
    "auth_uri": os.environ["FIREBASE_AUTH_URI"],
    "token_uri": os.environ["FIREBASE_TOKEN_URI"],
    "auth_provider_x509_cert_url": os.environ["FIREBASE_AUTH_PROVIDER_X509_CERT_URL"],
    "client_x509_cert_url": os.environ["FIREBASE_CLIENT_X509_CERT_URL"],
    "universe_domain": os.environ["FIREBASE_UNIVERSE_DOMAIN"]
}

