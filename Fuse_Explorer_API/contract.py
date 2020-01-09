from .client import Client


class Contract(Client):
    def __init__(self, address=Client.seed_addr):
        Client.__init__(self, address=address)
        self.url_dict[self.MODULE] = 'contract'

    def get_list_contracts(self):
        self.url_dict[self.ACTION] = 'listcontracts'
        self.build_url()
        req = self.connect()
        return req['result']

    def get_abi(self, address):
        self.url_dict[self.ACTION] = 'getabi'
        self.url_dict[self.ADDRESS] = str(address)
        self.build_url()
        req = self.connect()
        # explicitly reset it here since some contract calls don't use it
        self.url_dict[self.ADDRESS] = ''
        return req['result']

    def get_sourcecode(self, address):
        self.url_dict[self.ACTION] = 'getsourcecode'
        self.url_dict[self.ADDRESS] = str(address)
        self.build_url()
        req = self.connect()
        # explicitly reset it here since some contract calls don't use it
        self.url_dict[self.ADDRESS] = ''
        return req['result']

    def verify(self, addressHash, name, compilerVersion, optimization, contractSourceCode):
        self.url_dict[self.ACTION] = 'verify'
        self.url_dict[self.ADDRESS_HASH] = str(addressHash)
        self.url_dict[self.NAME] = str(name)
        self.url_dict[self.COMPILER_VERSION] = str(compilerVersion)
        self.url_dict[self.OPTIMIZATION] = str(optimization)
        self.url_dict[self.contractSourceCode] = str(contractSourceCode)
        self.build_url()
        req = self.connect()
        return req['result']
