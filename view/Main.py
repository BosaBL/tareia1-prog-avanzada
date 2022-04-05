'''
Created on 04-04-2022

@author: dsanmartins
'''
from model.NodeList import NodeList
from model.Client import Client
from controller.DatabaseController import DatabaseController

nodeList = NodeList()
database = DatabaseController()
database.populateDatabase()

list_ = database.getClient("clients.csv")
for i in range(len(list_)):
    nodeList.addNode(list_[i])

print("***** Please chose an option ******")
print("[1] Print the list")
print("[2] Add a new client")
print("[3] Search for a client")
choice = input("?")
while True:
    
    if choice =='1':
        nodeList.printList()
    elif choice =='2':
        clientDni = input("DNI of the client?")
        clientName = input("Name of the client?")
        nodeList.addNode(Client(clientDni,clientName))
    elif choice =='3':
        try:
            clientDni = input("Search by DNI")
            client = nodeList.searchByDni(clientDni)
            print("The client exist in the database!")
            print("")
        except(Exception,AttributeError):
            print("Client does not exist")
    elif int(choice) > 3: #Or whatever end condition
        print("Bye!")
        break
    
    
    print("***** Please chose an option? ******")
    print("[1] Print the list")
    print("[2] Add a new client")
    print("[3] Search for a client")
    choice = input("?")
    



