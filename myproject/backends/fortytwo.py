from social_core.backends.oauth import BaseOAuth2

class FortyTwoOAuth2(BaseOAuth2):
    """42 API OAuth2 authentication backend"""
    name = '42'
    AUTHORIZATION_URL = 'https://api.intra.42.fr/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://api.intra.42.fr/oauth/token'
    API_URL = 'https://api.intra.42.fr/v2'
    ACCESS_TOKEN_METHOD = 'POST'
    DEFAULT_SCOPE = ['public']
    EXTRA_DATA = [
        ('id', 'id'),
        ('login', 'login'),
        ('email', 'email'),
    ]

    def get_user_details(self, response):
        """Return user details from 42 account"""
        return {
            'username': response.get('login'),
            'email': response.get('email'),
            'first_name': response.get('first_name', ''),
            'last_name': response.get('last_name', ''),
        }

    def user_data(self, access_token, *args, **kwargs):
        """Fetch user data from 42 API"""
        return self.get_json(f"{self.API_URL}/me", params={'access_token': access_token})
