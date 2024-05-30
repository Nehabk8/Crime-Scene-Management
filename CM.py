from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("Crime Scene Management")
root.geometry("1530x720+0+0")
    
lbltitle=Label(root, bd=20, relief=RIDGE, text='Crime Scene Management', fg='black', bg="yellow", font=("times new roman",50, "bold"))
lbltitle. pack(side=TOP, fill=X)

#dataframe
Dataframe=Frame(root, bd=20, relief=RIDGE,bg='yellow')
Dataframe.place(x=0, y=120, width=1530, height=400)

DataframeLeft=LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman",12, "bold"),bg='yellow')
DataframeLeft.place(x=0, y=5, width=1490, height=350)

#buttons frame
Buttonframe=Frame(root, bd=20, relief=RIDGE,bg='yellow')
Buttonframe. place(x=0, y=530, width=1530, height=70)

#details frame

Detailsframe=Frame(root, bd=20, relief=RIDGE,bg='yellow')
Detailsframe.place(x=0, y=600, width=1530, height=120)

#leftDF

lblNameUserID=Label(DataframeLeft, text="User ID: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameUserID.grid(row=0, column=0)
txtID=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtID.grid(row=0, column=1)

lblNameUserf=Label(DataframeLeft, text="First Name: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameUserf.grid(row=1, column=0)
txtf=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtf.grid(row=1, column=1)

lblNameUserm=Label(DataframeLeft, text="Midlle Name: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameUserm. grid(row=2, column=0)
txtm=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtm.grid(row=2, column=1)

lblNameUserl=Label(DataframeLeft, text="Last name: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameUserl. grid(row=3, column=0)
txtl=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtl.grid(row=3, column=1)

lblNameUsermail=Label(DataframeLeft, text="Email: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameUsermail. grid(row=4, column=0)
txtmail=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtmail.grid(row=4, column=1)

lblNameUseradd=Label(DataframeLeft, text="Address: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameUseradd.grid(row=5, column=0)
txtadd=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtadd.grid(row=5, column=1)

lblNameUserPh=Label(DataframeLeft, text="Phone: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameUserPh.grid(row=6, column=0)
txtPh=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtPh.grid(row=6, column=1)

#leftdhc2
lblNameCaseID=Label(DataframeLeft, text="Case ID: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameCaseID.grid(row=0, column=2)
txtcID=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtcID.grid(row=0, column=3)

lblNameCCID=Label(DataframeLeft, text="Case Crime ID: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameCCID.grid(row=1, column=2)
txtCC=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtCC.grid(row=1, column=3)

lblNameType=Label(DataframeLeft, text="Case Type", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameType.grid(row=2, column=2)
txtTY=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtTY.grid(row=2, column=3)

lblNameDes=Label(DataframeLeft, text="Case Description: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameDes.grid(row=3, column=2)
txtDes=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtDes.grid(row=3, column=3)

lblNameCn=Label(DataframeLeft, text="Case Name: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameCn.grid(row=4, column=2)
txtCn=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtCn.grid(row=4, column=3)

lblPID=Label(DataframeLeft, text="POLICE ID: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblPID. grid(row=5, column=2)
txtPId=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtPId. grid(row=5, column=3)

lblNameUID=Label(DataframeLeft, text="User ID: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameUID. grid(row=6, column=2)
txtUID=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtUID.grid(row=6, column=3)

#leftdhc3
lblNameCaseID2=Label(DataframeLeft, text="Criminal Id: : ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameCaseID2.grid(row=0, column=4)
txtcID2=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtcID2.grid(row=0, column=5)

lblNameCCID2=Label(DataframeLeft, text="First Name: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameCCID2. grid(row=1, column=4)
txtCC2=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtCC2. grid(row=1, column=5)

lblNameType2=Label(DataframeLeft, text="Middle Name", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameType2. grid(row=2, column=4)
txtTY2=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtTY2. grid(row=2, column=5)

lblNameDes2=Label(DataframeLeft, text="Last Name: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameDes2. grid(row=3, column=4)
txtDes2=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtDes2. grid(row=3, column=5)

lblNameCn2=Label(DataframeLeft, text="Criminal address: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameCn2. grid(row=4, column=4)
txtCn2=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtCn2. grid(row=4, column=5)

lblPID2=Label(DataframeLeft, text="criminal mail: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblPID2. grid(row=5, column=4)
txtPId2=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtPId2. grid(row=5, column=5)

lblNameUID2=Label(DataframeLeft, text="criminal pass: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameUID2. grid(row=6, column=4)
txtUID2=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtUID2. grid(row=6, column=5)

lblNameUID22=Label(DataframeLeft, text="criminal mobile: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameUID22. grid(row=7, column=4)
txtUID22=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtUID22. grid(row=7, column=5)

lblNameUID23=Label(DataframeLeft, text="Police ID: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameUID23. grid(row=0, column=6)
txtUID23=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtUID23. grid(row=0, column=7)

lblNameUID24=Label(DataframeLeft, text="Duration: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameUID24. grid(row=1, column=6)
txtUID24=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtUID24. grid(row=1, column=7)

#leftdhc4
lblNameCaseID37=Label(DataframeLeft, text="Victim ID: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameCaseID37. grid(row=3, column=6)
txtcID37=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtcID37. grid(row=3, column=7)



lblNameCaseID3=Label(DataframeLeft, text="Victim: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameCaseID3. grid(row=4, column=6)
txtcID3=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtcID3. grid(row=4, column=7)

lblNameCCID3=Label(DataframeLeft, text="Evidence: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameCCID3. grid(row=5, column=6)
txtCC3=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtCC3. grid(row=5, column=7)

lblNameType3=Label(DataframeLeft, text="Loaction", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameType3. grid(row=6, column=6)
txtTY3=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtTY3. grid(row=6, column=7)

#leftdhc5
lblNameCaseID4=Label(DataframeLeft, text="Police ID: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameCaseID4. grid(row=0, column=8)
txtcID4=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtcID4. grid(row=0, column=9)

lblNameCCID4=Label(DataframeLeft, text="Police Pass: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameCCID4. grid(row=1, column=8)
txtCC4=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtCC4. grid(row=1, column=9)

lblNameType4=Label(DataframeLeft, text="Police Address: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameType4. grid(row=2, column=8)
txtTY4=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtTY4. grid(row=2, column=9)

lblNameDes4=Label(DataframeLeft, text="Poice Dept Id: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameDes4. grid(row=3, column=8)
txtDes4=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtDes4. grid(row=3, column=9)

lblNameCn4=Label(DataframeLeft, text="Police Mobile: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameCn4. grid(row=4, column=8)
txtCn4=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtCn4. grid(row=4, column=9)

lblPID4=Label(DataframeLeft, text="Location: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblPID4. grid(row=5, column=8)
txtPId4=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtPId4. grid(row=5, column=9)

#leftdhc6
lblNameCaseID5=Label(DataframeLeft, text="Criminal ID: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameCaseID5. grid(row=0, column=10)
txtcID5=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtcID5. grid(row=0, column=11)

lblNameCCID5=Label(DataframeLeft, text="Case ID: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameCCID5. grid(row=1, column=10)
txtCC5=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtCC5. grid(row=1, column=11)

lblNameType5=Label(DataframeLeft, text="Start Date: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameType5. grid(row=2, column=10)
txtTY5=Entry(DataframeLeft, font=("arial",12, "bold"), width=12)
txtTY5. grid(row=2, column=11)

#buttonsLEFTC
btnIns=Button(DataframeLeft, text='Insert', bg='green', fg='white', font=("times new roman",12, "bold"), command=lambda: [CrimeData1(txtID,txtf,txtm,txtl,txtmail,txtadd,txtPh),messagebox.showinfo("USER","Record Added"),ClearData1(txtID,txtf,txtm,txtl,txtmail,txtadd,txtPh)], width=12, padx=1, pady=4)
btnIns. grid(row=7, column=1)

#buttonsLEFTC2
btnIns1=Button(DataframeLeft, text='Insert', bg='green', fg='white', font=("times new roman",12, "bold"), command=lambda: [CrimeData(txtcID,txtCC,txtTY,txtDes,txtCn,txtPId,txtUID),messagebox.showinfo("CASE","Record Added"),ClearData(txtcID,txtCC,txtTY,txtDes,txtCn,txtPId,txtUID)], width=12, padx=1, pady=4)
btnIns1. grid(row=7, column=3)

#buttonsLEFTC3
btnIns2=Button(DataframeLeft, text='Insert', bg='green', fg='white', font=("times new roman",12, "bold"), command=lambda:[ CrimeData2(txtcID2, txtCC2, txtTY2, txtDes2, txtCn2, txtPId2, txtUID2, txtUID22, txtUID23, txtUID24),messagebox.showinfo("CRIMINAL","Record Added"),ClearData2(txtcID2, txtCC2, txtTY2, txtDes2, txtCn2, txtPId2, txtUID2, txtUID22, txtUID23, txtUID24)], width=15, padx=1, pady=4)
btnIns2. grid(row=2, column=7)

#buttonsLEFTC4
btnIns3=Button(DataframeLeft, text='Insert', bg='green', fg='white', font=("times new roman",12, "bold"), command=lambda: [CrimeData3(txtcID37,txtcID3, txtCC3, txtTY3),messagebox.showinfo("CRIME SCENE","Record Added"),ClearData3(txtcID3, txtCC3, txtTY3)], width=12, padx=1, pady=4)
btnIns3. grid(row=7, column=7)

#buttonsLEFTC4
btnIns4=Button(DataframeLeft, text='Insert', bg='green', fg='white', font=("times new roman",12, "bold"), command=lambda: [CrimeData4(txtcID4, txtCC4, txtTY4, txtDes4, txtCn4, txtPId4),messagebox.showinfo("POLICE","Record Added"),ClearData4(txtcID4, txtCC4, txtTY4, txtDes4, txtCn4, txtPId4)], width=12, padx=1, pady=4)
btnIns4. grid(row=7, column=9)

#buttonsLEFTC4
btnIns5=Button(DataframeLeft, text='Insert', bg='green', fg='white', font=("times new roman",12, "bold"), command=lambda:[ CrimeData5(txtcID5, txtCC5, txtTY5),messagebox.showinfo("INVOLVES","Record Added"),ClearData5(txtcID5, txtCC5, txtTY5)], width=12, padx=1, pady=4)
btnIns5. grid(row=7, column=11)
        
#delete frame

lblNameUserID71=Label(Detailsframe, text="User ID: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameUserID71. grid(row=0, column=0)
txtID71=Entry(Detailsframe, font=("arial",12, "bold"), width=16)
txtID71. grid(row=0, column=1)

btnd12=Button(Detailsframe, text='Delete', bg='green', fg='white', font=("times new roman",12, "bold"), command=lambda: [DeleteData1(txtID71),messagebox.showinfo("Deleted","Record deleted"),ClearData6(txtID71,txtcID72,txtcID73,txtcID74,txtcID75,txtcID76)], width=16, padx=1, pady=4)
btnd12. grid(row=1, column=1)

lblNameCaseID72=Label(Detailsframe, text="Case ID: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameCaseID72. grid(row=0, column=2)
txtcID72=Entry(Detailsframe, font=("arial",12, "bold"), width=16)
txtcID72. grid(row=0, column=3)


btnd22=Button(Detailsframe, text='Delete', bg='green', fg='white', font=("times new roman",12, "bold"), command=lambda: [DeleteData(txtcID72),messagebox.showinfo("Deleted","Record deleted"),ClearData6(txtID71,txtcID72,txtcID73,txtcID74,txtcID75,txtcID76)], width=16, padx=1, pady=4)
btnd22.grid(row=1, column=3)



lblNameCaseID73=Label(Detailsframe, text="Criminal Id: : ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameCaseID73. grid(row=0, column=4)
txtcID73=Entry(Detailsframe, font=("arial",12, "bold"), width=16)
txtcID73.grid(row=0, column=5)


btnd32=Button(Detailsframe, text='Delete', bg='green', fg='white', font=("times new roman",12, "bold"),command=lambda: [DeleteData2(txtcID73),messagebox.showinfo("Deleted","Record deleted"),ClearData6(txtID71,txtcID72,txtcID73,txtcID74,txtcID75,txtcID76)], width=16, padx=1, pady=4)
btnd32.grid(row=1, column=5)

lblNameCaseID74=Label(Detailsframe, text="Victim: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameCaseID74.grid(row=0, column=6)
txtcID74=Entry(Detailsframe, font=("arial",12, "bold"), width=16)
txtcID74.grid(row=0, column=7)


btnd42=Button(Detailsframe, text='Delete', bg='green', fg='white', font=("times new roman",12, "bold"), command=lambda: [DeleteData3(txtcID74),messagebox.showinfo("Deleted","Record deleted"),ClearData6(txtID71,txtcID72,txtcID73,txtcID74,txtcID75,txtcID76)], width=16, padx=1, pady=4)
btnd42.grid(row=1, column=7)


lblNameCaseID75=Label(Detailsframe, text="Police ID: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameCaseID75.grid(row=0, column=8)
txtcID75=Entry(Detailsframe, font=("arial",12, "bold"), width=16)
txtcID75.grid(row=0, column=9)

btnd52=Button(Detailsframe, text='Delete', bg='green', fg='white', font=("times new roman",12, "bold"), command=lambda: [DeleteData4(txtcID75),messagebox.showinfo("Deleted","Record deleted"),ClearData6(txtID71,txtcID72,txtcID73,txtcID74,txtcID75,txtcID76)], width=16, padx=1, pady=4)
btnd52.grid(row=1, column=9)


lblNameCaseID76=Label(Detailsframe, text="Criminal ID: ", font=("times new roman",12, "bold"), padx=2, pady=6,bg='yellow')
lblNameCaseID76.grid(row=0, column=10)
txtcID76=Entry(Detailsframe, font=("arial",12, "bold"), width=16)
txtcID76.grid(row=0, column=11)


btnd62=Button(Detailsframe, text='Delete', bg='green', fg='white', font=("times new roman",12, "bold"), command=lambda:  [DeleteData5(txtcID76),messagebox.showinfo("Deleted","Record deleted"),ClearData6(txtID71,txtcID72,txtcID73,txtcID74,txtcID75,txtcID76)], width=16, padx=1, pady=4)
btnd62.grid(row=1, column=11)


# Display Buttons
btnd=Button(Buttonframe,text='Display ALL',bg='green',fg='white',command=lambda: disp(),font=("times new roman",12,"bold"),width=26,padx=1,pady=4)
btnd.grid()
        
btnd1=Button(Buttonframe,text='Display ALL',bg='green',fg='white',command=lambda: disp1(),font=("times new roman",12,"bold"),width=26,padx=1,pady=4)
btnd1.grid(row=0,column=1)
        
btnd2=Button(Buttonframe,text='Display ALL',bg='green',fg='white',command=lambda: disp2(),font=("times new roman",12,"bold"),width=26,padx=1,pady=4)
btnd2.grid(row=0,column=2)
        
btnd3=Button(Buttonframe,text='Display ALL',bg='green',fg='white',command=lambda: disp3(),font=("times new roman",12,"bold"),width=26,padx=1,pady=4)
btnd3.grid(row=0,column=3)
        
btnd4=Button(Buttonframe,text='Display ALL',bg='green',fg='white',command=lambda: disp4(),font=("times new roman",12,"bold"),width=26,padx=1,pady=4)
btnd4.grid(row=0,column=4)

btnd5=Button(Buttonframe,text='Display ALL',bg='green',fg='white',command=lambda: disp5(),font=("times new roman",12,"bold"),width=26,padx=1,pady=4)
btnd5.grid(row=0,column=5)



def disp():
    top=Toplevel()
    top.geometry("1600x800+0+0")
    top.title("USER TABLE")
    root.withdraw()
    myb1=Button(top,text='Close window',command=lambda:[root.deiconify(),top.destroy()]).pack()

def disp1():
    top=Toplevel()
    top.geometry("1600x800+0+0")
    top.title("CASE TABLE")
    root.withdraw()
    myb1=Button(top,text='Close window',command=lambda:[root.deiconify(),top.destroy()]).pack()


def disp2():
    top=Toplevel()
    top.geometry("1600x800+0+0")
    top.title("CRIMINAL TABLE")
    root.withdraw()
    myb1=Button(top,text='Close window',command=lambda:[root.deiconify(),top.destroy()]).pack()

def disp3():
    top=Toplevel()
    top.geometry("1600x800+0+0")
    top.title("CRIME SCENE TABLE")
    root.withdraw()
    myb1=Button(top,text='Close window',command=lambda:[root.deiconify(),top.destroy()]).pack()

def disp4():
    top=Toplevel()
    top.geometry("1600x800+0+0")
    top.title("POLICE TABLE")
    root.withdraw()
    myb1=Button(top,text='Close window',command=lambda:[root.deiconify(),top.destroy()]).pack()

def disp5():
    top=Toplevel()
    top.geometry("1600x800+0+0")
    top.title("INVOLVES TABLE")
    root.withdraw()
    myb1=Button(top,text='Close window',command=lambda:[root.deiconify(),top.destroy()]).pack()



#clear
def ClearData1(txtID,txtf,txtm,txtl,txtmail,txtadd,txtPh):
    txtID.delete(0,END)
    txtf.delete(0,END)
    txtm.delete(0,END)
    txtl.delete(0,END)
    txtmail.delete(0,END)
    txtadd.delete(0,END)
    txtPh.delete(0,END)

def ClearData2(txtcID2,txtCC2,txtTY2,txtDes2,txtCn2,txtPId2,txtUID2,txtUID22,txtUID23,txtUID24):
    txtcID2.delete(0,END)
    txtCC2.delete(0,END)
    txtTY2.delete(0,END)
    txtDes2.delete(0,END)
    txtCn2.delete(0,END)
    txtPId2.delete(0,END)
    txtUID2.delete(0,END)
    txtUID22.delete(0,END)
    txtUID23.delete(0,END)
    txtUID24.delete(0,END)


def ClearData(txtcID,txtCC,txtTY,txtDes,txtCn,txtPId,txtUID):
    txtcID.delete(0,END)
    txtCC.delete(0,END)
    txtTY.delete(0,END)
    txtDes.delete(0,END)
    txtCn.delete(0,END)
    txtPId.delete(0,END)
    txtUID.delete(0,END)

def ClearData3(txtcID3,txtCC3,txtTY3):
    txtcID37.delete(0,END)
    txtcID3.delete(0,END)
    txtCC3.delete(0,END)
    txtTY3.delete(0,END)

def ClearData4(txtcID4,txtCC4,txtTY4,txtDes4,txtCn4,txtPId4):
    txtcID4.delete(0,END)
    txtCC4.delete(0,END)
    txtTY4.delete(0,END)
    txtDes4.delete(0,END)
    txtCn4.delete(0,END)
    txtPId4.delete(0,END)

def ClearData5(txtcID5,txtCC5,txtTY5):
    txtcID5.delete(0,END)
    txtCC5.delete(0,END)
    txtTY5.delete(0,END)

def ClearData6(txtID71,txtcID72,txtcID73,txtcID74,txtcID75,txtcID76):
    txtID71.delete(0,END)
    txtcID72.delete(0,END)
    txtcID73.delete(0,END)
    txtcID74.delete(0,END)
    txtcID75.delete(0,END)
    txtcID76.delete(0,END)



def CrimeData(txtcID,txtCC,txtTY,txtDes,txtCn,txtPId,txtUID):
        
    conn=sqlite3.connect('crimeman2.db')
    c=conn.cursor()
    c.execute("INSERT INTO case2 VALUES(:cid,:ccid, :ctype,:casede,:casename,:polid,:userid)",
    {
    'cid':txtcID.get(),
    'ccid':txtCC.get(),
    'ctype':txtTY.get(),
    'casede':txtDes.get(),
    'casename':txtCn.get(),
    'polid':txtPId.get(),
    'userid':txtUID.get()
    })
    conn.commit()

    conn.close()


def CrimeData1(txtID,txtf,txtm,txtl,txtmail,txtadd,txtPh):
        
    conn=sqlite3.connect('crimeman2.db')
    c=conn.cursor()
    c.execute("INSERT INTO user values(:cid1,:ccid1, :ctype1,:casede1,:casename1,:polid1,:userid1)",{'cid1':txtID.get(),'ccid1':txtf.get(),'ctype1':txtm.get(),'casede1':txtl.get(),'casename1':txtmail.get(),'polid1':txtadd.get(),'userid1':txtPh.get()})
    conn.commit()

    conn.close()

def CrimeData2(txtcID2,txtCC2,txtTY2,txtDes2,txtCn2,txtPId2,txtUID2,txtUID22,txtUID23,txtUID24):
        
    conn=sqlite3.connect('crimeman2.db')
    c=conn.cursor()
    c.execute("INSERT INTO criminal VALUES(:cid2,:ccid2, :ctype2,:casede2,:casename2,:polid2,:userid2,:polide2,:uid2,:des2)",
    {
    'cid2':txtcID2.get(),
    'ccid2':txtCC2.get(),
    'ctype2':txtTY2.get(),
    'casede2':txtDes2.get(),
    'casename2':txtCn2.get(),
    'polid2':txtPId2.get(),
    'userid2':txtUID2.get(),
    'polide2':txtUID22.get(),
    'uid2':txtUID23.get(),
    'des2':txtUID24.get()
    })
    conn.commit()

    conn.close()

def CrimeData3(txtcID37,txtcID3,txtCC3,txtTY3):
        
    conn=sqlite3.connect('crimeman2.db')
    c=conn.cursor()
    c.execute("INSERT INTO crime_scene1 VALUES(:vid,:cid3,:ccid3, :ctype3)",
    {
    'vid':txtcID37.get(),
    'cid3':txtcID3.get(),
    'ccid3':txtCC3.get(),
    'ctype3':txtTY3.get(),
    })
    conn.commit()

    conn.close()


def CrimeData4(txtcID4,txtCC4,txtTY4,txtDes4,txtCn4,txtPId4):
        
    conn=sqlite3.connect('crimeman2.db')
    c=conn.cursor()
    c.execute("INSERT INTO police VALUES(:cid4,:ccid4, :ctype4,:casede4,:casename4,:polid4)",
    {
    'cid4':txtcID4.get(),
    'ccid4':txtCC4.get(),
    'ctype4':txtTY4.get(),
    'casede4':txtDes4.get(),
    'casename4':txtCn4.get(),
    'polid4':txtPId4.get(),

    })
    conn.commit()

    conn.close()

def CrimeData5(txtcID5,txtCC5,txtTY5):
        
    conn=sqlite3.connect('crimeman2.db')
    c=conn.cursor()
    c.execute("INSERT INTO involves VALUES(:cid5,:ccid5, :ctype5)",
    {
    'cid5':txtcID5.get(),
    'ccid5':txtCC5.get(),
    'ctype5':txtTY5.get(),
    })
    conn.commit()

    conn.close()

#delete Operation
def DeleteData(txtcID):
        
    conn=sqlite3.connect('crimeman2.db')
    c=conn.cursor()
    c.execute("DELETE FROM case2 WHERE case_id ="+txtcID.get())
    conn.commit()

    conn.close()

def DeleteData1(txtID):
        
    conn=sqlite3.connect('crimeman2.db')
    c=conn.cursor()
    c.execute("DELETE FROM user WHERE user_id ="+txtID.get())
    
    conn.commit()

    conn.close()

def DeleteData2(txtcID2):
        
    conn=sqlite3.connect('crimeman2.db')
    c=conn.cursor()
    c.execute("DELETE FROM criminal WHERE crm_id ="+txtcID2.get())

    
    conn.commit()

    conn.close()

def DeleteData3(txtcID3):
        
    conn=sqlite3.connect('crimeman2.db')
    c=conn.cursor()
    c.execute("DELETE FROM crime_scene1 WHERE victim_id ="+txtcID3.get())
    
    conn.commit()

    conn.close()


def DeleteData4(txtcID4):
        
    conn=sqlite3.connect('crimeman2.db')
    c=conn.cursor()
    c.execute("DELETE FROM police WHERE pol_id ="+txtcID4.get())
    conn.commit()

    conn.close()

def DeleteData5(txtcID5):
        
    conn=sqlite3.connect('crimeman2.db')
    c=conn.cursor()
    c.execute("DELETE FROM involves WHERE crm_id ="+txtcID5.get(),)
    conn.commit()

    conn.close()


def disp():
    top=Toplevel()
    top.geometry("1600x800+0+0")
    top.title("USER TABLE")
    root.withdraw()
    conn=sqlite3.connect('crimeman2.db')
    c=conn.cursor()
    r=c.execute("SELECT * FROM user")
    i=0
    for user in r:
        for j in range(len(user)):
            e=Entry(top,width=10,fg='blue')
            e.grid(row=i,column=j)
            e.insert(END,user[j])
        i=i+1


    conn.commit()

    conn.close()
    myb1=Button(top,text='Close window',command=lambda:[root.deiconify(),top.destroy()])
    myb1.grid(row=i+1,column=3)

def disp1():
    top=Toplevel()
    top.geometry("1600x800+0+0")
    top.title("USER TABLE")
    root.withdraw()
    df=Frame(top,bd=20,relief=RIDGE,bg='yellow')
    df.place(x=0,y=0,width=1600,height=750)
    conn=sqlite3.connect('crimeman2.db')
    c=conn.cursor()
    r=c.execute("SELECT * FROM case2")
   
    i=0
    for user in r:
        for j in range(len(user)):
            e=Entry(top,width=10,fg='blue')
            e.grid(row=i,column=j)
            e.insert(END,user[j])
        i=i+1


    conn.commit()

    conn.close()
    myb1=Button(top,text='Close window',command=lambda:[root.deiconify(),top.destroy()])
    myb1.grid(row=i+1,column=3)

def disp2():
    top=Toplevel()
    top.geometry("1600x800+0+0")
    top.title("USER TABLE")
    root.withdraw()
    conn=sqlite3.connect('crimeman2.db')
    c=conn.cursor()
    r=c.execute("SELECT * FROM criminal")
    i=0
    for user in r:
        for j in range(len(user)):
            e=Entry(top,width=10,fg='blue')
            e.grid(row=i,column=j)
            e.insert(END,user[j])
        i=i+1


    conn.commit()

    conn.close()
    myb1=Button(top,text='Close window',command=lambda:[root.deiconify(),top.destroy()])
    myb1.grid(row=i+1,column=3)

def disp3():
    top=Toplevel()
    top.geometry("1600x800+0+0")
    top.title("USER TABLE")
    root.withdraw()
    conn=sqlite3.connect('crimeman2.db')
    c=conn.cursor()
    r=c.execute("SELECT * FROM crime_scene1")
    i=0
    for user in r:
        for j in range(len(user)):
            e=Entry(top,width=10,fg='blue')
            e.grid(row=i,column=j)
            e.insert(END,user[j])
        i=i+1


    conn.commit()

    conn.close()
    myb1=Button(top,text='Close window',command=lambda:[root.deiconify(),top.destroy()])
    myb1.grid(row=i+1,column=3)


def disp4():
    top=Toplevel()
    top.geometry("1600x800+0+0")
    top.title("USER TABLE")
    root.withdraw()
    conn=sqlite3.connect('crimeman2.db')
    c=conn.cursor()
    r=c.execute("SELECT * FROM police")
    i=0
    for user in r:
        for j in range(len(user)):
            e=Entry(top,width=10,fg='blue')
            e.grid(row=i,column=j)
            e.insert(END,user[j])
        i=i+1


    conn.commit()

    conn.close()
    myb1=Button(top,text='Close window',command=lambda:[root.deiconify(),top.destroy()])
    myb1.grid(row=i+1,column=3)


def disp5():
    top=Toplevel()
    top.geometry("1600x800+0+0")
    top.title("USER TABLE")
    root.withdraw()
    conn=sqlite3.connect('crimeman2.db')
    c=conn.cursor()
    r=c.execute("SELECT * FROM involves")
    i=0
    for user in r:
        for j in range(len(user)):
            e=Entry(top,width=10,fg='blue')
            e.grid(row=i,column=j)
            e.insert(END,user[j])
        i=i+1


    conn.commit()

    conn.close()
    myb1=Button(top,text='Close window',command=lambda:[root.deiconify(),top.destroy()])
    myb1.grid(row=i+1,column=3)





mainloop()
 
        
        