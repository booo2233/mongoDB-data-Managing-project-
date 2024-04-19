
import json 
from pymongo import MongoClient
import pprint



counts = "mongodb+srv://youarealoafofbread1:SNt6eJKr2nbLZAT@lol.rntnmjb.mongodb.net/?retryWrites=true&w=majority&tls=true"
cilent = MongoClient(counts)


produck = cilent.project
ads = produck.ads


def inst():
  while True:  
     name = input("Enter the name of Customer: ").lower()
     number = input("Enter the number of Customer: ")
     if len(number) != 10:
        print("Number should be 10 digits")
        continue
     if not number.isdigit():
       print("Enter a wallet number")
       continue

    
     number = int(number)

     existing_user = ads.find_one({"number": number})  
     if  existing_user is not None:
            ads.update_one({"number": number}, {"$inc": {"count": 1}})
            print(f"Customer with number {number} already exists. Count incremented by 1.")
            columns = {"_id": 0, "name": 1, "number": 1,"count":1}
            people = ads.find({"number":number}, columns)

            for person in people:
              pprint.pprint(person)
            break
      
     
     else:
             
            
            customer_doc = {
                "name": name,
                "number": number,
                "count": 1
            }

            
            insertion_result = ads.insert_one(customer_doc)
            print(f"Customer added successfully with ID: {insertion_result.inserted_id}")

            break
def math():
  while True:
    op = ["+","-","*","/","**"]
    ev = input("Input a statement like (1+1,1*1,1/1) qm to Quit form mode math:")
    if ev == "qm":
        break
    else:
        try:
         evt = eval(ev)
         print(evt)
         continue
        except Exception as e:
           print(f"Input {e} invalid statements")
        
def sdb():
   while True:
      modes = input("Would you like to search by name or number To search by name, type in na to search by number. Type in num or qm to quit sedb mode: ").lower()
      if modes == "na":

         name = input("input a name of customer: ").lower()
         columns = {"_id": 0, "name": 1, "number": 1,"count":1}
         people = ads.find({"name":name}, columns)

         for person in people:
            pprint.pprint(person)

      elif modes == "num":
         name = input("input the name of customer: ").lower()
         number = input("input the number of customer: ")
         if len(number) != "10":
            print("Number should be 10 digits load")
         if  number.isdigit():
            number = int(number)
            columns = {"_id": 0, "name": 1, "number": 1,"count":1}
            people = ads.find({"name":name,"number":number}, columns)

            for person in people:
              pprint.pprint(person)
         else:
            
           print("Enter a wallet number") 

      elif modes == "qm":
         break
        
      else:
         print("Invalid input")
         continue  
      
          
         

while True:
    mode = input("To add a customer Type in add or q to Quit :").lower()

    if mode == "add":
        inst()

    elif mode == "math":
        math()
    elif mode == "sedb":
       sdb()
      
    elif mode == "q":
       quit()

    elif mode == "--help":
          fhand = open("help0.txt")
          for words in fhand:
              print(words)
          fhand.close()
    else:
        print("Invalid mode.use --help")
        continue



