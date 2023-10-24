#-------------------------------------------------------------------------
# AUTHOR: Sunjay Guttikonda
# FILENAME: index_mongo.py
# SPECIFICATION: Driver program that triggers the operations by calling the functions and feeding them user-inputted data
# FOR: CS 4250- Assignment #2
# TIME SPENT: 45 minutes
#-----------------------------------------------------------*/

from pymongo import MongoClient  # import mongo client to connect
from db_connection_mongo import *

if __name__ == '__main__':

    # Connecting to the database
    db = connectDataBase()

    # Creating a collection
    documents = db.documents

    #print a menu
    print("")
    print("######### Menu ##############")
    #print("#a - Create a category.")
    print("#b - Create a document")
    print("#c - Update a document")
    print("#d - Delete a document.")
    print("#e - Output the inverted index.")
    print("#q - Quit")

    option = ""
    while option != "q":

          print("")
          option = input("Enter a menu choice: ")

          if (option == "b"):

              docId = input("Enter the ID of the document: ")
              docText = input("Enter the text of the document: ")
              docTitle = input("Enter the title of the document: ")
              docDate = input("Enter the date of the document: ")
              docCat = input("Enter the category of the document: ")

              createDocument(documents, docId, docText, docTitle, docDate, docCat)

          elif (option == "c"):

              docId = input("Enter the ID of the document: ")
              docText = input("Enter the text of the document: ")
              docTitle = input("Enter the title of the document: ")
              docDate = input("Enter the date of the document: ")
              docCat = input("Enter the category of the document: ")

              updateDocument(documents, docId, docText, docTitle, docDate, docCat)

          elif (option == "d"):

              docId = input("Enter the document id to be deleted: ")

              deleteDocument(documents, docId)

          elif (option == "e"):

              index = getIndex(documents)
              print(index)

          elif (option == "q"):

               print("Leaving the application ... ")

          else:

               print("Invalid Choice.")