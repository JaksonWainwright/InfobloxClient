import requests, json
from conf import infoblox_vars
from requests.auth import HTTPBasicAuth


class InfobloxClient:
    def __init__(self):
        self.infoblox_base_url = infoblox_vars.infoblox_base_url
        self.infoblox_user = infoblox_vars.infoblox_user
        self.infoblox_password = infoblox_vars.infoblox_pass
        self.url_ip_block = infoblox_vars.infoblox_url_ip_block

    def send_get_request(self, uri, *args):
        headers = {"Content_Type": "application/json"}
        if args:
            request = requests.get(f'{self.infoblox_base_url}{uri}', headers=headers, verify=False,
                                   auth=HTTPBasicAuth(infoblox_vars.infoblox_user,
                                                      infoblox_vars.infoblox_pass), data=args[0])
        else:
            request = requests.get(f'{self.infoblox_base_url}{uri}', verify=False,
                                   auth=HTTPBasicAuth(infoblox_vars.infoblox_user,
                                                      infoblox_vars.infoblox_pass))
        response = json.loads(request.text.strip('[]'))
        return response

    def get_ext_attrs(self, attr_name):
        ext_atrr_values = []
        data = json.dumps({"name": attr_name})
        request = self.send_get_request("extensibleattributedef?_return_fields=list_values", data)
        for list_key in request['list_values']:
            ext_atrr_values.append(list_key['value'])
        return ext_atrr_values

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

    def test_func(self):
        print(self.get_ext_attrs('Program Name'))
