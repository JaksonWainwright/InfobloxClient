import requests, json
from conf import infoblox_vars
from requests.auth import HTTPBasicAuth


class InfobloxClient:
    def __init__(self):
        self.infoblox_base_url = infoblox_vars.infoblox_base_url
        self.infoblox_user = infoblox_vars.infoblox_user
        self.infoblox_password = infoblox_vars.infoblox_pass
        self.url_ip_block = infoblox_vars.infoblox_url_ip_block
        self.headers = {"Content_Type": "application/json"}

    def send_get_request(self, uri, *args):
        if args:
            request = requests.get(f'{self.infoblox_base_url}{uri}', headers=self.headers, verify=False,
                                   auth=HTTPBasicAuth(infoblox_vars.infoblox_user,
                                                      infoblox_vars.infoblox_pass), data=args[0])
        else:
            request = requests.get(f'{self.infoblox_base_url}{uri}', headers=self.headers, verify=False,
                                   auth=HTTPBasicAuth(infoblox_vars.infoblox_user,
                                                      infoblox_vars.infoblox_pass))
        response = json.loads(request.text.strip('[]'))
        return response

    def send_put_request(self, uri, data):
        request = requests.put(f'{self.infoblox_base_url}{uri}', headers=self.headers, verify=False,
                               auth=HTTPBasicAuth(infoblox_vars.infoblox_user,
                                                  infoblox_vars.infoblox_pass), data=data)
        return request.text

    def get_ext_attr(self, attr_name):
        ext_atrr_values = []
        data = json.dumps({"name": attr_name})
        request = self.send_get_request("extensibleattributedef?_return_fields=list_values", data)
        ext_atrr_values.append(request['_ref'])
        for list_key in request['list_values']:
            ext_atrr_values.append(list_key['value'])
        return ext_atrr_values

    def return_ext_attr_values(self, attr_name):
        return self.get_ext_attr(attr_name)[1:]

    def return_ext_attr_ref(self, attr_name):
        return self.get_ext_attr(attr_name)[0]

    def add_ext_attr_values(self, attr_name, *args):
        put_dict = {
            "name": attr_name,
            "type": "ENUM",
            "list_values":[

            ]

        }
        for value in self.return_ext_attr_values(attr_name):
            put_dict["list_values"].append({"value": value})
        for arg in args:
            if {"value": arg} not in put_dict["list_values"]:
                put_dict["list_values"].append({"value": arg})
        put_dict = str(put_dict).replace("\'", "\"")
        uri = self.return_ext_attr_ref(attr_name)
        return self.send_put_request(uri, put_dict)

    def get_unused_ips(self, subnet):
        return_list = []
        uri = f'ipv4address?network={subnet}&status=UNUSED&_return_as_object=1'
        for key in self.send_get_request(uri)['result']:
            return_list.append({key['_ref']: key['ip_address']})
        return return_list

    def get_next_unused_ip(self, subnet):
        unused_ips = self.get_unused_ips(subnet)
        return unused_ips[0]

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
        print(self.get_next_unused_ip(infoblox_vars.infoblox_url_ip_block))
