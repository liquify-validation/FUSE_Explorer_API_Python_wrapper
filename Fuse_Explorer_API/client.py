# coding: utf-8
import collections

import requests


class ClientException(Exception):
    """Unhandled API client exception"""
    message = 'unhandled error'

    def __init__(self, message=None):
        if message is not None:
            self.message = message

    def __unicode__(self):
        return u'<Err: {0.message}>'.format(self)

    __str__ = __unicode__


class ConnectionRefused(ClientException):
    """Connection refused by remote host"""


class EmptyResponse(ClientException):
    """Empty response from API"""


class BadRequest(ClientException):
    """Invalid request passed"""

class Client(object):
    seed_addr = ''

    # Constants
    PREFIX = 'https://explorer.fuse.io/api?'
    MODULE = 'module='
    ACTION = '&action='
    CONTRACT_ADDRESS = '&contractaddress='
    ADDRESS = '&address='
    OFFSET = '&offset='
    PAGE = '&page='
    SORT = '&sort='
    BLOCK_TYPE = '&blocktype='
    START_BLOCK = '&startblock='
    END_BLOCK = '&endblock='
    BLOCKNO = '&blockno='
    TXHASH = '&txhash='
    INDEX = '&index='
    ADDRESS_HASH = '&addressHash='
    NAME = '&name='
    COMPILER_VERSION = '&compilerVersion='
    OPTIMIZATION = '&optimization='
    CONTRACT_SOURCE_CODE = '&contractSourceCode='
    TOPIC_ZERO = '&topic0='
    FROM_BLOCK = '&fromBlock='
    TO_BLOCK = '&toBlock='

    url_dict = {}

    def __init__(self, address):
        self.http = requests.session()
        self.url_dict = collections.OrderedDict([
            (self.MODULE, ''),
            (self.ADDRESS, ''),
            (self.OFFSET, ''),
            (self.PAGE, ''),
            (self.SORT, ''),
            (self.BLOCK_TYPE, ''),
            (self.START_BLOCK, ''),
            (self.END_BLOCK, ''),
            (self.BLOCKNO, ''),
            (self.TXHASH, ''),
            (self.INDEX, ''),
            (self.ADDRESS_HASH, ''),
            (self.NAME, ''),
            (self.COMPILER_VERSION, ''),
            (self.OPTIMIZATION, ''),
            (self.CONTRACT_SOURCE_CODE , ''),
            (self.TOPIC_ZERO , ''),
            (self.FROM_BLOCK , ''),
            (self.TO_BLOCK , '')])

        self.url = None

        if (type(address) == list):
            self.url_dict[self.ADDRESS] = ','.join(address)
        else:
            self.url_dict[self.ADDRESS] = address

    def build_url(self):
        self.url = self.PREFIX + ''.join(
            [param + val if val else '' for param, val in
             self.url_dict.items()])

    def clear_url(self):
        #get the URL back into a clean state, don't touch address or module
        for key in self.url_dict:
            if key != self.MODULE and key != self.ADDRESS:
                self.url_dict[key] = ''

    def connect(self):
        try:
            req = self.http.get(self.url)
        except requests.exceptions.ConnectionError:
            raise ConnectionRefused

        if req.status_code == 200:
            # Check for empty response
            if req.text:
                data = req.json()
                status = data.get('status')
                self.clear_url()
                if status == '1':
                    return data
                else:
                    raise EmptyResponse(data.get('message', 'no message'))
        raise BadRequest(
            "Problem with connection, status code: %s" % req.status_code)
