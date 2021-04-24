from django.shortcuts import render
from web3 import Web3
from django.http import HttpResponse, request, JsonResponse
from .models import PostToken
import json
from django.views.decorators.csrf import csrf_exempt
# ------------------PRIVATE KEYS----------------------------------------------------
# private_key = "b3d0ed78f9f2e9bad89d86b5014088f4ace228e5cb08d4b23085f12359402588"
# private_key = "c08a7a25e4366e6e4d1befaccccaa7192520e0ad3eb01106646a37d9e53b9bf9"
# ----------------------------------------------------------------------------------

# URL for ropsten from infura and connecting to web3
ropsten_url = "https://ropsten.infura.io/v3/b9c5cb184a4c45f9bdb16fc184c5e523"
web3 = Web3(Web3.HTTPProvider(ropsten_url))
# The contract address for my contract built in solidity.
contract_address = Web3.toChecksumAddress("0x5b35d46e0634efad6843c067bf8f498ed7c1ea4b")
abi = json.loads(
'''
[
    {
        "inputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "tokenOwner",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "tokens",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "tokens",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "RGdecimals",
        "outputs": [
            {
                "internalType": "uint8",
                "name": "",
                "type": "uint8"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "RGname",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "RGsymbol",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "internalType": "address",
                "name": "receiver",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tknQty",
                "type": "uint256"
            }
        ],
        "name": "RGtransfer",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "internalType": "address",
                "name": "RGTokenUser",
                "type": "address"
            }
        ],
        "name": "balance",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
] ''' )

# -------------------------GET and POST--------------------------------------
@csrf_exempt
def RGTokenPost(request):
    if request.method == "GET":
        obj = PostToken.objects.all()
        data = {"Token response":list(obj.values(
            "id",
            "sender_address",
            "reciever_address",
            "value",
            "sender_balances",
            "reciever_balance",
            "private_key"
            ))}
        return JsonResponse(data)
    
    elif request.method == "POST":
        sender = request.POST["sender_address"]
        reciever = request.POST["reciever_address"]
        value = request.POST["value"]
        private_key = request.POST["private_key"]
        sender_addr = Web3.toChecksumAddress(sender)
        reciever_addr = Web3.toChecksumAddress(reciever)
        rgt_qty = int(value)
        # To connect to my contract using the contract address and abi
        contract = web3.eth.contract(address = contract_address,abi=abi)
        nonce = web3.eth.getTransactionCount(sender_addr)

        RGtrx = contract.functions.RGtransfer(reciever_addr,rgt_qty).buildTransaction({
            'chainId':3,
            'gas':3000000,
            'gasPrice':web3.toWei('40','gwei'),
            'nonce':nonce,
        })

        signed_RGtrx = web3.eth.account.signTransaction(RGtrx,private_key)
        RGtrx_hash = web3.eth.sendRawTransaction(signed_RGtrx.rawTransaction)
        RGtrx_receipt = web3.eth.waitForTransactionReceipt(RGtrx_hash)
        count = 0
        while RGtrx_receipt is None and (count<30):
            time.sleep(10)
            RGtrx_receipt = w3.eth.getTansactionReceipt(result)

        sender_balance = contract.functions.balance(sender).call()
        reciever_balance = contract.functions.balance(reciever).call()

        obj = PostToken(
            sender_address = sender,
            reciever_address = reciever,
            value = value,
            sender_balances = sender_balance,
            reciever_balance = reciever_balance,
            private_key = private_key
            )
        obj.save()
        data = {
                "From":obj.sender_address,
                "To":obj.reciever_address,
                "Value":obj.value}
        return JsonResponse(data)

