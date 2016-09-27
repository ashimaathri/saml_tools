import os
import saml2

from saml2.metadata import create_metadata_string

entity_id = 'https://sp-test.rackspace.com'
path = os.path.dirname(os.path.abspath(__file__))

metadata = create_metadata_string(path + "/sp_conf.py",
                                  None,
                                  4,
                                  path + "/pki/sp.crt",
                                  path + "/pki/sp.key",
                                  entity_id,
                                  None,
                                  True)
print metadata
