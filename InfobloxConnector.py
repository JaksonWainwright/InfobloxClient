from conf import infoblox_vars


class InfobloxConnector:
    def __init__(self):
        self.infoblox_base_url = infoblox_vars.infoblox_base_url
        self.infoblox_user = infoblox_vars.infoblox_user
        self.infoblox_password = infoblox_vars.infoblox_pass
        self.url_ip_block = infoblox_vars.infoblox_url_ip_block

    def get_ext_attrs(self, attr_name):
        return 'To do '

    def set_ext_attrs(self, attrs):
        return 'To do '

    def get_next_ip(self):
        return 'To do'

    def reserve_ip(self, ip):
        return 'To do '

    def create_host_record(self, ip):
        return 'To do'

    def remove_ext_attr(self, attr):
        return 'To do '

    def unreserve_ip(self, ip):
        return 'To do'

    def remove_host_record(self):
        return 'To do'
