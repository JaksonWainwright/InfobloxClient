### Features

1. Get extensible Attributes  and store corresponding values in a list
2. Set extensible Attribute's values
3. Get next available IP for a certain block
4. Set a host record for an IP address
5. Remove extensible attribute values
6. Remove a host record

# Infoblox Client
## Initializing Class
Start by creating a secure_conf.py file that will include the following: 

    class infoblox_credentials:
        infoblox_pass = 'your_pass'
        infoblox_user = 'your_user'

Place this in the same directory as InfobloxClient.py

### Syntax: 

    infoblox_client = InfobloxClient()
    infoblox_client.function()


## Functions

#### Gets

`get_ext_attrs(attr_name)`

Pass the extensible attribute name into this. The name needs to be a string. The extensible attribute must be a list type. It will return all values associated with that extensible attribute as a list. 
Note that the return value's first index will always be the Ref ID. (needed for put/post's)

`def get_next_unused_ip(subnet)`

Pass subnet in as parameter. Ideally, subnet to be assigned in the conf.py file, so as to assign IP blocks to notable, human readable categories. Then use that as the subnet parameter. This function will return the object reference, and next available IP for that subnet 


------------


#### Puts
`add_ext_attr_values(self, attr_name, *args)`

Pass the extensible attribute name into the attr_name parameter. The args are going to be values to add to the extensible attribute

`remove_ext_attr_values(self, attr_name, *args)`

Pass the extensible attribute name into the attr_name parameter. The args are going to be values to remove from extensible attribute.


#### Deletes
