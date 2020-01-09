from .client import Client

class Account(Client):
    def __init__(self, address=Client.seed_addr):
        Client.__init__(self, address=address)
        self.url_dict[self.MODULE] = 'account'

    def get_eth_balance(self, block='blocks'):
        self.url_dict[self.ACTION] = 'eth_get_balance'
        self.build_url()
        req = self.connect()
        return req['result']

    def get_balance(self):
        self.url_dict[self.ACTION] = 'balance'
        self.build_url()
        req = self.connect()
        return req['result']

    def get_balance_multiple(self):
        self.url_dict[self.ACTION] = 'balancemulti'
        self.build_url()
        req = self.connect()
        return req['result']

    def get_tx_list(self, page=1, offset=10000, sort='asc') -> list:
        self.url_dict[self.ACTION] = 'txlist'
        self.url_dict[self.PAGE] = str(page)
        self.url_dict[self.OFFSET] = str(offset)
        self.url_dict[self.SORT] = sort
        self.build_url()
        req = self.connect()
        return req['result']

    def get_tx_list_internal(self, page=1, offset=10000, sort='asc') -> list:
        self.url_dict[self.ACTION] = 'txlistinternal'
        self.url_dict[self.PAGE] = str(page)
        self.url_dict[self.OFFSET] = str(offset)
        self.url_dict[self.SORT] = sort
        self.build_url()
        req = self.connect()
        return req['result']

    def get_tx_list_token(self, page=1, offset=10000, sort='asc') -> list:
        self.url_dict[self.ACTION] = 'tokentx'
        self.url_dict[self.PAGE] = str(page)
        self.url_dict[self.OFFSET] = str(offset)
        self.url_dict[self.SORT] = sort
        self.build_url()
        req = self.connect()
        return req['result']

    def get_blocks_mined_page(self, page=1,
                              offset=10000) -> list:
        self.url_dict[self.ACTION] = 'getminedblocks'
        self.url_dict[self.PAGE] = str(page)
        self.url_dict[self.OFFSET] = str(offset)
        self.build_url()
        req = self.connect()
        return req['result']

    def get_list_of_accounts(self, page=1, offset=10000) -> list:
        self.url_dict[self.ACTION] = 'listaccounts'
        self.url_dict[self.PAGE] = str(page)
        self.url_dict[self.OFFSET] = str(offset)
        self.build_url()
        req = self.connect()
        return req['result']
