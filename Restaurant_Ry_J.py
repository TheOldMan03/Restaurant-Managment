def Main_Menu():
    while True:
        print()
        print('Main Menu')
        print()
        print('''1.Adminstration
2.Customer Service
3.Exit''')

        print()
        try:
            ch=int(input('Choice: '))                   

            if ch==1:
                Adminstration_Screen()
            elif ch==2:
                Customer_Service()
            elif ch==3:
                break
            else:
                print()
            
        except ValueError:              #If the user enters any other data type in the input statements other than integers
            print()
            print('You have entered a wrong data type.Type only integer values accordingly')
            print()

def Adminstration_Screen():
        while True:
            print()
            print('Adminstration')
            print()
            print('''1.Menu
2.Chef
3.Return to main menu''')
            print()

            try:
                c1=int(input('Choice: '))
            
                if c1==1:
                    Menu()
                elif c1==2:
                    Chef()
                elif c1==3:
                    break
                    Main_Menu()
                else:
                    print()
            except ValueError:
                print()
                print('You have entered a wrong data type.Type only integer values accordingly')
                print()

def Menu():    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Menu
(food_code VARCHAR(7) NOT NULL PRIMARY KEY,
food_item_name VARCHAR(30) NOT NULL,
cost INT NOT NULL)''')

    while True:
        print()
        print('Menu Designing')
        print()
        print('''1.Add Data in Menu
2.Update any data
3.Delete the data
4.Display Menu
5.Return to adminstration menu''')

        try:
            c_menu=int(input('Choice: '))
            print()
        
            if c_menu==1:
                n=int(input('Number of times to add the data in menu: '))
                print()
                if n==0 or n<0:                                     #If the user enters a number less than or equal to 0
                    print('No Data is added in Menu')
                    print()
                else:
                    for i in range(n):
                        cursor.execute('SELECT * FROM MENU')            #Selects everything from table Menu 
                        d=cursor.fetchall()                                                #The selected data is stored as d(as a list of tuples)
                        food_code=input('Enter the food code(Number): ')
                        if len(food_code)==0:                                           #Checks whether the food code entered is not a null value
                            print('This is not a valid name!')
                        else:
                            for j in d:
                                if food_code==j[0]:                                       #Checks if the food code already exists in the table menu,if it does it is rejected
                                    print('The food code given already exists.Try another valid food code')
                                    print()
                                    break
                            else:
                                name=input('Enter the name of the food item:')
                                cost=int(input('Enter the cost of the food item: '))

                                cursor.execute("INSERT INTO Menu VALUES('{}','{}',{})".format(food_code,name,cost))
                                sqlc.commit()
                                print('Successfully added')
                                print()

            elif c_menu==2:
                cursor.execute('SELECT * FROM MENU')
                D=cursor.fetchall()
                if D==[]:
                    print('The table is empty,nothing to update here!')
                    print()
                    
                else:
                    print()
                    print('''Update the table through
1.Name
2.Cost''')
                    c_menu_modify=int(input('Choice: '))
                    print()

                    if c_menu_modify==1:
                        code=input('Enter the code of the food item: ')
                        cursor.execute('SELECT * FROM MENU')
                        d=cursor.fetchall()
                                        
                        for j in d:
                            if code==j[0]:                      
                                new_name=input('Enter new name of the food item: ')
                                print('Are you sure you want to UPDATE the NAME of food code',code,'to',new_name,'?')
                                confirm=input('Y/N:')
                                if confirm=='Y' or confirm=='y':
                                    cursor.execute("UPDATE Menu SET food_item_name='{}' WHERE food_code='{}' ".format(new_name,code))
                                    sqlc.commit()                                               #In line 136,the data in the table is getting updated
                                    print('Successfully Modified!')                     #sqlc.commit() makes sure the update is permanent 
                                    print()
                                    break
                                if confirm=='N' or confirm=='n':
                                    print('Update Cancelled')
                                    print()
                                    break
                        else:   
                            print('The given food code does not exist')
                            print()

                    elif c_menu_modify==2:
                        code=input('Enter the code of the food item: ')
                    
                        for j in d:
                            if code==j[0]:
                                new_cost=int(input('Enter new cost of the food item: '))
                                print('Are you sure you want to UPDATE the COST of food code',code,'to',new_cost,'?')
                                confirm=input('Y/N:')
                                print()

                                if confirm=='Y' or confirm=='y':
                                    cursor.execute("UPDATE MENU SET cost={} WHERE food_code='{}' ".format(new_cost,code))
                                    sqlc.commit()
                                    print('Successfully Modified!')
                                    print()
                                    break
                                if confirm=='N' or confirm=='n':
                                    print('Update Cancelled!')
                                    print()
                                    break
                        else:
                            print('The given food code does not exist')
                            print()
                    
                    else:
                        print()
            

            elif c_menu==3:
                cursor.execute('SELECT * FROM MENU')
                dc=cursor.fetchall()
                if dc==[]:
                    print('The table menu is already empty')
                    print()
                else:
                    print()
                    print('''1.Delete the entire table Menu
2.Delete specified rows''')
            
                    c_menu_delete=int(input('Choice: '))
                    print()

                    if c_menu_delete==1:
                        print('Are you sure you want to DELETE EVERYTHING in Menu?')
                        confirm=input('Y/N: ')
                    
                        if confirm=='Y' or confirm=='y':
                            cursor.execute("DELETE FROM MENU")
                            sqlc.commit()
                            print('Table is deleted successfully!')
                            print()
                        if confirm=='N' or confirm=='n':
                            print('Delete cancelled')
                            print()
                
                    elif c_menu_delete==2:
                        cursor.execute('SELECT * FROM MENU')
                        dc=cursor.fetchall()
                        if dc==[]:
                            print('Menu table is already empty')
                            print()
                        else:
                            code=input('Enter the food item code to be deleted: ')
                            for j in d:
                                if code==j[0]:
                                    print('Are you sure you want to DELETE the ENTIRE ROW having food code',code,'?')
                                    confirm=input('Y/N:')
                                    print()

                                    if confirm=='y' or confirm=='Y':
                                        cursor.execute("DELETE FROM MENU WHERE food_code='{}' ".format(code))
                                        sqlc.commit()
                                        print('Deletion Sucessful!')
                                        print()
                                        break
                                    if confirm=='n' or confirm=='N':
                                        print('Deletion Cancelled!')
                                        print()
                                        break
                            else:
                                print('The given food code does not exist')

                            
            elif c_menu==4:                                                     
                cursor.execute('SELECT * FROM MENU')
                d=cursor.fetchall()
                if d==[]:
                    print('Empty')
                    print()
                else:
                    x=PrettyTable()                                                         #The data will be represented in a tabular form
                    x.field_names=['Food_code','Food_item','cost']
                    for i in d:
                        x.add_row([i[0],i[1],i[2]])
                    print(x)
        
            elif c_menu==5:
                print()
                break
                Adminstration_Screen()
            
            else:
                print()
        except ValueError:
            print('You have entered a wrong data type.Type only integer values accordingly')
            print()


def Customer_Service():    
    cursor.execute('SHOW TABLES')
    dzxu=cursor.fetchall()
    try:
        for kzxu in dzxu:
            if kzxu[0]=='chef':                 #Checks whether the table Chef has been created
                cursor.execute("SELECT food_item_name,cost FROM MENU")
                d1=cursor.fetchall()
                if d1==[]:                          
                    print('The menu table is empty,go to admin and fill the tables')
                    print()
                else:
                    while True:
                        print()
                        print('Customer Service')
                        print()
                        print('''1.Take in
2.Take out
3.Return to Main menu''')

                        c=int(input('Choice: '))
                        print()

                        if c==1:
                            print('''1.Order Now
2.Cancel Order''')
                            print()
                            
                            c1=int(input('Choice: '))
                            print()

                            if c1==1:
                                cursor.execute('Select * From Chef')
                                s=cursor.fetchall()
                            
                                if len(s)==15:
                                    print('The restaurant is fully booked and cannot take any more customers')
                                    print()
                                
                                else:
                                    tk=randint(0,15)
                                    cursor.execute('Select Token_No From Chef')
                                    s=cursor.fetchall()
                                
                                    for i in range(len(s)):
                                        if tk==s[i]:
                                            w=s[i]
                                            while tk==w:
                                                tk=randint(0,15)

                                    else:
                                        cursor.execute("SELECT food_item_name,cost FROM MENU")
                                        d=cursor.fetchall()                                                                           
                                        print('Menu')
                                        print()
                                        y=PrettyTable()
                                        y.field_names=['Food Item','Cost']                  #Displays the menu so that 
                                        for q in d:                                                           #the user can order food 
                                            y.add_row([q[0],q[1]])
                                        print(y)


                                        f=input('What would you like to have ?: ')
                                        cursor.execute('SELECT food_item_name,food_code,cost From Menu')
                                        d1=cursor.fetchall()
                                
                                        for i in d1:
                                            if i[0]==f:
                                                y=i[1]
                                                x=i[2]
                                                q=int(input('Quantity required: '))
                                                s='NotReady'
                                                cursor.execute("INSERT INTO Chef values({},'{}',{},'{}')".format(tk,y,q,s))
                                                sqlc.commit()
                                                print()
                                                print('Your Bill')
                                                print()
                                                print('Here is your token number: ',tk)
                                                print('Total cost will be: ',q*x)
                                                print('Please wait till the order is ready ')
                                                print()
                                                break
                                        else:
                                            print('The given food name does not exists')
                                            print()
                                            
                            elif c1==2:
                                cursor.execute('Select * From Chef')
                                f=cursor.fetchall()

                                if f==[]:
                                    print('Empty table.Nothing to cancel')
                                    
                                else:
                                    t=int(input('Enter the token number to be cancelled: '))
                                    for j in f:
                                        if j[0]==t:

                                            if j[3]=='Ready':
                                                print('The food is ready you cannot cancel this order')
                                                print()
                                                
                                            else:
                                                x=j[1]
                                                z=j[2]
                                                cursor.execute("Select food_item_name,cost From Menu where food_code='{}' ".format(x))
                                                a=cursor.fetchall()
                                                y=a[0][0]
                                                k=a[0][1]
                                        
                                        
                                                print()
                                                print('Your Order:')
                                                print()
                                                print('Token No:',t)
                                                print('Food name:',y)
                                                print('Quantity:',z)
                                                print('Cost:',k*z)
                                                print()

                                        
                                                print('Are you sure you want to cancel your order?')
                                                con=input('Y/N')
                                                print()

                                                if con=='y' or con=='Y':
                                                    cursor.execute("Delete From Chef where Token_No='{}' ".format(t))
                                                    sqlc.commit()
                                                    print('Order Cancelled Successfully!')
                                                    print()

                                                elif con=='N' or con=='n':
                                                    print('Order is not cancelled')
                                                    print()

                                                break
                                        else:
                                            print('The given token number does not exist')
                                            print()
                        

                        elif c==2:
                            f=int(input('Enter the token no you have got: '))
                            cursor.execute("SELECT * FROM Chef WHERE Token_no={}".format(f))
                            d=cursor.fetchall()

                            if d==[]:
                                print('The token no given does not exist')
                                print()
                            else:
                                for i in d:                 
                                    if i[0]==f:
                                        if i[3]=='NotReady':
                                            print('The food is not ready')
                                            print()
                                        else:
                                            print('The food is ready now, Now you can eat')
                                            cursor.execute('DELETE FROM CHEF WHERE Token_No={}'.format(f))
                                            sqlc.commit() #Once the food is delivered,the program deletes the record from the chef table
                                            print()
                                        break
                                else:
                                    print('The given token number does not exists')
                                    print()                        
                                                
                        elif c==3:
                            print()
                            break
                            Main_Menu()

                        else:
                            print('Wrong choice: ')
                            print()
                break           
        else:
            print('The table menu or chef does not exists')
            print('Go to admin,go and create both the tables and then come back here')
            print()
            
    except ValueError:
        print('You have entered a wrong data type.Type only integer values accordingly')
        Customer_Service()
        

def Chef():
    cursor.execute('''CREATE TABLE IF NOT EXISTS CHEF
(Token_no int not null,
food_code varchar(30) not null,
quantity int not null,
status varchar(30) not null)''')

    cursor.execute('SELECT * FROM CHEF')
    D=cursor.fetchall()

    if D==[]:
         print('The table has been created go to chef,Now you can go to customer side')
         print()
    else:
            while True: 
                print('Chef Designing')
                print()
                print('''1.Display the details of chef
2.Update the status of food
3.Return to Adminstration''')
                print()

                try:
                    c_chef=int(input('Choice: '))
                    if c_chef==1:
                        cursor.execute('SELECT * FROM CHEF')
                        d=cursor.fetchall()
                        if d==[]:
                            print('Empty')
                            print()
                        else:
                            z=PrettyTable()
                            z.field_names=['Token No','Food_code','Quantity','Status']
                            for i in d:
                               z.add_row([i[0],i[1],i[2],i[3]])
                            print(z)
    
                    elif c_chef==2:
                        tk=int(input('Enter the token number: '))
                        cursor.execute("Select Token_No From Chef WHere Status='Ready' ")
                        r=cursor.fetchall()

                        for j in r:
                            if tk==j[0]:
                                print('You have already modified the status of this token number')
                                print()
                                break
                        else:
                            cursor.execute("SELECT * FROM CHEF WHERE Token_no={} and Status='NotReady' ".format(tk))
                            d=cursor.fetchall()
            
                            for i in d:
                                if i[0]==tk:
                                    cursor.execute("UPDATE CHEF SET STATUS='Ready' WHERE Token_No={}".format(tk))
                                    sqlc.commit()   #Updates the status from Not Ready to Ready
                                    print('Successfully modified!')
                                    print()
                                    break
                            else:
                                 print('The given token number does not exists')
                                 print()
                            
                    elif c_chef==3:
                        break
                        Adminstration_Screen()

                    else:
                        print()
                except ValueError:
                    print('You have entered a wrong data type.Type only integer values accordingly')
                    print()

try:
    import mysql.connector                              #Importing mysql.connector to use Mysql in python
    from random import randint                       #importing random module for RNG(random number generation used in Customer_Service)
    from prettytable import PrettyTable          #Importing prettytable so that data can be read in a tabular form
    
except ModuleNotFoundError:                       #If the user does not have mysql.connector or prettytable module
    print('The module mysql.connector or prettytable are not installed in your device')
    print('Install it in your PC and come back here')
    print('Press the Enter key to continue')
    ch=input()

else:
    sqlc=mysql.connector.connect(host='localhost',user='root',passwd='root123')       #Connecting python to Mysql
    cursor=sqlc.cursor()                                                                                                      #Creating cursor object
    cursor.execute('CREATE DATABASE IF NOT EXISTS restaurant')
    cursor.execute('Use Restaurant')
    print()
    print('\t\t\tRestaurant Management')                                                                        #The beginning is in the end
    Main_Menu()

    sqlc.close()                                                                                                                    #Closing the connection once the user exits
