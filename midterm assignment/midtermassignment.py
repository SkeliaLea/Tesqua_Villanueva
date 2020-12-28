#RUIZ, James Adrian S.
#kuwang ko read file sir nahutdan oras ^_^ 
from student import Student
from os import system
import os

menu = ('0.Exit','1.Add Student','2.Find Student','3.Delete Student','4.Display Student')
studlist=[]
filename = 'student.txt'

def addStudent():
    
    test=True
    while test!=False:
        try:
            idno=int(input('Please Enter an ID Number:'))
            test=False
        except:
            print("Invalid ID Number! Please enter a valid ID Number.")
            test=True
    lname= input('Enter lastname:')
    fname= input('Enter firstname:')
    test=True
    while test!=False:
        try:
            age= input('Enter age:')
            test=False
        except:
            print("Invalid Age! Please input an integer.")
            test=True
    course= input('Enter course:')
    test=True

    while test!=False:
        try:
            level= input('Enter level:')
            if (int(level)<=5 and int(level)>0):
                test=False
        except:
            print("Invalid level! Please input an integer.")
            test=True
    s=Student(idno,lname,fname,age,course,level)
    studlist.append(s)
    writedata();
def writedata():
    f=open(filename,'a')
    for item in studlist:
        f.write(str(item.idno)+',')
        f.write(str(item.lastname)+',')
        f.write(str(item.firstname)+',')
        f.write(str(item.age)+',')
        f.write(str(item.course)+',')
        f.write(str(item.level)+'')
        f.write(' - ')
    f.close()
def findStudent():
    print("------------FIND STUDENT------------")
    idno = input('Find Student- Enter ID Number:')
    for item in studlist:
        if(int(idno)==int(item.idno)):
            print("\n\n")
            print("------------------------")
            print(item.idno,item.firstname,item.lastname,item.age,item.course,item.level)
            print("------------------------\n\n")
def deleteStudent():
    count=0
    print("------------DELETE STUDENT------------")
    idno = input('Delete Student- Enter ID Number:')
    for item in studlist:
        
        if(int(idno)==int(item.idno)):
            
            studlist.pop(count)
            print('Student removed')
        count=count+1
def display():
    print("---------DISPLAY STUDENTS---------\n")
    for item in studlist:
        print(item.idno,item.firstname,item.lastname,item.age,item.course,item.level, sep= ' ')

    print("------------------------\n")    
def main():
    #idno,lastname,firstname,age,course,level
    global studlist
    temp_list=[]
    count = 0
    content=[]
    #if no file create txtfile
    if not os.path.isfile(filename):
        f=open(filename,'a')
        f.close()
    #read data from txtfile into list
    """if os.path.isfile(filename):
        with open("student.txt", "r") as txtfile:
            lines = txtfile.readlines()
            
        print(lines)

        for i in range():
            for l in lines:
                temp_list = l.split("+")
                studlist.append(temp_list[i])
     
        for item in studlist:
            print(item)
    """
    system("clear")
    opt = -1
    flag = 1
    test=True
 
    while opt!=0:
        for items in menu:
            print(items)
        while test!=False:
            try:
                opt=int(input("Choose Option(0-4):"))
                test=False
            except:
                print("Invalid Option!")
                test=True
            

        print("------------------------")
                
        if opt==1:
            addStudent()
        elif opt==2:
            findStudent()
        elif opt==3:
            deleteStudent()
        elif opt==4:
            display()
                
        
    
        
    
    #s=Student("18726273","Ruiz","James Adrian","10","BSIT","3")
    #print("Student=>",end=" ")

    #studlist.append(Student("18726273","Ruiz","James Adrian","10","BSIT","3"))
    #s.displayStudent()
    
    
    
if __name__=="__main__":
    
    main()
