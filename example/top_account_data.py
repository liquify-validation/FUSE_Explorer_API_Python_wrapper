from Fuse_Explorer_API.account import Account
from datetime import datetime
import csv

def main():
    apiFuse = Account(address='')
    balance = apiFuse.get_list_of_accounts()
    #build the list in balance order
    sortedList = sorted(balance, key=lambda i: int(i['balance']), reverse=True)
    sortedList = [elem for elem in sortedList if elem['balance'] != '0']
    consensus = '0x3014ca10b91cb3d0ad85fef7a3cb95bcac9c0f79'

    validatorBalance = {}
    with open('holders.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        #headers
        writer.writerow(["Wallet", "Validating", "Staked", "Delegated", "Current Balance", "first transaction", 'delegated to'])
        for i in range (0,20):
            address = sortedList[i]['address']
            validatorBalance[address] = 0

        for i in range (0,20):
            address = sortedList[i]['address']
            balance = float(float(sortedList[i]['balance']) * 1e-18)
            apiFuse = Account(address=address)
            txList = apiFuse.get_tx_list()
            tx = [elem for elem in txList if elem['from'] == address]
            rx = [elem for elem in txList if elem['to'] == address]
            totalIn = 0
            for itr in rx:
                totalIn += int(itr['value'])

            #this address started with 300million
            if(address == '0xd9176e84898a0054680aec3f7c056b200c3d96c3'):
                totalIn += 300000000 * 1e18

            totalOut = 0
            for itr in tx:
                totalOut += (int(itr['value']) + int(itr['gasUsed']))

            sentToConsensus = [elem for elem in tx if elem['to'] == consensus]
            sentToConsensus = [elem for elem in sentToConsensus if elem['value'] != '0']
            staked = 0
            delegated = 0
            delegationstr = ''

            for itr in sentToConsensus:
                if(itr['isError'] == '0'):
                    if itr['input'] == '0x':
                        staked += float(float(itr['value'])* 1e-18)
                        validatorBalance[address] += staked
                    else:
                        #delegated
                        delegationstr += ' 0x' + itr['input'][-len(address)+2:] + ' (' + str(float(int(itr['value']) * 1e-18)) + '); '
                        delegated += float(float(itr['value'])* 1e-18)
                        try:
                            validatorBalance['0x' + itr['input'][(-len(address)+2):]] += delegated
                        except KeyError:
                            print("error")

            dateOfFirstTransaction = datetime.utcfromtimestamp(int(txList[0]['timeStamp'])).strftime('%Y-%m-%d %H:%M:%S')
            if float(int(totalIn - totalOut) * 1e-18) != balance and validatorBalance[address] >= 3000000:
                validating = 'yes'
            else:
                validating = 'no'
            writer.writerow([address, validating, staked, delegated, balance, dateOfFirstTransaction, delegationstr ])

if __name__ == "__main__":
    main()