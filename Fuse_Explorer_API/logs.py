from .client import Client

class Logs(Client):
    def __init__(self, address=Client.seed_addr):
        Client.__init__(self, address=address)
        self.url_dict[self.MODULE] = 'logs'

    def get_logs(self, from_block, toBlock, topic0):
        self.url_dict[self.ACTION] = 'getLogs'
        self.url_dict[self.FROM_BLOCK] = str(from_block)
        self.url_dict[self.TO_BLOCK] = str(toBlock)
        self.url_dict[self.TOPIC_ZERO] = str(topic0)
        self.build_url()
        req = self.connect()
        return req['result']

