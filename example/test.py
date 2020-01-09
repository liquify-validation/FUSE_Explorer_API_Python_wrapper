from Fuse_Explorer_API.account import Account

def main():
    address = '0xd9176e84898a0054680aEc3f7C056b200c3d96C3'
    apiFuse = Account(address=address)
    balance = apiFuse.get_balance()
    balance = float(int(balance) * 1e-18)

    list = apiFuse.get_tx_list(offset=10)
    print("print fuse balance = ", balance)
    print(*list, sep='\n')

if __name__ == "__main__":
    main()