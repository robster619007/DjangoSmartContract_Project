# DjangoSmartContract_Project
a demo smart contract project using django which connects to my solidity application deployed on Etherscan

# Smart Contract

Have used solidity as the main language to create the smart contract and deployed on ropsten etherscan test network. The transactions for my tokens can be found on the following link
https://ropsten.etherscan.io/address/0x4e882e0fee2d7b55e5f360532e278d79ac85cf11#tokentxns
Have used Web3 and Django Framework to call the functions created in the solidity application.
Metamask was used to get the sender's address and reciever's addresses. Test ether was bought from the following link: https://faucet.ropsten.be/

# The Django Application

The application can be started with the following steps:
1) install pipenv and run pipenv shell to activate the environment
2) run python mange.py makemigrations and python mange.py migrate (to create ur sqllite db)
3) run python manage.py runserver, this will start the local server http://127.0.0.1:8000/
4) http://127.0.0.1:8000/RGToken/ with GET for the get functions
5) http://127.0.0.1:8000/RGToken/ with POST will allow you to add your own transactions with following parameter
          a)sender_address
          b)reciever_address
          c)value
          d)primary_key
6) Then use the get function to get the details of the transaction with the primary key(please dont show ur primary key to anyone)

This is a very small project. I am still very inexperienced but am hoping to gain more experience by working on such projects



