from .client import Client


class Transactions(Client):
    def __init__(self):
        Client.__init__(self, address='')
        self.url_dict[self.MODULE] = 'transaction'

    def get_tx_info(self, tx_hash):
        self.url_dict[self.ACTION] = 'gettxinfo'
        self.url_dict[self.TXHASH] = str(tx_hash)
        self.build_url()
        req = self.connect()
        return req['result']

    def get_status(self, tx_hash):
        self.url_dict[self.ACTION] = 'getstatus'
        self.url_dict[self.TXHASH] = str(tx_hash)
        self.build_url()
        req = self.connect()
        return req['result']

    def get_tx_receipt_status(self, tx_hash):
        self.url_dict[self.ACTION] = 'gettxreceiptstatus'
        self.url_dict[self.TXHASH] = str(tx_hash)
        self.build_url()
        req = self.connect()
        return req['result']
