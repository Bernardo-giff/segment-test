import datetime
import uuid
import jwt
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Replace the example values below (remove the brackets).
# Store secrets securely based on your team's best practices.
# See: https://help.tableau.com/current/online/en-us/connected_apps_direct.htm

# Use secret_id from .env
# Use secret_value from .env
# Use client_id from .env
# Use username from .env



secretId = os.getenv('secret_id')
secretValue = os.getenv('secret_id')
clientId = os.getenv('client_id')
username = os.getenv('username')
tokenExpiryInMinutes = 10  # Max of 10 minutes.

# Remove 'tableau:views:embed_authoring' scope if Authoring is not needed.
# Remove 'tableau:insights:embed' scope if Pulse is not needed.
scopes = [
    "tableau:views:embed",
    "tableau:views:embed_authoring",
    "tableau:insights:embed",
]

kid = secretId
iss = clientId
sub = username
aud = "tableau"
exp = datetime.datetime.utcnow() + datetime.timedelta(minutes=tokenExpiryInMinutes)
jti = str(uuid.uuid4())
scp = scopes

userAttributes = {
    # User attributes are optional.
    # Add entries to this dictionary if desired.
    # "[User Attribute Name]": "[User Attribute Value]",
}

payload = {
    "iss": clientId,
    "exp": exp,
    "jti": jti,
    "aud": aud,
    "sub": sub,
    "scp": scp,
} | userAttributes


def getJwt():
    token = jwt.encode(
        payload,
        secretValue,
        algorithm="HS256",
        headers={
            "kid": kid,
            "iss": iss,
        },
    )

    return token


if __name__ == "__main__":
    token = getJwt()
    print(token)