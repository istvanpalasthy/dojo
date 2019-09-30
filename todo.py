task=input("Please specify an input [list, add, mark, archive]: ")
if task=="add":
    with open("todo.txt","a") as file:
        toDo=input("Add an item: ")
        file.write(" "+toDo+"\n")
        print("Task added.")
if task=="list":
    with open("todo.txt","r") as file:
        print("You saved the following things:")
        a=1
        for line in file:
            print("{}. ".format(a),line)
            a+=1
if task=="mark":
    lists=[]
    with open("todo.txt","r") as file:
        print("You saved the following inputs:")
        a=1
        for line in file:
            print("{}. ".format(a),line)
            lists.append(line)
            a+=1      
    with open("todo.txt","w") as file:
        toDelete=int(input("Which task did you finished?: "))
        for i in range(a-1):
            if i==toDelete-1:
                file.write("[X] "+lists[i][3:])
                print(lists[i][3:(len(lists[i])-1)]+" is completed.")
            else:
                file.write("[ ] "+lists[i][3:])
            a+=1
if task=="archive":
    lists=[]
    a=1
    with open("todo.txt","r") as file:
        for line in file:
            lists.append(line)
            a+=1
    with open("todo.txt","w") as file:
        for i in range(a-1):
            if not(lists[i][1]=="X"):
                file.write("[ ] "+lists[i][3:])   
    print("I deleted everything.")