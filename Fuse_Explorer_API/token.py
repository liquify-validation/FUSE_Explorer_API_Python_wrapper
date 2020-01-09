from .client import Client


class Token(Client):
    def __init__(self):
        Client.__init__(self, address='')

        self.url_dict[self.MODULE] = 'token'

    def get_token(self, contract_address):
        self.url_dict[self.ACTION] = 'getToken'
        self.url_dict[self.CONTRACT_ADDRESS] = str(contract_address)
        self.build_url()
        req = self.connect()
        return req['result']
