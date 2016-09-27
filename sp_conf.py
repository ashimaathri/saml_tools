import os

from saml2 import BINDING_HTTP_POST, BINDING_HTTP_REDIRECT
from saml2.saml import NAME_FORMAT_URI

try:
    from saml2.sigver import get_xmlsec_binary
except ImportError:
    get_xmlsec_binary = None


if get_xmlsec_binary:
    xmlsec_path = get_xmlsec_binary(['/opt/local/bin', '/usr/local/bin'])
else:
    xmlsec_path = '/usr/local/bin/xmlsec1'

# Make sure the same port number appear in service_conf.py
BASEDIR = os.path.abspath(os.path.dirname(__file__))
BASE = 'https://sp-url.rackspace.com'


SSL_CERT_LOCATION = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pki')
CERT = os.path.join(SSL_CERT_LOCATION, 'sp.crt')
IDP_METADATA_LOCATION = os.getenv('IDP_METADATA_LOCATION',
                                  os.path.join(SSL_CERT_LOCATION,
                                               'idp_metadata.xml'))
PRIVATE_KEY = os.path.join(SSL_CERT_LOCATION, 'sp.key')

CONFIG = {
    'entityid': BASE,
    'service': {
        'sp': {
            'authn_requests_signed': True,
            'logout_requests_signed': True,
            'allow_unsolicited': True,
            'endpoints': {
                'assertion_consumer_service': [
                    ('%s/acs' % BASE, BINDING_HTTP_POST)
                ],
                'single_logout_service': [
                    ('%s/slo/redirect' % BASE, BINDING_HTTP_REDIRECT),
                    ('%s/slo/post' % BASE, BINDING_HTTP_POST),
                ]
            }
        }
    },
    'metadata': {
        'local': [IDP_METADATA_LOCATION]
    },
    # Allows for multiple certs in the metadata - just here to demonstrate
    # a solution to cert rotation
    # 'additional_cert_files': ['/data/astra/alt_sso_cert'],
    'key_file': PRIVATE_KEY,
    'cert_file': CERT,
    'xmlsec_binary': xmlsec_path,
    'name_form': NAME_FORMAT_URI
}
