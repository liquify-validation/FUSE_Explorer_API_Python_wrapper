from .client import Client


class Stats(Client):
    def __init__(self):
        Client.__init__(self, address='')
        self.url_dict[self.MODULE] = 'stats'

    def get_token_supply(self, contractAddress):
        self.url_dict[self.ACTION] = 'tokensupply'
        self.url_dict[self.CONTRACT_ADDRESS] = str(contractAddress)
        self.build_url()
        req = self.connect()
        return req['result']

    def get_total_ether_supply_wei(self):
        self.url_dict[self.ACTION] = 'ethsupply'
        self.build_url()
        req = self.connect()
        return req['result']

    def get_ether_last_price(self):
        self.url_dict[self.ACTION] = 'ethprice'
        self.build_url()
        req = self.connect()
        return req['result']
