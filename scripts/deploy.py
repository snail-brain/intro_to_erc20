from eth_utils.currency import from_wei
from brownie import network, SNLToken, config
from scripts.helpful_scripts import getAccount
from web3 import Web3


def deploy_token():
    account = getAccount()
    _snail = SNLToken.deploy(
        10000,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print(_snail.totalSupply())
    print(Web3.fromWei(_snail.balanceOf(account), "ether"))


def main():
    deploy_token()
