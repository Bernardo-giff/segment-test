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

secret_id="379368d6-916a-43b7-abd1-93911cc71d8a"
secret_value="N892zqD5l5R5CCslTXav+BZgxpuQ8Js5OcBsGPcz8mY="
client_id="0b3f0512-e260-4f8b-9a38-16ebde2939b0"
username="bernardo.carvalho@metaloop.com"

# secretId = os.getenv('secret_id')
# secretValue = os.getenv('secret_id')
# clientId = os.getenv('client_id')
# username = os.getenv('username')

secretId = secret_id
secretValue = secret_value
clientId = client_id
username = username

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