# DjangoSmartContract_Project
A demo smart contract project using django which connects to my solidity application deployed on Etherscan

# The Django Application

The application can be started with the following steps:
1) install pipenv and run pipenv shell to activate the environment(If the above pipenv does not work)
2) make sure to install django and web3 using pip install django and pip install web3
3) run python mange.py makemigrations and python mange.py migrate (to create ur sqllite db)
4) run python manage.py runserver, this will start the local server http://127.0.0.1:8000/
5) Please enter the urls mentions below in Postman.
6) http://127.0.0.1:8000/RGToken/ with GET for the get functions
7) http://127.0.0.1:8000/RGToken/ with POST will allow you to add your own transactions with following parameter<br >
          a) sender_address<br >
          b) reciever_address<br >
          c) value<br >
          d) primary_key<br >
6) Then use the get function to get the details of the transaction with the primary key(please dont show ur primary key to anyone)<br >

This is a very small project. I am still very inexperienced but am hoping to gain more experience by working on such projects


# Smart Contract

Have used solidity as the main language to create the smart contract and deployed on ropsten etherscan test network.<br > 
The transactions for my tokens can be found on the following link<br ><br >
https://ropsten.etherscan.io/address/0x4e882e0fee2d7b55e5f360532e278d79ac85cf11#tokentxns<br ><br >
Have used Web3 and Django Framework to call the functions created in the solidity application.<br ><br >
Metamask was used to get the sender's address and reciever's addresses. Test ether was bought from the following link: https://faucet.ropsten.be/<br ><br >
You can check my code for the smart contract on https://github.com/robster619007/demoSoliditySC<br ><br >


