import os
from tkinter import*
path=os.getcwd()
path1=path+"/Bank"
path5=path1
path2 =""
t=0
v=0
a5=0
a1=0
a=10
if(os.path.exists(path1)):
	os.chdir(path1)
	f=open("acc.txt","r+")
	a=f.read()
	a=int(a)
	if(a==394000):
		t=1
else:
	os.mkdir(path1)
	os.chdir(path1)
	f=open("acc.txt","w+")
	f.write("394000")
	f.close()
	t=1

def create_acc():
	root= Tk()
	root.geometry("1600x800+0+0")
	root.title("Epicness Bank")
	Tops = Frame(root, width = 1600,height = 50)
	Tops.pack(side=TOP)

	f0 = Frame(root, width = 800,height = 100, relief=SUNKEN)
	f0.pack(side=TOP)
	f1 = Frame(root, width = 200,height = 100, relief=SUNKEN)
	f1.pack(side=LEFT)
	f2 = Frame(root, width = 200,height = 100, relief=SUNKEN)
	f2.pack(side=RIGHT)
	f3 = Frame(root, width = 800,height = 100, relief=SUNKEN)
	f3.pack(side=BOTTOM)
	f=open("acc.txt","r+")
	x=int(f.read())
	x+=1
	x=str(x)
	f.seek(0,0)
	f.write(x)
	f.close()
	path2=path1+"/"+x
	os.mkdir(path2)
	os.chdir(path2)
	tem="You have been alloted the account number: "+x

	lblInfo = Label(Tops, font=('arial',50,'bold'),text="Account Creation under process",fg="Dark Blue", bd=5, anchor='w')
	lblInfo.grid(row=0,column=0)
	lblInfo = Label(Tops,font=('arial',20,'bold'),text=tem,fg="orange", bd=2,anchor='w')
	lblInfo.grid(row=1,column=0)
	lblInfo = Label(f1,font=('arial',20,'bold'),text="Set a password of your choice.",fg="orange", bd=2,anchor='n')
	lblInfo.grid(row=0,column=0)
	lblInfo = Label(f2,font=('arial',20,'bold'),text="Enter your initial deposit.",fg="orange", bd=2,anchor='n')
	lblInfo.grid(row=0,column=0)

	password=StringVar()
	deposit=StringVar()

	txtpass=Entry(f1,font=('arial', 16,'bold'),textvariable=password, bd=10, insertwidth=4,bg="orange", justify = 'right')
	txtpass.grid(row=1,column=0)
	txtdep=Entry(f2,font=('arial', 16,'bold'),textvariable=deposit, bd=10, insertwidth=4,bg="orange", justify = 'right')
	txtdep.grid(row=1,column=0)

	def qExit():
	    root.destroy()

	def Next():
	    root.destroy()
	    menu()

	def submitp():
		p=(password.get())
		f1=open("pass.txt","w+")
		f1.write(p)
		f1.close()

	def submitd():
		d=(deposit.get())
		f2=open("bal.txt","w+")
		f2.write(d)
		f2.close()
		f3=open("hist.txt","w+")
		f3.write("\bYour transaction history is as follows:\b\nYour initial deposit was "+d+".\n")
		f3.close()

	btnSubmitp=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=15,
	                text="Submit Password", bg="orange",command =submitp).grid(row=6,column=0)

	btnSubmitd=Button(f2,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=15,
	                text="Submit Deposit", bg="orange",command =submitd).grid(row=6,column=0)

	btnNext=Button(f3,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
	                text="Next", bg="orange",command =Next).grid(row=7,column=1)

	btnExit=Button(f3,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
	                text="Exit", bg="orange",command =qExit).grid(row=8,column=1)


	root.mainloop()




def menu():
	root= Tk()
	root.geometry("1600x800+0+0")
	root.title("Epicness Bank")
	Tops = Frame(root, width = 1600,height = 50)
	Tops.pack(side=TOP)

	f0 = Frame(root, width = 800,height = 100, relief=SUNKEN)
	f0.pack(side=TOP)
	f2 = Frame(root, width = 800,height = 100, relief=SUNKEN)
	f2.pack(side=TOP)
	f1 = Frame(root, width = 400,height = 400, relief=SUNKEN)
	f1.pack(side=TOP)

	lblInfo = Label(Tops, font=('arial',30,'bold'),text="Refer our bank to others as well. Thank you!",fg="Dark Blue", bd=5, anchor='w')
	lblInfo.grid(row=0,column=0)
	lblInfo = Label(f2,font=('arial',20,'bold'),text="Select one of the following options:",fg="orange", bd=2,anchor='n')
	lblInfo.grid(row=2,column=0)


	def qExit():
	    root.destroy()

	def Login():
		root.destroy()
		os.chdir(path1)
		login()

	def Create():
		root.destroy()
		os.chdir(path1)
		create_acc()



	btnCreate=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
	                text="Create Account", bg="orange",command =Create).grid(row=3,column=0)

	btnLogin=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
	                text="Login", bg="orange",command =Login).grid(row=5,column=0)

	btnExit=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
	                text="Exit", bg="orange",command =qExit).grid(row=7,column=0)


	root.mainloop()


def menu2(acc1):
	root= Tk()
	root.geometry("1600x800+0+0")
	root.title("Epicness Bank")
	Tops = Frame(root, width = 1600,height = 50)
	Tops.pack(side=TOP)

	f0 = Frame(root, width = 800,height = 75, relief=SUNKEN)
	f0.pack(side=TOP)
	f2 = Frame(root, width = 800,height = 50, relief=SUNKEN)
	f2.pack(side=TOP)
	f1 = Frame(root, width = 600,height = 400, relief=SUNKEN)
	f1.pack(side=TOP)

	lblInfo = Label(Tops, font=('arial',30,'bold'),text="Refer our bank to others as well. Thank you!",fg="Dark Blue", bd=5, anchor='w')
	lblInfo.grid(row=0,column=0)
	lblInfo = Label(f2,font=('arial',20,'bold'),text="You have successfully logged in.",fg="orange", bd=2,anchor='n')
	lblInfo.grid(row=1,column=0)
	lblInfo = Label(f2,font=('arial',20,'bold'),text="Select one of the following options:",fg="orange", bd=2,anchor='n')
	lblInfo.grid(row=2,column=0)


	def qExit():
	    root.destroy()

	def Login():
		root.destroy()
		os.chdir(path1)
		login()

	def Create():
		root.destroy()
		os.chdir(path1)
		create_acc()

	def Deposit():
		root.destroy()
		deposit(acc1)

	def Withdraw():
		root.destroy()
		withdraw(acc1)

	def Display():
		root.destroy()
		display(acc1)

	def Transfer():
		root.destroy()
		transfer(acc1)

	btnDeposit=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=15,
	                text="Deposit", bg="orange",command =Deposit).grid(row=3,column=0)

	btnWithdraw=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=15,
	                text="Withdraw", bg="orange",command =Withdraw).grid(row=4,column=0)

	btnTransfer=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=15,
	                text="Transfer", bg="orange",command =Transfer).grid(row=5,column=0)

	btnDisplay=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=25,
	                text="Display transaction history", bg="orange",command =Display).grid(row=6,column=0)

	btnCreate=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=30,
	                text="Logout and create another account", bg="orange",command =Create).grid(row=7,column=0)

	btnLogin=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=30,
	                text="Logout and log in to another account", bg="orange",command =Login).grid(row=8,column=0)

	btnExit=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
	                text="Exit", bg="orange",command =qExit).grid(row=9,column=0)


	root.mainloop()


def login():
	root= Tk()
	root.geometry("1600x800+0+0")
	root.title("Epicness Bank")
	Tops = Frame(root, width = 1600,height = 50)
	Tops.pack(side=TOP)

	f0 = Frame(root, width = 800,height = 100, relief=SUNKEN)
	f0.pack(side=TOP)
	f5 = Frame(root, width = 800,height = 50, relief=SUNKEN)
	f5.pack(side=TOP)
	f1 = Frame(root, width = 400,height = 50, relief=SUNKEN)
	f1.pack(side=LEFT)
	f2 = Frame(root, width = 400,height = 50, relief=SUNKEN)
	f2.pack(side=RIGHT)
	f3 = Frame(root, width = 800,height = 50, relief=SUNKEN)
	f3.pack(side=BOTTOM)

	global path2
	global v
	global a1
	v=0
	lblInfo = Label(Tops, font=('arial',50,'bold'),text="Login portal",fg="Dark Blue", bd=5, anchor='w')
	lblInfo.grid(row=0,column=0)
	lblInfo = Label(f5,font=('arial',20,'bold'),text="Enter your account number first.",fg="orange", bd=2,anchor='n')
	lblInfo.grid(row=1,column=0)
	lblInfo = Label(f1,font=('arial',20,'bold'),text="Enter your account number.",fg="orange", bd=2,anchor='n')
	lblInfo.grid(row=0,column=0)
	lblInfo = Label(f2,font=('arial',20,'bold'),text="Enter your password.",fg="orange", bd=2,anchor='n')
	lblInfo.grid(row=0,column=0)

	password=StringVar()
	acc=StringVar()
	acc1=""
	txtacc=Entry(f1,font=('arial', 16,'bold'),textvariable=acc, bd=10, insertwidth=4,bg="orange", justify = 'right')
	txtacc.grid(row=1,column=0)
	txtpass=Entry(f2,font=('arial', 16,'bold'),textvariable=password, bd=10, insertwidth=4,bg="orange", justify = 'right')
	txtpass.grid(row=1,column=0)


	def qExit():
	    root.destroy()


	def submita():
		a=(acc.get())
		acc1=a
		global path2
		global a1
		a1=acc1
		path2=path1+"/"+a
		if(os.path.exists(path2)):
			os.chdir(path2)
			lblInfo = Label(f5,font=('arial',20,'bold'),text="----------------------------Enter your password now.----------------------------",fg="orange", bd=2,anchor='n')
			lblInfo.grid(row=1,column=0)
		else:
			lblInfo = Label(f5,font=('arial',20,'bold'),text="The account number you entered doesn't exist. Please Try again.",fg="Red", bd=2,anchor='n')
			lblInfo.grid(row=1,column=0)


	def submitp():
		p=(password.get())
		f1=open("pass.txt","r+")
		x=f1.read()
		f1.close()
		if(x==p):
			lblInfo = Label(f5,font=('arial',20,'bold'),text="------------------------------You have successfully logged in.------------------------------",fg="orange", bd=2,anchor='n')
			lblInfo.grid(row=1,column=0)
			global v
			v=1
		else:
			lblInfo = Label(f5,font=('arial',20,'bold'),text="---------------------------The password you entered is incorrect.---------------------------",fg="red", bd=2,anchor='n')
			lblInfo.grid(row=1,column=0)

	def Next():
	    global v
	    if(v==1):
	    	root.destroy()
	    	menu2(acc1)
	    	v=0
	    else:
	    	lblInfo = Label(f5,font=('arial',20,'bold'),text="---------------------------Please enter your password.---------------------------",fg="orange", bd=2,anchor='n')
	    	lblInfo.grid(row=1,column=0)



	btnSubmitp=Button(f2,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=15,
	                text="Submit Password", bg="orange",command =submitp).grid(row=6,column=0)

	btnSubmita=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=19,
	                text="Submit Account Number", bg="orange",command =submita).grid(row=6,column=0)

	btnNext=Button(f3,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
	                text="Next", bg="orange",command =Next).grid(row=10,column=1)

	btnExit=Button(f3,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
	                text="Exit", bg="orange",command =qExit).grid(row=11,column=1)


	root.mainloop()


def deposit(acc1):
	root= Tk()
	root.geometry("1600x800+0+0")
	root.title("Epicness Bank")
	Tops = Frame(root, width = 1600,height = 50)
	Tops.pack(side=TOP)


	f0 = Frame(root, width = 800,height = 100, relief=SUNKEN)
	f0.pack(side=TOP)
	f5 = Frame(root, width = 800,height = 50, relief=SUNKEN)
	f5.pack(side=TOP)
	f1 = Frame(root, width = 400,height = 50, relief=SUNKEN)
	f1.pack(side=TOP)

	f3 = Frame(root, width = 800,height = 50, relief=SUNKEN)
	f3.pack(side=BOTTOM)

	lblInfo = Label(Tops, font=('arial',50,'bold'),text="Deposit Window",fg="Dark Blue", bd=5, anchor='w')
	lblInfo.grid(row=0,column=0)
	lblInfo = Label(f5,font=('arial',20,'bold'),text="Enter the amount to be deposited.",fg="orange", bd=2,anchor='n')
	lblInfo.grid(row=1,column=0)
	lblInfo = Label(f1,font=('arial',20,'bold'),text="Enter the deposit amount.",fg="orange", bd=2,anchor='n')
	lblInfo.grid(row=0,column=0)
	dep=StringVar()
	txtdep=Entry(f1,font=('arial', 16,'bold'),textvariable=dep, bd=10, insertwidth=4,bg="orange", justify = 'right')
	txtdep.grid(row=1,column=0)

	def qExit():
	    root.destroy()

	def Next():
	    root.destroy()
	    menu2(acc1)

	def Create():
		root.destroy()
		create_acc()

	def Submitd():
		f1=open("bal.txt","r+")
		f2=open("hist.txt","a+")
		bal=int(f1.read())
		f1.close()
		d1=int(dep.get())
		bal=bal+d1
		d1=str(d1)
		bal=str(bal)
		x="You just deposited "+d1+"."
		y="Your current balance is "+bal+"."
		z=x+" "+y
		lblInfo = Label(f5,font=('arial',20,'bold'),text=z,fg="orange", bd=2,anchor='n')
		lblInfo.grid(row=1,column=0)
		f2.write(x+"\n"+y+"\n")
		f3=open("bal.txt","w+")
		f3.write(bal)
		f2.close()
		f3.close()



	btnSubmitd=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=25,
	                text="Submit Deposit Amount", bg="orange",command =Submitd).grid(row=6,column=0)

	btnNext=Button(f3,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
	                text="Next", bg="orange",command =Next).grid(row=10,column=1)

	btnExit=Button(f3,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
	                text="Exit", bg="orange",command =qExit).grid(row=11,column=1)


	root.mainloop()


def withdraw(acc1):
	root= Tk()
	root.geometry("1600x800+0+0")
	root.title("Epicness Bank")
	Tops = Frame(root, width = 1600,height = 50)
	Tops.pack(side=TOP)


	f0 = Frame(root, width = 800,height = 100, relief=SUNKEN)
	f0.pack(side=TOP)
	f5 = Frame(root, width = 800,height = 50, relief=SUNKEN)
	f5.pack(side=TOP)
	f1 = Frame(root, width = 400,height = 50, relief=SUNKEN)
	f1.pack(side=LEFT)
	f2 = Frame(root, width = 400,height = 50, relief=SUNKEN)
	f2.pack(side=RIGHT)
	f3 = Frame(root, width = 800,height = 50, relief=SUNKEN)
	f3.pack(side=BOTTOM)

	lblInfo = Label(Tops, font=('arial',50,'bold'),text="Withdrawal Window",fg="Dark Blue", bd=5, anchor='w')
	lblInfo.grid(row=0,column=0)
	lblInfo = Label(f5,font=('arial',20,'bold'),text="Enter the amount to be withdrawn.",fg="orange", bd=2,anchor='n')
	lblInfo.grid(row=1,column=0)
	lblInfo = Label(f1,font=('arial',20,'bold'),text="Enter the withdrawal amount.",fg="orange", bd=2,anchor='n')
	lblInfo.grid(row=0,column=0)
	wit=StringVar()
	txtwit=Entry(f1,font=('arial', 16,'bold'),textvariable=wit, bd=10, insertwidth=4,bg="orange", justify = 'right')
	txtwit.grid(row=1,column=0)

	def qExit():
	    root.destroy()

	def Next():
	    root.destroy()
	    menu2(acc1)

	def Create():
		root.destroy()
		create_acc()

	def Submitw():
		f1=open("bal.txt","r+")
		f2=open("hist.txt","a+")
		bal=int(f1.read())
		f1.close()
		w1=int(wit.get())
		if(w1<bal):
			bal=bal-w1
			w1=str(w1)
			bal=str(bal)
			m="---------------------------"
			x="You just withdrew "+w1+"."
			y="Your current balance is "+bal+"."
			z=m+x+" "+y+m
			lblInfo = Label(f5,font=('arial',15,'bold'),text=z,fg="orange", bd=2,anchor='n')
			lblInfo.grid(row=1,column=0)
			f2.write(x+"\n"+y+"\n")
			f3=open("bal.txt","w+")
			f3.write(bal)
			f2.close()
			f3.close()
		else:
			bal=str(bal)
			x="You can't withdraw more than your balance amount. Please try again keeping in mind you balance is "+bal+"."
			lblInfo = Label(f5,font=('arial',15,'bold'),text=x,fg="red", bd=2,anchor='n')
			lblInfo.grid(row=1,column=0)
			f2.close()



	btnSubmitw=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=25,
	                text="Submit Withdrawal Amount", bg="orange",command =Submitw).grid(row=6,column=0)

	btnNext=Button(f3,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
	                text="Next", bg="orange",command =Next).grid(row=10,column=1)

	btnExit=Button(f3,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
	                text="Exit", bg="orange",command =qExit).grid(row=11,column=1)


	root.mainloop()


def transfer(acc1):
	root= Tk()
	root.geometry("1600x800+0+0")
	root.title("Epicness Bank")
	Tops = Frame(root, width = 1600,height = 50)
	Tops.pack(side=TOP)
	global a5
	global path2

	f0 = Frame(root, width = 800,height = 100, relief=SUNKEN)
	f0.pack(side=TOP)
	f5 = Frame(root, width = 800,height = 50, relief=SUNKEN)
	f5.pack(side=TOP)
	f1 = Frame(root, width = 400,height = 50, relief=SUNKEN)
	f1.pack(side=LEFT)
	f2 = Frame(root, width = 400,height = 50, relief=SUNKEN)
	f2.pack(side=RIGHT)
	f3 = Frame(root, width = 800,height = 50, relief=SUNKEN)
	f3.pack(side=BOTTOM)

	lblInfo = Label(Tops, font=('arial',50,'bold'),text="Transfer Window",fg="Dark Blue", bd=5, anchor='w')
	lblInfo.grid(row=0,column=0)
	lblInfo = Label(f5,font=('arial',20,'bold'),text="Enter the account number.",fg="orange", bd=2,anchor='n')
	lblInfo.grid(row=1,column=0)
	lblInfo = Label(f1,font=('arial',20,'bold'),text="Enter the account to be transferred to.",fg="orange", bd=2,anchor='n')
	lblInfo.grid(row=0,column=0)
	lblInfo = Label(f2,font=('arial',20,'bold'),text="Enter the transfer amount.",fg="orange", bd=2,anchor='n')
	lblInfo.grid(row=0,column=0)
	a2=""
	print(path1)
	tra=StringVar()
	acc2=StringVar()
	txtacc=Entry(f1,font=('arial', 16,'bold'),textvariable=acc2, bd=10, insertwidth=4,bg="orange", justify = 'right')
	txtacc.grid(row=1,column=0)
	txttra=Entry(f2,font=('arial', 16,'bold'),textvariable=tra, bd=10, insertwidth=4,bg="orange", justify = 'right')
	txttra.grid(row=1,column=0)

	def qExit():
	    root.destroy()

	def Next():
	    root.destroy()
	    menu2(acc1)

	def Submitacc():
		path2=os.getcwd()
		global a5
		global path5
		a5=acc2.get()
		a3="/"+a5
		path5 = path5+a3
		if(os.path.exists(path5)):
			lblInfo = Label(f5,font=('arial',15,'bold'),text="---------------------------Enter the amount to be transferred now.---------------------------",fg="orange", bd=2,anchor='n')
			lblInfo.grid(row=1,column=0)
		else:
			lblInfo = Label(f5,font=('arial',15,'bold'),text="The account number you entered doesn't exist. Please try again.",fg="red", bd=2,anchor='n')
			lblInfo.grid(row=1,column=0)


	def Submitt():
		f1=open("bal.txt","r+")
		f2=open("hist.txt","a+")
		bal=int(f1.read())
		f1.close()
		global a5
		global a1
		global path2
		global path5
		t1=int(tra.get())
		if(t1<bal):
			bal=bal-t1
			t1=str(t1)
			bal=str(bal)
			m="----------------------------"
			x="You just transferred "+t1+" to ACC-"+a5+"."
			y="Your current balance is "+bal+"."
			z=m+x+" "+y+m
			lblInfo = Label(f5,font=('arial',15,'bold'),text=z,fg="orange", bd=2,anchor='n')
			lblInfo.grid(row=1,column=0)
			f2.write(x+"\n"+y+"\n")
			f3=open("bal.txt","w+")
			f3.write(bal)
			f2.close()
			f3.close()
			t1=int(t1)
			os.chdir(path5)
			f4=open("bal.txt","r+")
			bal1=int(f4.read())
			f4.close()
			f4=open("bal.txt","w+")
			f6=open("hist.txt","a+")
			bal1=bal1+t1
			bal1=str(bal1)
			t1=str(t1)
			f6.write(t1+" was transfered to your account from ACC-"+a1+".\nYour current balance is "+bal1+".\n")
			f4.write(bal1)
			f4.close()
			f6.close()
			path5=path1
			os.chdir(path2)
		else:
			bal=str(bal)
			x="You can't transfer more than your balance amount. Please try again keeping in mind you balance is "+bal+"."
			lblInfo = Label(f5,font=('arial',15,'bold'),text=x,fg="red", bd=2,anchor='n')
			lblInfo.grid(row=1,column=0)
			f2.close()



	btnSubmitacc=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=25,
	                text="Submit Account Number", bg="orange",command =Submitacc).grid(row=6,column=0)

	btnSubmitt=Button(f2,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=25,
	                text="Submit Transfer Amount", bg="orange",command =Submitt).grid(row=6,column=0)

	btnNext=Button(f3,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
	                text="Next", bg="orange",command =Next).grid(row=10,column=1)

	btnExit=Button(f3,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
	                text="Exit", bg="orange",command =qExit).grid(row=11,column=1)


	root.mainloop()




def display(acc1):
	root= Tk()
	root.geometry("1600x800+0+0")
	root.title("Epicness Bank")
	Tops = Frame(root, width = 1600,height = 50)
	Tops.pack(side=TOP)


	f0 = Frame(root, width = 800,height = 100, relief=SUNKEN)
	f0.pack(side=TOP)
	f5 = Frame(root, width = 200,height = 500, relief=SUNKEN)
	f5.pack(side=TOP)
	f1 = Frame(root, width = 400,height = 50, relief=SUNKEN)
	f1.pack(side=LEFT)
	f2 = Frame(root, width = 400,height = 50, relief=SUNKEN)
	f2.pack(side=RIGHT)
	f3 = Frame(root, width = 800,height = 50, relief=SUNKEN)
	f3.pack(side=BOTTOM)

	lblInfo = Label(Tops, font=('arial',50,'bold'),text="Transaction History",fg="Dark Blue", bd=5, anchor='w')
	lblInfo.grid(row=0,column=0)


	def qExit():
	    root.destroy()

	def Next():
	    root.destroy()
	    menu2(acc1)

	def Display():
		f2=open("hist.txt","r+")
		m=3
		n=0
		for line in f2:
			lblInfo = Label(f5, font=('arial',10,'bold'),text=line,fg="Black", bd=5, anchor='e')
			lblInfo.grid(row=m,column=n%3)
			n+=1
			if(n%3==0):
				m+=1
		f2.close()

	btnDisplay=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=20,
	                text="Display the history", bg="orange",command =Display).grid(row=2,column=1)

	btnNext=Button(f2,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
	                text="Next", bg="orange",command =Next).grid(row=16,column=1)

	btnExit=Button(f2,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
	                text="Exit", bg="orange",command =qExit).grid(row=17,column=1)


	root.mainloop()


root= Tk()
root.geometry("1600x800+0+0")
root.title("Epicness Bank")


if(t==1):
	Tops = Frame(root, width = 1600,height = 50)
	Tops.pack(side=TOP)

	f0 = Frame(root, width = 800,height = 200, relief=SUNKEN)
	f0.pack(side=TOP)
	f1 = Frame(root, width = 800,height = 500, relief=SUNKEN)
	f1.pack(side=TOP)

	lblInfo = Label(Tops, font=('arial',50,'bold'),text="Welcome to Epicness Bank",fg="Dark Blue", bd=5, anchor='w')
	lblInfo.grid(row=0,column=0)
	lblInfo = Label(Tops,font=('arial',20,'bold'),text="We currently don't have any accounts. Please create one.",fg="orange", bd=2,anchor='w')
	lblInfo.grid(row=1,column=0)

	def qExit():
	    root.destroy()

	def Create():
		root.destroy()
		create_acc()


	btnCreate=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=15,
	                text="Create Account", bg="orange",command =Create).grid(row=3,column=3)

	btnExit=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
	                text="Exit", bg="orange",command =qExit).grid(row=7,column=3)
	root.mainloop()

else:
	Tops = Frame(root, width = 1600,height = 50)
	Tops.pack(side=TOP)

	f0 = Frame(root, width = 800,height = 200, relief=SUNKEN)
	f0.pack(side=TOP)
	f1 = Frame(root, width = 800,height = 500, relief=SUNKEN)
	f1.pack(side=TOP)


	lblInfo = Label(Tops, font=('arial',50,'bold'),text="Welcome to Epicness Bank",fg="Dark Blue", bd=5, anchor='w')
	lblInfo.grid(row=0,column=0)
	lblInfo = Label(Tops,font=('arial',20,'bold'),text="Select one of the following options:",fg="orange", bd=2,anchor='w')
	lblInfo.grid(row=1,column=0)

	def qExit():
	    root.destroy()

	def Login():
		root.destroy()
		login()

	def Create():
		root.destroy()
		create_acc()



	btnCreate=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=15,
	                text="Create Account", bg="orange",command =Create).grid(row=3,column=3)

	btnLogin=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
	                text="Login", bg="orange",command =Login).grid(row=5,column=3)

	btnExit=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
	                text="Exit", bg="orange",command =qExit).grid(row=7,column=3)
	root.mainloop()
