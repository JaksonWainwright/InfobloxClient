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
        self.http_auth = HTTPBasicAuth(infoblox_vars.infoblox_user, infoblox_vars.infoblox_pass)

    def send_get_request(self, uri, *args):
        if args:
            request = requests.get(f'{self.infoblox_base_url}{uri}', headers=self.headers, verify=False,
                                   auth=self.http_auth, data=args[0])
        else:
            request = requests.get(f'{self.infoblox_base_url}{uri}', headers=self.headers, verify=False,
                                   auth=self.http_auth)
        response = json.loads(request.text.strip('[]'))
        return response

    def send_put_request(self, uri, data):
        request = requests.put(f'{self.infoblox_base_url}{uri}', headers=self.headers, verify=False,
                               auth=self.http_auth, data=data)
        return request.text

    def send_post_request(self, uri, data):
        request = requests.post(f'{self.infoblox_base_url}{uri}', headers=self.headers, verify=False,
                                auth=self.http_auth, data=data)
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
            "list_values": []

        }
        for value in self.return_ext_attr_values(attr_name):
            put_dict["list_values"].append({"value": value})
        for arg in args:
            if {"value": arg} not in put_dict["list_values"]:
                put_dict["list_values"].append({"value": arg})
        put_dict = str(put_dict).replace("\'", "\"")
        uri = self.return_ext_attr_ref(attr_name)
        return self.send_put_request(uri, put_dict)

    def get_all_unused_ips(self, subnet):
        return_list = []
        uri = f'ipv4address?network={subnet}&status=UNUSED&_return_as_object=1'
        for key in self.send_get_request(uri)['result']:
            return_list.append({key['_ref']: key['ip_address']})
        return return_list

    def get_next_unused_ip(self, subnet):
        unused_ips = self.get_all_unused_ips(subnet)
        return unused_ips[0]

    def create_host_record(self, subnet, host):
        post_data = {
            "name": host,
            "configure_for_dns": False,
            "ipv4addrs": [
                {
                    "ipv4addr": f"func:nextavailableip:{subnet}"
                }
            ]
        }
        return self.send_post_request('record:host', json.dumps(post_data))

    def return_ext_attr_dict(self, attr_name):
        attr_value_list = self.return_ext_attr_values(attr_name)
        value_dict = {
            "name": attr_name,
            "type": "ENUM",
            "list_values": []

        }
        for value in attr_value_list:
            value_dict['list_values'].append({"value": value})
        value_dict = str(value_dict).replace("\'", "\"")
        uri = self.return_ext_attr_ref(attr_name)
        return value_dict, uri

    def remove_ext_attr_values(self, attr_name, *args):
        existing_values = json.loads(self.return_ext_attr_dict(attr_name)[0])
        ext_attr_ref_id = self.return_ext_attr_dict(attr_name)[1]
        for index, value in enumerate(existing_values['list_values']):
            for arg in args:
                if arg == existing_values['list_values'][index]['value']:
                    del existing_values["list_values"][index]
        existing_values = str(existing_values).replace("\'", "\"")
        return self.send_put_request(ext_attr_ref_id, existing_values)


    def unreserve_ip(self, ip):
        return 'To do'

    def remove_host_record(self):
        return 'To do'

    def test_func(self):
        print(self.remove_ext_attr_values('Program Name', 'test2', 'test3', 'test4', 'test5', 'test7'))
