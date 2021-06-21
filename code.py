import csv

words=[]
global_variable=""  ###the part of used global variable for seventh selection

with open('movies.csv') as csv_file:  ###the part of reading of file.
    csv_reader = csv.reader(csv_file,delimiter=',') 
    for row in csv_reader:
        words.append(row)
for i in range(len(words)):
        for j in range(len(words[i])):
            words[i][j]=words[i][j].strip().lower() 
            ###the part of deleting of unnecessary space.
            
def menu():
    print("1. List all movies of given actor or actress")
    print("2. Given an actor or actress's name, find all the actors or actresses with whom he/she has acted.")
    print("3. List all actors and actresses in a movie.")
    print("4. List all actors and actresses in two movies.")
    print("5. List common actors and actresses in two movies.")
    print("6. List all actors and actresses in either of the movies but not both")
    print("7. Save results to a file.")
    print("0. Exit")
    print()

        
    deger=10
    while deger != 0:  ###I created infinite loop with 'while loop' for menu.
        try:
            deger=int(input("Select the operation you want to do between 0 and 7.\n"))
            if(deger==1):
                first_selection()
            elif(deger==2):
                second_selection()
            elif(deger==3):
                third_selection()
            elif(deger==4):
                fourth_selection()
            elif(deger==5):
                fifth_selection()
            elif(deger==6):
                sixth_selection()
            elif(deger==7):
                seventh_selection()
        except ValueError: ###I used 'try catch' for incorrectly entered value.
            print('Wrong value')
            
def first_selection(): 
    global global_variable
    global_variable+='(first_selection)\n'
    name=input("Enter Actor or actress's name.\n").lower()
    global_variable+='Entered value('+name.title()+')'+','
    
    for i in range(len(words)):
        for j in range(1,len(words[i])):
            if(name==words[i][0]):
                ###If it matches the actor we entered, it prints the actor or actress's movies.
                print(words[i][j].title())
                global_variable+=words[i][j].title()+', '
                ###The done operations are kept in a variable for the seventh operation.
    global_variable+='\n'
    
def second_selection():
    global global_variable
    my_set=set() ###I used 'set' for repetitive words in this part.
    global_variable+='(second_selection)\n'
    name=input("Enter Actor or actress's name.\n").lower()
    global_variable+='Entered value('+name.title()+')'+','
    
    for i in range(len(words)):
        for j in range(len(words[i])):
            if(name==words[i][0]):
                temp=words[i][j]
                for a in range(len(words)):
                    for b in range(len(words[a])):
                        if(temp==words[a][b]):
                            if(name!=words[a][0]):
                                my_set.add(words[a][0].title())
    for a in my_set:
        print(a)
        global_variable+=a.title()+', '
        ###The done operations are kept in a variable for the seventh operation.
    global_variable+='\n'
    
def third_selection():
    global global_variable
    global_variable+='(third_selection)\n'
    name=input("Enter Film's name.\n").lower()
    global_variable+='Entered value('+name.title()+')'+','
    
    for i in range(len(words)):
        for j in range(len(words[i])):
            if(name==words[i][j]):
                ###If it matches the film we entered,it prints all the actors who play in the film.
                print(words[i][0].title())
                global_variable+=words[i][0].title()+', '
                ###The done operations are kept in a variable for the seventh operation.
    global_variable+='\n'
    
def fourth_selection():
    global global_variable
    global_variable+='(fourth_selection)\n'
    my_set=set() ###I used 'set' for repetitive words in this part.
    name1=input("Enter Film's name.\n").lower()
    name2=input("Enter the name of the other movie.\n").lower()
    global_variable+='Entered value('+name1.title()+' and '+name2.title()+')'+','
    for i in range(len(words)):
        for j in range(len(words[i])):
            if(name1==words[i][j] or name2==words[i][j]):
                ###If it matches the films we entered,it assigns to the 'set' variable I created.
                my_set.add(words[i][0])
    for a in my_set:
        print(a.title())
        global_variable+=a.title()+', '
        ###The done operations are kept in a variable for the seventh operation.
    global_variable+='\n'      
    
def fifth_selection():
    global global_variable
    global_variable+='(fifth_selection)\n'
    name1=input("Enter Film's name.\n").lower()
    name2=input("Enter the name of the other movie.\n").lower()
    global_variable+='Entered value('+name1.title()+' and '+name2.title()+')'+','
    for i in range(len(words)):
        temp=0
        for j in range(len(words[i])):
            if(name1==words[i][j]):
                temp+=1
            elif(name2==words[i][j]):
                temp+=1
            elif(temp==2):
                print(words[i][0].title())
                ###If the films we entered are available, the 'temp'  increases.if 'temp' is equal to 2,it prints actors or actresses. 
                global_variable+=words[i][0].title()+', '
                ###The done operations are kept in a variable for the seventh operation.
                break
    global_variable+='\n'
    
def sixth_selection():
    global global_variable
    global_variable+='(sixth_selection)\n'
    array=[]
    name1=input("Enter Film's name.\n").lower()
    name2=input("Enter the name of the other movie.\n").lower()
    global_variable+='Entered value('+name1.title()+' and '+name2.title()+')'+','
    for i in range(len(words)):
        for j in range(len(words[i])):
            if(name1==words[i][j] or name2==words[i][j]):
                array.append(words[i][0].title())
                ###it assigns into 'list' the films we entered.
    for a in range(len(array)): 
        counter=0
        temp=array[a]
        for b in range(len(array)):
            if(temp==array[b]):
                counter+=1
        if(counter==1):
            ###if temp is equal to 1,it prints only once repetitive actors or actresses.
            print(temp)
            global_variable+=temp+', '
            ###The done operations are kept in a variable for the seventh operation.
    global_variable+='\n'
    
def seventh_selection():   ######the part of writing of file.
    global global_variable
    output=open('output.csv','w') 
    output.write(global_variable)
    print("The operations recorded.")
    output.close()
    
    


menu()
