import tempfile
from tkinter import *
from tkinter import messagebox
import random,os,smtplib

def clear():
    bath_Etry.delete(0,END)
    FC_Etry.delete(0,END)
    FW_Etry.delete(0,END)
    HS_Etry.delete(0,END)
    HG_Etry.delete(0,END)
    BL_Etry.delete(0,END)

    rice_Etry.delete(0,END)
    oil_Etry.delete(0,END)
    daal_Etry.delete(0,END)
    wheat_Etry.delete(0,END)
    Sugar_Etry.delete(0,END)
    Tea_Etry.delete(0,END)

    coke_Etry.delete(0,END)
    mirinda_Etry.delete(0,END)
    sprite_Etry.delete(0,END)
    lemon_Etry.delete(0,END)
    bovanto_Etry.delete(0,END)
    fanta_Etry.delete(0,END)

    bath_Etry.insert(0,0)
    FC_Etry.insert(0,0)
    FW_Etry.insert(0,0)
    HS_Etry.insert(0,0)
    HG_Etry.insert(0,0)
    BL_Etry.insert(0,0)

    rice_Etry.insert(0,0)
    oil_Etry.insert(0,0)
    daal_Etry.insert(0,0)
    wheat_Etry.insert(0,0)
    Sugar_Etry.insert(0,0)
    Tea_Etry.insert(0,0)


    coke_Etry.insert(0,0)
    mirinda_Etry.insert(0,0)
    sprite_Etry.insert(0,0)
    lemon_Etry.insert(0,0)
    bovanto_Etry.insert(0,0)
    fanta_Etry.insert(0,0)

    cosmetic_Etry.delete(0, END)
    grocery_Etry.delete(0, END)
    drinks_Etry.delete(0, END)

    cosme_tax_Etry.delete(0, END)
    grocery_tax_Etry.delete(0, END)
    drinks_tax_Etry.delete(0, END)

    name_Etry.delete(0, END)
    ph_Etry.delete(0, END)
    BN_Etry.delete(0,END)

    bill_txt.delete(1.0, END)



# def send_gmail():
#     def send_Email():
#         ob=smtplib.SMTP('smtp.gmail.com',587)
#         ob.starttls()
#         ob.login(mailId_Etry.get(),password_Etry.get())
#         message=messagetext.get(1.0,END)
#         ob.sendmail(cstmr_mail_Etry.get(),messagetext.get(),message)
#         ob.quit()
#         messagebox.showinfo('Success','Mail sented successfully')
#
#
#     if bill_txt.get(1.0, END) == '\n':
#         messagebox.showerror('Error', 'Bill is Empty')
#     else:
#         root1=Toplevel()
#         root1.title('Email Sender')
#         root1.config(bg='gray20')
#         root1.resizable(0,0)
#
#         sender_frame=LabelFrame(root1,text='Sender',font=('arial',16,'bold')
#                                 ,bg='gray20',fg='white')
#         sender_frame.grid(row=0,column=0,padx=40,pady=20)
#
#         mailId_lbl=Label(sender_frame,text="Sender's Mail",font=('arial',10,'bold')
#                          ,bg='gray20',fg='white')
#         mailId_lbl.grid(row=0,column=0,padx=20,pady=20)
#         mailId_Etry=Entry(sender_frame,font=('calibri',16,'bold'),bg='white',
#                           fg='gray20',bd=8,relief=GROOVE)
#         mailId_Etry.grid(row=0,column=1,padx=5)
#
#         password_lbl = Label(sender_frame, text='Password', font=('arial', 10, 'bold')
#                            , bg='gray20', fg='white')
#         password_lbl.grid(row=1, column=0, padx=20, pady=20)
#         password_Etry = Entry(sender_frame, font=('calibri', 16, 'bold'), bg='white',
#                             fg='gray20', bd=8, relief=GROOVE,show='*')
#         password_Etry.grid(row=1, column=1, padx=5)
#
#         recipient_lf=LabelFrame(root1,text='RECIPIENT',font=('arial',14,'bold')
#                                 ,bg='gray20',fg='white')
#         recipient_lf.grid(row=1,column=0,padx=40,pady=1)
#
#         cstmr_mail_lbl=Label(recipient_lf,text='Mail_Id',font=('arial', 10, 'bold')
#                            , bg='gray20', fg='white')
#         cstmr_mail_lbl.grid(row=0,column=0,padx=20,pady=20)
#         cstmr_mail_Etry=Entry(recipient_lf,font=('arial', 10, 'bold'),bd=8,
#                               relief=GROOVE)
#         cstmr_mail_Etry.grid(row=0,column=1,padx=1,pady=10)
#
#
#         message_lbl = Label(recipient_lf, text='Message', font=('arial', 10, 'bold')
#                                , bg='gray20', fg='white')
#         message_lbl.grid(row=1, column=0, padx=20, pady=10)
#
#         messagetext=Text(recipient_lf, font=('arial', 10, 'bold'),bd=2,
#                         relief=SUNKEN,width=53,height=10 )
#         messagetext.grid(row=2,column=0,columnspan=2)
#         messagetext.delete(1.0,END)
#         messagetext.insert(END,bill_txt.get(1.0,END).replace('*','').replace('-',''))
#
#         sendbtn=Button(root1,text='SEND',font=('arial', 14, 'bold'),bd=8,
#                        relief=GROOVE,width=20,command=send_Email)
#         sendbtn.grid(row=2,column=0,pady=10)
#
#
#         root1.mainloop()


def print_bill():
    if bill_txt.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(bill_txt.get(1.0,END))
        os.startfile(file,'print')


def search_bill():
    for i in os.listdir('Bills/'):
        if i.split('.')[0] == BN_Etry.get():
            f=open(f'Bills/{i}','r')
            bill_txt.delete('1.0',END)
            for data in f:
                bill_txt.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Billnumber')





if not os.path.exists('Bills/'):
    os.mkdir('Bills/')
def save_bill():
    global Billnumber
    result=messagebox.askyesno('confirm','Do you want save this bill')
    if result:
        bill_content=bill_txt.get(1.0,END)
        file=open(f'bills/{Billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'billnumber{Billnumber}is save successfully')
        Billnumber = random.randint(1000, 2000)

Billnumber=random.randint(1000,2000)

def bill_btn():

    bill_txt.delete(1.0,END)

    if name_Etry.get()=='' or ph_Etry.get()=='':
        messagebox.showerror('Error','Customer details are required')
    elif cosmetic_Etry.get()=='' and grocery_Etry.get()=='' and drinks_Etry.get()=='':
        messagebox.showerror('Error','No product are selected')
    elif cosmetic_Etry.get()=='0 Rs' and grocery_Etry.get()=='0 Rs' and drinks_Etry.get()=='0 Rs':
        messagebox.showerror('Error','No product are selected')
    else:
        bill_txt.insert(END,'\t\t\t**Welcome Customer** \n')
        bill_txt.insert(END,f'Bill No:{Billnumber}\n')
        bill_txt.insert(END,f'Customer Name:{name_Etry.get()}\n')
        bill_txt.insert(END,f'Phone Number:{ph_Etry.get()}\n')
        bill_txt.insert(END,'\n*********************************************************\n')
        bill_txt.insert(END,'Product\t\t\tQuantity\t\t\tPrice\n')
        bill_txt.insert(END,'*********************************************************\n')

        if bath_Etry.get()!='0':
            bill_txt.insert(END,f'Bath soap\t\t\t   {bath_Etry.get()}\t\t\t {sp_value}\n')
        if FC_Etry.get()!='0':
            bill_txt.insert(END,f'Face Cream\t\t\t   {FC_Etry.get()}\t\t\t {fc_value}\n')
        if FW_Etry.get()!='0':
            bill_txt.insert(END,f'Face Wash\t\t\t   {FW_Etry.get()}\t\t\t  {fw_value}\n')
        if HS_Etry.get()!='0':
            bill_txt.insert(END,f'Hair spray\t\t\t   {HS_Etry.get()}\t\t\t {hs_value}\n')
        if HG_Etry.get()!='0':
            bill_txt.insert(END,f'Hair Gel\t\t\t   {HG_Etry.get()}\t\t\t {hg_value}\n')
        if BL_Etry.get()!='0':
            bill_txt.insert(END,f'Body Lotion\t\t\t   {BL_Etry.get()}\t\t\t {bl_value}\n')

        if rice_Etry.get()!='0':
            bill_txt.insert(END,f'Rice \t\t\t   {rice_Etry.get()}\t\t\t {rice_Rs}\n')
        if oil_Etry.get()!='0':
            bill_txt.insert(END,f'Oil \t\t\t   {oil_Etry.get()}\t\t\t {oil_Rs}\n')
        if daal_Etry.get()!='0':
            bill_txt.insert(END,f'Daal \t\t\t   {daal_Etry.get()}\t\t\t {daal_Rs}\n')
        if wheat_Etry.get()!='0':
            bill_txt.insert(END,f'Wheat \t\t\t   {wheat_Etry.get()}\t\t\t {wheat_Rs}\n')
        if Sugar_Etry.get()!='0':
            bill_txt.insert(END,f'Sugar \t\t\t   {Sugar_Etry.get()}\t\t\t {sugar_Rs}\n')
        if Tea_Etry.get()!='0':
            bill_txt.insert(END,f'Tea \t\t\t   {Tea_Etry.get()}\t\t\t {Tea_Rs}\n')

        if coke_Etry.get()!='0':
            bill_txt.insert(END,f'Coke \t\t\t   {coke_Etry.get()}\t\t\t {coke_Rs}\n')
        if mirinda_Etry.get()!='0':
            bill_txt.insert(END,f'Mirinda \t\t\t   {mirinda_Etry.get()}\t\t\t {mirinda_Rs}\n')
        if sprite_Etry.get()!='0':
            bill_txt.insert(END,f'Sprite \t\t\t   {sprite_Etry.get()}\t\t\t {sprite_Rs}\n')
        if lemon_Etry.get()!='0':
            bill_txt.insert(END,f'Lemon \t\t\t   {lemon_Etry.get()}\t\t\t {lemon_Rs}\n')
        if bovanto_Etry.get()!='0':
            bill_txt.insert(END,f'Bovanto \t\t\t   {bovanto_Etry.get()}\t\t\t {bovonto_Rs}\n')
        if fanta_Etry.get()!='0':
            bill_txt.insert(END,f'Fanta \t\t\t   {fanta_Etry.get()}\t\t\t {fanta_Rs}\n')

        bill_txt.insert(END,'\n---------------------------------------------------------\n')

        if cosme_tax_Etry.get()!='0.0 Rs':
            bill_txt.insert(END,f'Cosmetic Tax\t\t{cosme_tax_Etry.get()}\n')
        if grocery_tax_Etry.get()!='0.0 Rs':
            bill_txt.insert(END,f'Grocery Tax\t\t{grocery_tax_Etry.get()}\n')
        if drinks_tax_Etry.get()!='0.0 Rs':
            bill_txt.insert(END,f'Drinks Tax\t\t{drinks_tax_Etry.get()}\n')
        bill_txt.insert(END,'\n--------------------------------------------------------\n')

        bill_txt.insert(END,f'Total Bill\t\t{totalbill}')

        save_bill()

def total():
    # cosmetic_Price
    global sp_value,fc_value,fw_value,hs_value,hg_value,bl_value
    global rice_Rs,oil_Rs,daal_Rs,wheat_Rs,sugar_Rs,Tea_Rs
    global coke_Rs,mirinda_Rs,sprite_Rs,lemon_Rs,bovonto_Rs,fanta_Rs
    global totalbill
    sp_value=int(bath_Etry.get())*30
    fc_value=int(FC_Etry.get())*50
    fw_value=int(FW_Etry.get())*70
    hs_value=int(HS_Etry.get())*80
    hg_value=int(HG_Etry.get())*100
    bl_value=int(BL_Etry.get())*60

    total_cos_price = sp_value+fc_value+fw_value+hs_value+hg_value+bl_value
    cosmetic_Etry.delete(0,END)
    cosmetic_Etry.insert(0,f'{total_cos_price} Rs')
    cosmetictax=total_cos_price*0.12
    cosme_tax_Etry.delete(0,END)
    cosme_tax_Etry.insert(0,f'{cosmetictax} Rs')

    # Grocery_Price
    rice_Rs=int(rice_Etry.get())*55
    oil_Rs=int(oil_Etry.get())*110
    daal_Rs=int(daal_Etry.get())*35
    wheat_Rs=int(wheat_Etry.get())*75
    sugar_Rs=int(Sugar_Etry.get())*24
    Tea_Rs=int(Tea_Etry.get())*35

    grocery_total = rice_Rs+oil_Rs+daal_Rs+wheat_Rs+sugar_Rs+Tea_Rs
    grocery_Etry.delete(0,END)
    grocery_Etry.insert(0,f'{grocery_total} Rs')
    grocerytax=grocery_total*0.10
    grocery_tax_Etry.delete(0,END)
    grocery_tax_Etry.insert(0,f'{grocerytax} Rs')

    # Drinks_Price
    coke_Rs=int(coke_Etry.get())*10
    mirinda_Rs=int(mirinda_Etry.get())*15
    sprite_Rs=int(sprite_Etry.get())*12
    lemon_Rs=int(lemon_Etry.get())*20
    bovonto_Rs=int(bovanto_Etry.get())*25
    fanta_Rs=int(fanta_Etry.get())*30

    drinkstotalprice=coke_Rs+mirinda_Rs+sprite_Rs+lemon_Rs+bovonto_Rs+fanta_Rs
    drinks_Etry.delete(0,END)
    drinks_Etry.insert(0,f'{drinkstotalprice} Rs')
    drinkstax=drinkstotalprice*0.5
    drinks_tax_Etry.delete(0,END)
    drinks_tax_Etry.insert(0,f'{drinkstax} Rs')

    totalbill=total_cos_price+grocery_total+drinkstotalprice+cosmetictax+grocerytax+drinkstax




root=Tk()
root.title('Billing project')
root.geometry('1980x1080')
headingLabel=Label(root,text='Retail Billing System',font=('times new roman',
                    20,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
headingLabel.pack(fill=X)

ctmr_Lbl_Frm=LabelFrame(root,text='Customer Details',font=('times new roman',
                    17,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
ctmr_Lbl_Frm.pack(fill=X,pady=10)

name_lbl=Label(ctmr_Lbl_Frm,text='Name',font=('times new roman',
                    15,'bold'),fg='white',bg='gray20')
name_lbl.grid(row=0,column=0)
name_Etry=Entry(ctmr_Lbl_Frm,font=('arial',8,'bold'),relief=GROOVE,bd=5,width=30)
name_Etry.grid(row=0,column=1,padx=5,pady=3)

ph_lbl=Label(ctmr_Lbl_Frm,text='Phone number',font=('times new roman',
                    15,'bold'),fg='white',bg='gray20')
ph_lbl.grid(row=0,column=2,padx=20)
ph_Etry=Entry(ctmr_Lbl_Frm,font=('arial',8,'bold'),bd=8,relief=GROOVE,width=30)
ph_Etry.grid(row=0,column=3,padx=5,pady=3)

BN_lbl=Label(ctmr_Lbl_Frm,text='Bill number',font=('times new roman',
                    15,'bold'),fg='white',bg='gray20')
BN_lbl.grid(row=0,column=4,padx=20)
BN_Etry=Entry(ctmr_Lbl_Frm,font=('arial',8,'bold'),bd=8,relief=GROOVE,width=30)
BN_Etry.grid(row=0,column=5,padx=5,pady=3)

src_btn=Button(ctmr_Lbl_Frm,text='SEARCH',width=20,font=('times new roman',10,'bold')
               ,relief=GROOVE,bd=8,command=search_bill)
src_btn.grid(row=0,column=6,padx=30)

pdct_frm=Frame(root)
pdct_frm.pack(pady=1)

cosmtc_lbl_frm=LabelFrame(pdct_frm,text='Cosmetics',font=('times new roman',
                    17,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
cosmtc_lbl_frm.grid(row=0,column=0)

bath_lbl=Label(cosmtc_lbl_frm,text='Bath Soap',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
bath_lbl.grid(row=0,column=0,sticky='w')
bath_Etry=Entry(cosmtc_lbl_frm,font=('arial',8,'bold'),bd=8,relief=GROOVE,width=20)
bath_Etry.grid(row=0,column=1,padx=5)
bath_Etry.insert(0,0)

FC_lbl=Label(cosmtc_lbl_frm,text='Face Cream',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
FC_lbl.grid(row=1,column=0,sticky='w',pady=5)
FC_Etry=Entry(cosmtc_lbl_frm,font=('arial',8,'bold'),bd=8,relief=GROOVE,width=20)
FC_Etry.grid(row=1,column=1,padx=5,pady=5)
FC_Etry.insert(0,0)

FW_lbl=Label(cosmtc_lbl_frm,text='Face Wash',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
FW_lbl.grid(row=2,column=0,pady=5,sticky='w')
FW_Etry=Entry(cosmtc_lbl_frm,font=('arial',8,'bold'),bd=8,relief=GROOVE,width=20)
FW_Etry.grid(row=2,column=1,padx=5,pady=5)
FW_Etry.insert(0,0)

HS_lbl=Label(cosmtc_lbl_frm,text='Hair Spray',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
HS_lbl.grid(row=3,column=0,pady=5,sticky='w')
HS_Etry=Entry(cosmtc_lbl_frm,font=('arial',8,'bold'),bd=8,relief=GROOVE,width=20)
HS_Etry.grid(row=3,column=1,padx=5,pady=5)
HS_Etry.insert(0,0)

HG_lbl=Label(cosmtc_lbl_frm,text='Hair Gel',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
HG_lbl.grid(row=4,column=0,pady=5,sticky='w')
HG_Etry=Entry(cosmtc_lbl_frm,font=('arial',8,'bold'),bd=8,relief=GROOVE,width=20)
HG_Etry.grid(row=4,column=1,padx=5,pady=5)
HG_Etry.insert(0,0)

BL_lbl=Label(cosmtc_lbl_frm,text='Body Lotion',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
BL_lbl.grid(row=5,column=0,sticky='w',pady=5)
BL_Etry=Entry(cosmtc_lbl_frm,font=('arial',8,'bold'),bd=8,relief=GROOVE,width=20)
BL_Etry.grid(row=5,column=1,padx=5,pady=5)
BL_Etry.insert(0,0)

grocery_lbl_frm=LabelFrame(pdct_frm,text='Grocery',font=('times new roman',
                    17,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
grocery_lbl_frm.grid(row=0,column=1,padx=5)

rice_lbl=Label(grocery_lbl_frm,text='Rice',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
rice_lbl.grid(row=0,column=0,sticky='w',pady=4)
rice_Etry=Entry(grocery_lbl_frm,font=('arial',8,'bold'),bd=8,relief=GROOVE,width=20)
rice_Etry.grid(row=0,column=1,padx=5,pady=4)
rice_Etry.insert(0,0)

oil_lbl=Label(grocery_lbl_frm,text='Oil',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
oil_lbl.grid(row=1,column=0,sticky='w',pady=4)
oil_Etry=Entry(grocery_lbl_frm,font=('arial',8,'bold'),bd=8,relief=GROOVE,width=20)
oil_Etry.grid(row=1,column=1,padx=5,pady=4)
oil_Etry.insert(0,0)

daal_lbl=Label(grocery_lbl_frm,text='Daal',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
daal_lbl.grid(row=2,column=0,sticky='w',pady=4)
daal_Etry=Entry(grocery_lbl_frm,font=('arial',8,'bold'),bd=8,relief=GROOVE,width=20)
daal_Etry.grid(row=2,column=1,padx=5,pady=4)
daal_Etry.insert(0,0)

wheat_lbl=Label(grocery_lbl_frm,text='Wheat',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
wheat_lbl.grid(row=3,column=0,sticky='w',pady=4)
wheat_Etry=Entry(grocery_lbl_frm,font=('arial',8,'bold'),bd=8,relief=GROOVE,width=20)
wheat_Etry.grid(row=3,column=1,padx=5,pady=4)
wheat_Etry.insert(0,0)

Sugar_lbl=Label(grocery_lbl_frm,text='Sugar',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
Sugar_lbl.grid(row=4,column=0,sticky='w',pady=4)
Sugar_Etry=Entry(grocery_lbl_frm,font=('arial',8,'bold'),bd=8,relief=GROOVE,width=20)
Sugar_Etry.grid(row=4,column=1,padx=5,pady=4)
Sugar_Etry.insert(0,0)

Tea_lbl=Label(grocery_lbl_frm,text='Tea',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
Tea_lbl.grid(row=5,column=0,sticky='w',pady=4)
Tea_Etry=Entry(grocery_lbl_frm,font=('arial',8,'bold'),bd=8,relief=GROOVE,width=20)
Tea_Etry.grid(row=5,column=1,padx=5,pady=4)
Tea_Etry.insert(0,0)

drinks_lbl_frm=LabelFrame(pdct_frm,text='Cool Drinks',font=('times new roman',
                    17,'bold'),width=20,bg='gray20',fg='gold',bd=8,relief=GROOVE)
drinks_lbl_frm.grid(row=0,column=2)

coke_lbl=Label(drinks_lbl_frm,text='Coke',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
coke_lbl.grid(row=0,column=0,pady=4,sticky='w')
coke_Etry=Entry(drinks_lbl_frm,font=('arial',8),bd=8,relief=GROOVE,width=20)
coke_Etry.grid(row=0,column=1,padx=5,pady=4)
coke_Etry.insert(0,0)

mirinda_lbl=Label(drinks_lbl_frm,text='Mirinda',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
mirinda_lbl.grid(row=1,column=0,pady=4,sticky='w')
mirinda_Etry=Entry(drinks_lbl_frm,font=('arial',8,'bold'),bd=8,relief=GROOVE,width=20)
mirinda_Etry.grid(row=1,column=1,padx=5,pady=4)
mirinda_Etry.insert(0,0)

sprite_lbl=Label(drinks_lbl_frm,text='Sprite',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
sprite_lbl.grid(row=2,column=0,pady=4,sticky='w')
sprite_Etry=Entry(drinks_lbl_frm,font=('arial',8,'bold'),bd=8,relief=GROOVE,width=20)
sprite_Etry.grid(row=2,column=1,padx=5,pady=4)
sprite_Etry.insert(0,0)

lemon_lbl=Label(drinks_lbl_frm,text='Lemon',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
lemon_lbl.grid(row=3,column=0,pady=4,sticky='w')
lemon_Etry=Entry(drinks_lbl_frm,font=('arial',8,'bold'),bd=8,relief=GROOVE,width=20)
lemon_Etry.grid(row=3,column=1,padx=5,pady=4)
lemon_Etry.insert(0,0)

bovanto_lbl=Label(drinks_lbl_frm,text='Bovanto',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
bovanto_lbl.grid(row=4,column=0,pady=4,sticky='w')
bovanto_Etry=Entry(drinks_lbl_frm,font=('arial',8,'bold'),bd=8,relief=GROOVE,width=20)
bovanto_Etry.grid(row=4,column=1,padx=5,pady=4)
bovanto_Etry.insert(0,0)

fanta_lbl=Label(drinks_lbl_frm,text='Fanta',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
fanta_lbl.grid(row=5,column=0,pady=4,sticky='w')
fanta_Etry=Entry(drinks_lbl_frm,font=('arial',8,'bold'),bd=8,relief=GROOVE,width=20)
fanta_Etry.grid(row=5,column=1,padx=5,pady=4)
fanta_Etry.insert(0,0)

bill_area=Frame(pdct_frm,bd=8,relief=GROOVE)
bill_area.grid(row=0,column=3,padx=3)

lbl_area=Label(bill_area,text='Bill Area',font=(16),bd=8,relief=GROOVE)
lbl_area.pack(fill=X)

scroll_bar=Scrollbar(bill_area,orient=VERTICAL)
scroll_bar.pack(side=RIGHT,fill=Y)

bill_txt=Text(bill_area,width=60,height=14,yscrollcommand=scroll_bar.set)
bill_txt.pack()
scroll_bar.config(command=bill_txt.yview)

bill_menu=LabelFrame(root,text='Bill_Menu',font=('times new roman',
                    17,'bold'),width=20,bg='gray20',fg='gold',bd=8,relief=GROOVE)
bill_menu.pack(pady=5)

cosmetic_bill=Label(bill_menu,text='Cosmetic Menu',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
cosmetic_bill.grid(row=0,column=0,padx=20,pady=10)
cosmetic_Etry=Entry(bill_menu,bd=8,font=('arial',10,'bold'),relief=GROOVE)
cosmetic_Etry.grid(row=0,column=1,padx=4,pady=10)

grocery_bill=Label(bill_menu,text='Grocery Menu',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
grocery_bill.grid(row=1,column=0,pady=10)
grocery_Etry=Entry(bill_menu,bd=8,font=('arial',10,'bold'),relief=GROOVE)
grocery_Etry.grid(row=1,column=1,padx=4,pady=10)

drinks_bill=Label(bill_menu,text='Drinks Menu',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
drinks_bill.grid(row=2,column=0,pady=10)
drinks_Etry=Entry(bill_menu,bd=8,font=('arial',10,'bold'),relief=GROOVE)
drinks_Etry.grid(row=2,column=1,padx=4,pady=10)

cosmetic_tax=Label(bill_menu,text='Cosmetic tax',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
cosmetic_tax.grid(row=0,column=2,padx=20,pady=10)
cosme_tax_Etry=Entry(bill_menu,bd=8,font=('arial',10,'bold'),relief=GROOVE)
cosme_tax_Etry.grid(row=0,column=3,padx=4,pady=10)

grocery_tax=Label(bill_menu,text='Grocery tax',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
grocery_tax.grid(row=1,column=2,padx=20,pady=10)
grocery_tax_Etry=Entry(bill_menu,bd=8,font=('arial',10,'bold'),relief=GROOVE)
grocery_tax_Etry.grid(row=1,column=3,padx=4,pady=10)

drinks_tax=Label(bill_menu,text='Drinks Tax',font=('times new roman', 15,'bold')
               ,fg='white',bg='gray20')
drinks_tax.grid(row=2,column=2,padx=20,pady=10)
drinks_tax_Etry=Entry(bill_menu,bd=8,font=('arial',10,'bold'),relief=GROOVE)
drinks_tax_Etry.grid(row=2,column=3,padx=4,pady=10)

button_frame=Frame(bill_menu,bd=8,relief=GROOVE,height=40)
button_frame.grid(row=0,column=4,padx=70,rowspan=3)

btn_total=Button(button_frame,text='Total',command=total,font=('arial',10,'bold'),bg='gray20'
                ,width=10 ,fg='white',relief=GROOVE)
btn_total.grid(row=1,column=4,padx=10,pady=20)

btn_bill=Button(button_frame,text='Bill',font=('arial',10,'bold'),bg='gray20'
                ,width=10 ,fg='white',relief=GROOVE,command=bill_btn)
btn_bill.grid(row=1,column=5,padx=10,pady=20)

# btn_email=Button(button_frame,text='Email',font=('arial',10,'bold'),bg='gray20'
#                 ,width=10 ,fg='white',relief=GROOVE,command=send_gmail)
# btn_email.grid(row=1,column=6,padx=10,pady=10)

btn_print=Button(button_frame,text='print',font=('arial',10,'bold'),bg='gray20'
                ,width=10 ,fg='white',relief=GROOVE,command=print_bill)
btn_print.grid(row=1,column=7,padx=10,pady=20)

btn_clr=Button(button_frame,text='Clear',font=('arial',10,'bold'),bg='gray20'
                ,width=10 ,fg='white',relief=GROOVE,command=clear)
btn_clr.grid(row=1,column=8,padx=10,pady=20)

mainloop()
