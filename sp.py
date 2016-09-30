import base64
import saml2

from saml2.client import Saml2Client

logout_request = None

with open('test_files/mock_logout_request.xml') as logout_request_file:
    logout_request = logout_request_file.read()

logout_request = base64.b64encode(logout_request)

service_provider = Saml2Client(config_file='sp_conf')
logout_request = service_provider.parse_logout_request(logout_request, saml2.BINDING_HTTP_POST)
print logout_request
