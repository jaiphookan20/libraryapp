import sqlite3
import datetime
from datetime import date,datetime

connection = sqlite3.connect('./library.db')

cur = connection.cursor()

menu = '''
1.add user
2.add librarian
3.add books
4.update user details
5.update books details
6.delete user
7.delete books
8.read books details 
9.list of books
'''
print(menu)
option = int(input("Enter your option: "))

if option == 1:
	name = input('enter name : ')
	password = input('enter password : ')
	contact = input("enter contact : ")
	fees = input('enter fees : ')
	cur.execute('''INSERT INTO user VALUES(?,?,?,?);''',[name,password,contact,fees])

elif option == 2:
	name = input('enter name : ')
	contact = int(input("enter contact : "))
	cur.execute('''INSERT INTO librarian VALUES(?,?);''',[name,contact])

elif option == 3:
	author = input('enter author : ')
	name = input('enter name : ')
	pubcompany = input('enter pubcompany : ')

	rdate = date(int(input('enter year:')),int(input('enter month:')),int(input('enter day:')))

	ruser = input('enter ruser : ')
	cur.execute('''INSERT INTO books1 VALUES(?,?,?,?,?);''',[author,name,pubcompany,rdate,ruser])

elif option ==4 :
	contact = input("enter contact : ")
	name = input("enter name : ")
	cur.execute('''UPDATE user SET contact = ? WHERE name = ?;''',[contact,name])

elif option == 5:
	renteduser = input("enter renteduser : ")
	name = input("enter name : ")
	cur.execute('''UPDATE books SET renteduser = ? WHERE name = ?;''',[renteduser,name])

elif option == 6:

	cur.execute('''SELECT name,password FROM user;''')
	nplist = cur.fetchall()
	print(nplist)
	uname = input("enter your user name :").strip()
	upassword = input('enter your password :').strip()
	np = (uname,upassword)
	print(np)

	if np in nplist:
		print('Welcome')
		name = input("enter name you want to delete : ")
		cur.execute('''DELETE FROM user WHERE name = ?;''',[name])
	else:
		print("Register")

elif option == 7:
	name = input("enter name : ")
	cur.execute('''DELETE FROM books1 WHERE name = ?;''',[name])

elif option == 8:
	name = input("enter name : ")
	cur.execute('''SELECT * FROM books1 WHERE name = ?;''',[name])
	details = cur.fetchall()
	print(details)

elif  option == 9:
	cur.execute('''SELECT * FROM books1;''')
	blist = cur.fetchall()
	for row in blist:
		print(row)


cur.execute('''SELECT renteduser,renteddate FROM books1;''')
blist = cur.fetchall()

tday = datetime.now()

for row in blist:

	date_object = datetime.strptime(row[1], "%Y-%m-%d")

	if (tday - date_object).days > 14:
		print(row[0]+' has used the book for two weeks.')

	numofdays=(tday-date_object).days

	k = 0

	if numofdays>20:
		k += 20
		if numofdays > 20 and numofdays < 25:
			k += 0
		if numofdays > 24 and numofdays < 30:
			k += 25
		if numofdays > 29 and numofdays < 35:
			k += 30+25
		if numofdays > 34 and numofdays < 40:
			k += 30+25+35
		if numofdays > 39 and numofdays < 45:
			k += 30+25+35+40

		cur.execute('''UPDATE user SET fees = ? WHERE name = ?;''',[k,row[0]])
		cur.execute('''SELECT * FROM user WHERE name = ?;''',[row[0]])
		udetails = cur.fetchall()
		print('updated : ', udetails)





connection.commit()
connection.close()


