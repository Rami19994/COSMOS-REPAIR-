from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import uuid

from datetime import datetime
from database import DataBase





root=Tk()

root.title("Cosmos Repair")
root.geometry("1410x800+10+10")
root.resizable(False,False)

root.configure(bg="#364768")
#enrtes frame sitting
entres_fram=Frame(root,bg="#d7d8b5")
entres_fram.place(x=0,y=0,width=1410,height=200)
#title for entres name
title=Label(entres_fram,text="job center",font=('Brush Script MT',22,'bold'),bg='#d7d8b5',fg='black')
title.place(x=520,y=3)

Data=DataBase("cosmos.db")


Costomer_Name=StringVar()
Phon_Number=StringVar()
Model=StringVar()
IMEI=StringVar()
SN=StringVar()
Warrenty_state=StringVar()
Fulty=StringVar()
Your_Servece=StringVar()
Item_Code =StringVar()
Descraption=StringVar()
Price_Dolar=StringVar()
Price_IQ=StringVar()
Date=StringVar()
Jub_NUM=StringVar()

#function for database


def getdata(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data['values']
    
    Costomer_Name.set(row[1])
    Phon_Number.set(row[2])
    Model.set(row[3])
    IMEI.set(row[4])
    SN.set(row[5])
    Warrenty_state.set(row[6])
    Fulty.set(row[7])
    Your_Servece.set(row[8])
    Item_Code.set(row[9])
    Descraption.set(row[10])
    Price_Dolar.set(row[11])
    Price_IQ.set(row[12])
    Date.set(row[13])
    Jub_NUM.set(row[14])


def displayall():
    tv.delete(* tv.get_children())
    for row in Data.fetch():
        tv.insert("","end",values=row)
    return 


def delete():
    Data.remove(row[0])
    clearr()
    displayall()
  
def clearr():
    Costomer_Name.set("")
    Phon_Number.set("")
    Model.set("") 
    IMEI.set("") 
    SN.set("")
    Warrenty_state.set("") 
    Fulty.set("") 
    Your_Servece .set("")
    Item_Code.set("") 
    Descraption .set("")
    Price_Dolar .set("")
    Price_IQ .set("")
    Date .set("")
    Jub_NUM.set("")

def new_func():
    entryname.setvar('')

def add_job():
    if entryname.get()=="" or Enphon.get()=="" or Enimei.get()=="" or Ensn.get()=="" or enserverce.get()=="" or enwarranty.get()==""  or Enprice.get()=="" or enuniq_number.get()=="" :
        messagebox.showwarning("Error"," Please enter important information")
    elif Enitem.get()=="":
        messagebox.showerror("Error","please input the item code !")
    
        return
    Data.insert(
        
        entryname.get(),
        Enphon.get(),
        defmodel.get(),
        Enimei.get(),
        Ensn.get(),
        enwarranty.get(),
        
        enfulty.get(),
        enserverce.get(),
        
        Enitem.get(),
        enPart.get(),
        Enprice.get(),
        result_entry.get(),
        endate.get(),
        enuniq_number.get(),
    )
    messagebox.showinfo("Seccess %" )
    displayall()
    clearr()
   

def search_data():
    
    tv.delete(*tv.get_children())
    
  
    Jub_NUM= Search.get()
    search_results = Data.search(Jub_NUM)
    for row in search_results:
        tv.insert("", "end", values=row)

# id 
id=Label(entres_fram,text='ID',font=('Times New Roman (Headings CS)',8),bg='#d7d8b5')
id.place(x=70,y=30)
enid=Entry(entres_fram,width=10,font=('Aptos',8))
enid.place(x=85,y=30)


#customer name
costomer_name=Label(entres_fram,text='Customr_Name',font=('Times New Roman (Headings CS)',8),bg='#d7d8b5')
costomer_name.place(x=10,y=50)
entryname=Entry(entres_fram,textvariable=Costomer_Name,width=20,font=('Aptos',8))
entryname.place(x=85,y=50)

#phon number for customer 
phon=Label(entres_fram,text='Phon_Number',font=('Times New Roman (Headings CS)',8),bg='#d7d8b5')
phon.place(x=200,y=50)
Enphon=Entry(entres_fram,textvariable=Phon_Number,width=20,font=('Aptos',8))
Enphon.place(x=270,y=50)

#mobali model
model=Label(entres_fram,text='Model',font=('Times New Roman (Headings CS)',8),bg='#d7d8b5')
model.place(x=375,y=50)
defmodel=ttk.Combobox(entres_fram,textvariable=Model,font=('Times New Roman (Headings CS)',8),width=10,state='readonly')
defmodel['values']=('HUAWEI','REALME','OSCAL','HONOR','NOKIA')
defmodel.place(x=410,y=50)

#imei 

imei=Label(entres_fram,text='IMEI',font=('Times New Roman (Headings CS)',8),bg='#d7d8b5')
imei.place(x=495,y=50)
Enimei=Entry(entres_fram,width=17,textvariable=IMEI,font=('Aptos',8))
Enimei.place(x=520,y=50)

# sirail number 
sn=Label(entres_fram,text='SN',font=('Times New Roman (Headings CS)',8),bg='#d7d8b5')
sn.place(x=620,y=50)
Ensn=Entry(entres_fram,width=17,textvariable=SN,font=('Aptos',8))
Ensn.place(x=640,y=50)

#warranty state
warranty=Label(entres_fram,text='WARRANTY',font=('Times New Roman (Headings CS)',8),bg='#d7d8b5')
warranty.place(x=745,y=50)
enwarranty=ttk.Combobox(entres_fram,textvariable=Warrenty_state,font=('Times New Roman (Headings CS)',8),width=13,state='readonly')
enwarranty['values']=('IN WARRANTY','OUT WARRANTY')
enwarranty.place(x=810,y=50)


#type of fulty
fulty=Label(entres_fram,text='FULTY',font=('Times New Roman (Headings CS)',8),bg='#d7d8b5')
fulty.place(x=913,y=50)
enfulty=ttk.Combobox(entres_fram,textvariable=Fulty,font=('Times New Roman (Headings CS)',8),width=15,state='readonly')
enfulty['values']=('FRP','HUWAEI ID','SCREEN BROKEN','BLACK SCREEN','LINSE ON SCREEN','TOUCH NOT WORKS','CON NOT CHARGE','SLOW CHARGE','GOST CHARGE','MIC NOT WORK','NOIISE SOUND ON MIC','NO SIRVCE','LOW SIRVECE','CALL DROUPED','NOISE ON CALL','SIM NOT WORK','NO POWER','POWER ON LOGO','HEAT UP')
enfulty.place(x=950,y=50)

#SERVEC 

servece=Label(entres_fram,text='Your_Servce',font=('Times New Roman (Headings CS)',8),bg='#d7d8b5')
servece.place(y=80,x=10)
enserverce=ttk.Combobox(entres_fram,textvariable=Your_Servece,font=('Times New Roman (Headings CS)',8),width=13,state='readonly')
enserverce['values']=('software','part replacement')
enserverce.place(y=80,x=80)

#item code

item_code=Label(entres_fram,text='Item_Code',font=('Times New Roman (Headings CS)',8),bg='#d7d8b5')
item_code.place(y=80,x=185)
Enitem=Entry(entres_fram,width=17,textvariable=Item_Code,font=('Aptos',8))
Enitem.place(y=80,x=240)

#part descraption

Part=Label(entres_fram,text='Descrption',font=('Times New Roman (Headings CS)',8),bg='#d7d8b5')
Part.place(y=80,x=340)
enPart=ttk.Combobox(entres_fram,textvariable=Descraption,font=('Times New Roman (Headings CS)',8),width=13,state='readonly')
enPart['values']=('Screen','MainBoard','SubBoard','speker','Fpc Main','Fpc saidkay','Main Camera','frot Camera','Small Camera','Battery','Back Cover')
enPart.place(y=80,x=400)

#price




def calculate_product():
    try:
        # Get the value from the entry
        value = float(Enprice.get())
        # Calculate the product
        result = value * 1500
        # Display the result in the non-editable entry
        result_entry.config(state='normal')  # Allow editing
         # Clear any previous value
        result_entry.insert(0, str(result))  # Insert the calculated result
        result_entry.config(state='readonly')  # Make it read-only again
    except ValueError:
        # Handle the case where the input is not a number
        
        result_entry.insert(0, "Error")

button = ttk.Button(entres_fram, text="Price IQ", command=calculate_product)
button.place(y=80,x=660)


result_entry = Entry(entres_fram, textvariable=Price_IQ,width=15, font=('Arial', 10), state='readonly')
result_entry.place(y=80,x=740)


price=Label(entres_fram,text='Price',font=('Times New Roman (Headings CS)',8),bg='#d7d8b5')
price.place(y=80,x=505)
Enprice=Entry(entres_fram,textvariable=Price_Dolar,width=17,font=('Aptos',8))
Enprice.place(y=80,x=540)


#date lable
date_lbl=Label(entres_fram,text='Date',font=('Times New Roman (Headings CS)',8),bg='#d7d8b5')
date_lbl.place(y=80,x=850)
endate=Entry(entres_fram,textvariable=Date,width=17,font=('Aptos',8))
endate.place(y=80,x=877)

#import date and time

def update_datetime():
    new=datetime.now()
    date_time_string = new.strftime("%Y-%m-%d %H:%M:%S")
    date_time_label.config(text=date_time_string)
    root.after(1000, update_datetime)

date_time_label = ttk.Label(entres_fram, font=('Arial', 12),background='#d7d8b5',foreground='#364768')
date_time_label.place(x=1,y=1)

update_datetime()


#generat job number
def generate_unique_number():
    now = datetime.now()
    date_prefix = now.strftime("CR-"+"001-"+"%y%m%d") 
    unique_number = date_prefix + str(uuid.uuid4().int)[:6] 
    enuniq_number.insert(0, str(unique_number))
    enuniq_number.bind("<FocusOut>", enable_button)
    generate_button.config(50,state=DISABLED)
    enuniq_number.config(state='readonly')

def enable_button(event):
    generate_button.config(state=NORMAL)
    
unique_number_label =Label(entres_fram,text="JOB_NUM", font=('Arial', 10),background="#d7d8b5",foreground='#364768')
unique_number_label.place(y=110,x=10)
enuniq_number=ttk.Entry(entres_fram,textvariable=Jub_NUM, width=20, font=('Arial', 10))
enuniq_number.place(y=110,x=75)

#button for job number

generate_button =Button(entres_fram, text="Job_Number", command=generate_unique_number,width=12,bg="#5dbb86")
generate_button.place(y=135,x=7)

#Remark 
Remark_r=Label(entres_fram,width=50,bg="white",bd=1,relief='solid',height=5).place(y=120,x=280)

#set defult text 
def remark_text():
    remarkk_text="Remark"
    
    Remark.insert(0,remarkk_text)

Remark=Entry(entres_fram,fg="black",width=50,borderwidth=2,)
Remark.place(y=130,x=285)
remark_text()


#set search
def search_text():
    Searchh_text="Search"
    
    Search.insert(0,Searchh_text)
    
Search=Entry(entres_fram,fg="black",width=50,borderwidth=2)
Search.place(y=160,x=285)

search_button=Button(entres_fram,text="Search",width=5,height=1,command=search_data)
search_button.place(y=160,x=235)
search_text()

#fram for buttons 
button_lbl=Label(entres_fram,width=50,bg="white",bd=1,relief=SOLID,height=5).place(y=120,x=600)

#state button




state_button =Button(button_lbl, text="Complet",command=add_job,width=8,bg="#578c3b")
state_button.place(y=130,x=610)

#Reset botton



    
delet_button =Button(button_lbl, text="Reset",width=8,bg="#bf5b5a",command=clearr)
delet_button.place(y=130,x=680)

#update button





update_button =Button(button_lbl, text="Delete ",width=8,bg="#16a085",command=delete)
update_button.place(y=130,x=750)



#export button



export_button =ttk.Button(button_lbl, text="Export",width=10,style="Green.TButton")
export_button.place(y=130,x=820)


#table
table=Frame(root,bg='white')
table.place(x=2,y=210,width=1210,height=580)

style=ttk.Style()
style.configure("mystyle.Treeview",font=('calibri',8),rowheight=60)
style.configure("mystyle.Treeview.Heading",font=('calibri',8))
tv=ttk.Treeview(table,columns=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14),style="mystyle.Treeview")
tv.heading('0',text="ID")
tv.column('0',width='16')

tv.heading("1",text="Customer_Name")
tv.column("1",width="90",anchor='center')


tv.heading("2",text="Phon_Number")
tv.column("2",width="100",anchor='center')

tv.heading("3",text="Model")
tv.column("3",width="80",anchor='center')

tv.heading("4",text="IMEI")
tv.column("4",width="80",anchor='center')

tv.heading("5",text="SN")
tv.column("5",width="80",anchor='center')

tv.heading("6",text="Warranty_state")
tv.column("6",width="80",anchor='center')

tv.heading("7",text="Fulty")
tv.column("7",width="80",anchor='center')

tv.heading("8",text="Your_Servece")
tv.column("8",width="80",anchor='center')

tv.heading("9",text="Item_code")
tv.column("9",width="80",anchor='center')

tv.heading("10",text="Descraption")
tv.column("10",width="80",anchor='center')

tv.heading("11",text="Price_Dolar")
tv.column("11",width="80",anchor='center')

tv.heading("12",text="Price_IQ")
tv.column("12",width="89",anchor='center')

tv.heading("13",text="Date")
tv.column("13",width="100",anchor='center')

tv.heading("14",text="Job_NUM")
tv.column("14",width="100",anchor='center')
tv.bind("<ButtonRelease-1>",getdata)


tv.place(x=-200,y=1)

#logo fram

logo=PhotoImage(file='moo.png')

new_width=200
new_hight=230

logo=logo.subsample(int(logo.width() / new_width), int(logo.height()/ new_hight))
lbl_logo=Label(root,image=logo,bg="#364768").place(x=1230,y=210)


#cuculater 
def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)
    
def button_clear():
    global expression
    expression = ""
    input_text.set("")

def button_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""
    
expression = ""
input_text = StringVar()


#set buttons for caculater 
cacu_fram=Frame(root,width=180,height=280,bg="#364768")
cacu_fram.place(x=1225,y=510)



cacu_entry=Entry(cacu_fram,width=15,background="gray",state='readonly',bg='white',highlightbackground="black",bd=6,font=(6),textvariable=input_text).place(x=1,y=3)



clear=Button(cacu_fram,text="C",width=8,height=2,bd=1,bg='gray',fg="black",font=('Algerian',6),command=lambda:button_clear(),cursor='hand2')
clear.place(x=125,y=50)

div=Button(cacu_fram,text="/",width=8,height=2,bd=1,bg='gray',fg="black",font=('Algerian',6),command=lambda:button_click('/'),cursor='hand2')
div.place(x=125,y=80)

mal=Button(cacu_fram,text="*",width=8,height=2,bd=1,bg='gray',fg="black",font=('Algerian',6),command=lambda:button_click('*'),cursor='hand2')
mal.place(x=125,y=110)


add=Button(cacu_fram,text="+",width=8,height=2,bd=1,bg='gray',fg="black",font=('Algerian',6),command=lambda:button_click('+'),cursor='hand2')
add.place(x=125,y=140)

minus=Button(cacu_fram,text="-",width=8,height=2,bd=1,bg='gray',fg="black",font=('Algerian',6),command=lambda:button_click('-'),cursor='hand2')
minus.place(x=125,y=170)

one=Button(cacu_fram,text="1",width=5,height=2,bd=1,bg='gray',fg="black",font=('Algerian',7),command=lambda:button_click('1'),cursor='hand2')
one.place(x=2,y=50)

tow=Button(cacu_fram,text="2",width=5,height=2,bd=1,bg='gray',fg="black",font=('Algerian',7),command=lambda:button_click('2'),cursor='hand2')
tow.place(x=42,y=50)


three=Button(cacu_fram,text="3",width=5,height=2,bd=1,bg='gray',fg="black",font=('Algerian',7),command=lambda:button_click('3'),cursor='hand2')
three.place(x=83,y=50)

four=Button(cacu_fram,text="4",width=5,height=2,bd=1,bg='gray',fg="black",font=('Algerian',7),command=lambda:button_click('4'),cursor='hand2')
four.place(x=2,y=80)

five=Button(cacu_fram,text="5",width=5,height=2,bd=1,bg='gray',fg="black",font=('Algerian',7),command=lambda:button_click('5'),cursor='hand2')
five.place(x=42,y=80)

six=Button(cacu_fram,text="6",width=5,height=2,bd=1,bg='gray',fg="black",font=('Algerian',7),command=lambda:button_click('6'),cursor='hand2')
six.place(x=83,y=80)

saven=Button(cacu_fram,text="7",width=5,height=2,bd=1,bg='gray',fg="black",font=('Algerian',7),command=lambda:button_click('7'),cursor='hand2')
saven.place(x=2,y=110)

eight=Button(cacu_fram,text="8",width=5,height=2,bd=1,bg='gray',fg="black",font=('Algerian',7),command=lambda:button_click('8'),cursor='hand2')
eight.place(x=42,y=110)

nain=Button(cacu_fram,text="9",width=5,height=2,bd=1,bg='gray',fg="black",font=('Algerian',7),command=lambda:button_click('9'),cursor='hand2')
nain.place(x=83,y=110)

zero=Button(cacu_fram,text="0",width=5,height=2,bd=1,bg='gray',fg="black",font=('Algerian',7),command=lambda:button_click('0'),cursor='hand2')
zero.place(x=42,y=140)

dot=Button(cacu_fram,text=".",width=5,height=2,bd=1,bg='gray',fg="black",font=('Algerian',7),command=lambda:button_click('.'),cursor='hand2')
dot.place(x=83,y=140)

equl=Button(cacu_fram,text="=",width=10,height=0,bd=1,bg='gray',fg="black",font=('Algerian',9),command=lambda:button_equal(),cursor='hand2')
equl.place(x=42,y=170)



displayall()

root.mainloop()