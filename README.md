### Features

1. Get extensible Attributes  and store corresponding values in a list
2. Set extensible Attributes
3. Get next available IP for a certain block
4. Set a host record for an IP address
5. Reserve an IP address
6. Remove an extensible attribute
7. Unreserve and IP address
8. Remove a host record

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

`get_ext_attrs(self, attr_name)`

Pass the extensible attribute name into this. The extensible attribute must be a list type. It will return all values associated with that extensible attribute

------------


#### Puts
`add_ext_attr_values(self, attr_name, *args)`

Pass the extensible attribute name into the attr_name parameter. The args are going to be values to add to the extensible attribute