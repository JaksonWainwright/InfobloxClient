import ipaddress
from secure_conf import infoblox_credentials


class infoblox_vars:
    infoblox_wapi_version = 'v2.7.3'
    infoblox_base_url = f'https://192.168.0.2/wapi/{infoblox_wapi_version}/'
    infoblox_user = infoblox_credentials.infoblox_user
    infoblox_pass = infoblox_credentials.infoblox_pass
    infoblox_url_ip_block = ipaddress.IPv4Network('199.73.119.0/24')
