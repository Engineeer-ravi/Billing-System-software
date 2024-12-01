from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib
#functionality part
def clear():
    bathsoapEntry.insert(0, 0)
    facecreamEntry.insert(0, 0)
    hairsparyEntry.insert(0, 0)
    bodylotionEntry.insert(0, 0)
    facewashEntry.insert(0, 0)
    hairgelEntry.insert(0, 0)

    daalEntry.insert(0, 0)
    riceEntry.insert(0, 0)
    oilEntry.insert(0, 0)
    wheatEntry.insert(0, 0)
    sugerEntry.insert(0, 0)
    teaEntry.insert(0, 0)

    cococolaEntry.insert(0, 0)
    dewEntry.insert(0, 0)
    spriteEntry.insert(0, 0)
    pepsiEntry.insert(0, 0)
    maazaEntry.insert(0, 0)
    frootiEntry.insert(0,0)

    cosmeticstaxEntry.delete(0,END)
    grocerytaxEntry.delete(0, END)
    drinkstaxEntry.delete(0, END)

    cosmeticspriceEntry.delete(0, END)
    grocerypriceEntry.delete(0, END)
    drinkspriceEntry.delete(0, END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0, END)
    billnumberEntry.delete(0, END)

    textarea.delete(1.0,END)
def send_email():
    def send_gmail():
       try:
          ob=smtplib.SMTP('smtp.gmail.com',587)
          ob.starttls()
          ob.login(senderEntry.get(),passwordEntry.get())
          message=email_textarea.get(1.0,END)
          ob.sendmail(senderEntry.get(),reciverEntry.get(),message)
          ob.quit()
          messagebox.showinfo('Success','Bill is successfully sent',parent=root1)
          root1.destroy()
       except:
          messagebox.showerror('Error','Something went wrong ,Please  try again')
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')

    else:
     root1=Toplevel()
     root1.grab_set()
     root1.title('send  gmail')
     root1.config(bg='gray25')
     root1.resizable(0,0)

     senderFrame=LabelFrame(root1,text='Sender',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
     senderFrame.grid(row=0,column=0,padx=40,pady=20)

     senderLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
     senderLabel.grid(row=0,column=0,padx=10,pady=8)

     senderEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
     senderEntry.grid(row=0, column=1, padx=10, pady=8)


     passwordLabel = Label(senderFrame, text="Password", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
     passwordLabel.grid(row=1, column=0, padx=10, pady=8)

     passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE,show='*')
     passwordEntry.grid(row=1, column=1, padx=10,pady = 8)


     recipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
     recipientFrame.grid(row=1, column=0, padx=40, pady=20)


     reciverLabel = Label(recipientFrame, text="Email Address", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
     reciverLabel.grid(row=0, column=0, padx=10, pady=8)

     reciverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
     reciverEntry.grid(row=0, column=1, padx=10, pady=8)


     messageLabel = Label(recipientFrame, text="Message", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
     messageLabel.grid(row=1, column=0, padx=10, pady=8)

     email_textarea=Text(recipientFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,
                         width=42,height=11)
     email_textarea.grid(row=2,column=0 ,columnspan=2)
     email_textarea.delete(1.0,END)
     email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))


     sendButton=Button(root1,text='SEND',font=('arial',16,'bold'),width=15,command=send_gmail)
     sendButton.grid(row=2,column=0,pady=20)

     root.mainloop()

def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumberEntry.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
                f.close()
                break
            else:
             messagebox.showerror('Error', 'Invalid Bill Number')
if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumber
    result =messagebox.askyesno('Confirm','Do you want to save the bill')
    if result:
       bill_content=textarea.get(1.0,END)
       file=open(f'bills/{billnumber}.txt','w')
       file.write(bill_content)
       file.close()
       messagebox.showinfo('Success',f'bill number {billnumber} is saved successfully')
       billnumber=random.randint(500,1000)
billnumber=random.randint(500,1000)

def bill_area():
    if nameEntry.get()==''or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details Are Required')
    elif cosmeticspriceEntry.get() == '' and grocerypriceEntry.get() == '' and drinkspriceEntry.get() == '':
        messagebox.showerror('Error', 'No Products  are selected')
    elif cosmeticspriceEntry.get() == '0 Rs' and grocerypriceEntry.get() == '0 Rs' and drinkspriceEntry.get() == '0 Rs':
        messagebox.showerror('Error', 'No Products  are selected')
        textarea.delete(1.0,END)
    else:
        textarea.insert(END, '\t\t*Welcome Customer*\n')
        textarea.insert(END, f'\nBill Number:{billnumber}\n')
        textarea.insert(END, f'\nCustomer Name:{nameEntry.get()}\n')
        textarea.insert(END, f'\nCustomer Phone Number:{phoneEntry.get()}\n')
        textarea.insert(END,'\n=======================================================')
        textarea.insert(END,'Product\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END, '\n=======================================================')
        if bathsoapEntry.get()!='0':
            textarea.insert(END,f'\nBath soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs')
        if facecreamEntry.get()!=  '0':
            textarea.insert(END, f'\nFace Cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs')
        if facewashEntry.get() != '0':
            textarea.insert(END, f'\nFace Wash\t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs')
        if hairsparyEntry.get()!= '0':
           textarea.insert(END, f'\nHair Spray\t\t\t{hairsparyEntry.get()}\t\t\t{hairsprayprice} Rs')
        if hairgelEntry.get() != '0':
           textarea.insert(END, f'\nHair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs')
        if bodylotionEntry.get() != '0':
          textarea.insert(END, f'\nBody Lotion\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Rs')


        if riceEntry.get() != '0':
           textarea.insert(END, f'\nRice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs')
        if oilEntry.get() != '0':
           textarea.insert(END,f'\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs')
        if daalEntry.get() !='0':
           textarea.insert(END,f'\nDaal\t\t\t{daalEntry.get()}\t\t\t{daalprice} Rs')
        if wheatEntry.get() != '0':
            textarea.insert(END, f'\nWheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rs')
        if sugerEntry.get() != '0':
           textarea.insert(END, f'\nSuger\t\t\t{sugerEntry.get()}\t\t\t{sugerprice} Rs')
        if teaEntry.get() != '0':
            textarea.insert(END, f'\nTea\t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs')
        if maazaEntry.get() != '0':
            textarea.insert(END, f'\nMaaza\t\t\t{maazaEntry.get()}\t\t\t{maazaprice} Rs')
        if pepsiEntry.get() != '0':
            textarea.insert(END, f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Rs')
        if spriteEntry.get() != '0':
            textarea.insert(END, f'\nSprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice} Rs')
        if dewEntry.get() != '0':
            textarea.insert(END, f'\nDew\t\t\t{dewEntry.get()}\t\t\t{dewprice} Rs')
        if frootiEntry.get() != '0':
            textarea.insert(END, f'\nFrooti\t\t\t{frootiEntry.get()}\t\t\t{frootiprice} Rs')
        if cococolaEntry.get() != '0':
            textarea.insert(END, f'\nCoco Cola\t\t\t{cococolaEntry.get()}\t\t\t{cococolaprice} Rs')
        textarea.insert(END, '\n-------------------------------------------------------')

        if cosmeticstaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nCosmetics Tax\t\t\t{cosmeticstaxEntry.get()}')

        if grocerytaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nGrocery Tax\t\t\t{grocerytaxEntry.get()}')

        if drinkstaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nCold Drink Tax\t\t\t{drinkstaxEntry.get()}')
        textarea.insert(END,f'\n\nTotal Bill\t\t\t {totalbill}')
        textarea.insert(END, '\n-------------------------------------------------------')
        save_bill()
def total():
    global soapprice,facecreamprice,facewashprice,hairsprayprice,hairgelprice,bodylotionprice
    global riceprice,daalprice,sugerprice,wheatprice,oilprice,teaprice
    global maazaprice,frootiprice,pepsiprice,cococolaprice,dewprice,spriteprice
    global totalbill
    soapprice=int(bathsoapEntry.get())*20
    facecreamprice = int(facecreamEntry.get()) * 100
    facewashprice = int(facewashEntry.get()) * 90
    hairsprayprice = int(hairsparyEntry.get()) * 110
    hairgelprice = int(hairgelEntry.get()) * 120
    bodylotionprice = int(bodylotionEntry.get()) * 150

    totalcosmeticsprice = soapprice + facecreamprice + facewashprice + hairgelprice + hairsprayprice + bodylotionprice
    cosmeticspriceEntry.delete(0, END)
    cosmeticspriceEntry.insert(0, f'{totalcosmeticsprice} Rs')
    cosmeticstax = totalcosmeticsprice * 0.12
    cosmeticstaxEntry.delete(0, END)
    cosmeticstaxEntry.insert(0, str(cosmeticstax) + 'Rs')
    # grocery price calculation
    riceprice = int(riceEntry.get()) * 80
    daalprice = int(daalEntry.get()) * 100
    oilprice = int(oilEntry.get()) * 120
    sugerprice = int(sugerEntry.get()) * 50
    teaprice = int(teaEntry.get()) * 45
    wheatprice = int(wheatEntry.get()) * 90
    totalgroceryprice = riceprice + daalprice + oilprice + sugerprice + teaprice + wheatprice
    grocerypriceEntry.delete(0, END)
    grocerypriceEntry.insert(0, f'{totalgroceryprice} Rs')
    grocerytax = totalgroceryprice * 0.05
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, str(grocerytax) + 'Rs')
    # cold drink price calculation
    maazaprice = int(maazaEntry.get()) * 65
    frootiprice = int(frootiEntry.get()) * 20
    dewprice = int(dewEntry.get()) * 60
    pepsiprice = int(pepsiEntry.get()) * 20
    spriteprice = int(spriteEntry.get()) * 95
    cococolaprice = int(cococolaEntry.get()) * 95
    totaldrinksprice = maazaprice + frootiprice + dewprice + pepsiprice + spriteprice + cococolaprice
    drinkspriceEntry.delete(0, END)
    drinkspriceEntry.insert(0, f'{totaldrinksprice} Rs')
    drinkstax = totaldrinksprice * 0.08
    drinkstaxEntry.delete(0, END)
    drinkstaxEntry.insert(0, str(drinkstax) + 'Rs')

    totalbill=totalcosmeticsprice+totalgroceryprice+totaldrinksprice+cosmeticstax+grocerytax+drinkstax

#GUI part
root=Tk()
root.title('BILLING SYSTEM')
root.geometry('1270x700+0+0')
root.iconbitmap('icon.ico')
headingLabel=Label(root,text='AI DERIVEN BILLING SYSTEM',font=('times new roman',30,'bold',)
                  ,bg='grey20',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold')
                                  ,fg='gold',bd=8,relief=GROOVE,bg='grey20')
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
nameLabel.grid(row=0,column=0,padx=8)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
phoneLabel.grid(row=0,column=2,padx=8,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
billnumberLabel.grid(row=0,column=4,padx=8,pady=2)

billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)


searchButton=Button(customer_details_frame,text='SEARCH',
                    font=('arial',12,'bold'),bd=7,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack()

cosmeticsFrame=LabelFrame(productsFrame,text='cosmetics',font=('times new roman',15,'bold')
                                  ,fg='gold',bd=8,relief=GROOVE,bg='grey20')
cosmeticsFrame.grid(row=0, column=0,)

bathsoapLabel=Label(cosmeticsFrame,text='Bath Soap',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10,sticky='w')
bathsoapEntry.insert(0,0)

facecreamLabel=Label(cosmeticsFrame,text='Face Cream',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')
facecreamEntry.insert(0,0)

facewashLabel=Label(cosmeticsFrame,text='Face Wash',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

facewashEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')
facewashEntry.insert(0,0)

hairsparyLabel=Label(cosmeticsFrame,text='Hair Spray',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
hairsparyLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

hairsparyEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairsparyEntry.grid(row=3,column=1,pady=9,padx=10,sticky='w')
hairsparyEntry.insert(0,0)

hairgelLabel=Label(cosmeticsFrame,text='Hair Gel',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

hairgelEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10,sticky='w')
hairgelEntry.insert(0,0)

bodylotionLabel=Label(cosmeticsFrame,text='Body Lotion',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10,sticky='w')
bodylotionEntry.insert(0,0)



groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold')
                                  ,fg='gold',bd=8,relief=GROOVE,bg='grey20')
groceryFrame.grid(row=0, column=1,)

riceLabel=Label(groceryFrame,text='Rice',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10,stick='w')

riceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,0)

oilLabel=Label(groceryFrame,text='Oil',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

oilEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10)
oilEntry.insert(0,0)

daalLabel=Label(groceryFrame,text='Daal',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
daalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

daalEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
daalEntry.grid(row=2,column=1,pady=9,padx=10)
daalEntry.insert(0,0)

wheatLabel=Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

wheatEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
wheatEntry.grid(row=3,column=1,pady=9,padx=10)
wheatEntry.insert(0,0)

sugerLabel=Label(groceryFrame,text='Suger',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
sugerLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

sugerEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sugerEntry.grid(row=4,column=1,pady=9,padx=10)
sugerEntry.insert(0,0)


teaLabel=Label(groceryFrame,text='Tea',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

teaEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
teaEntry.grid(row=5,column=1,pady=9,padx=10)
teaEntry.insert(0,0)

drinksFrame=LabelFrame(productsFrame,text=' Cold Drinks',font=('times new roman',15,'bold')
                                  ,fg='gold',bd=8,relief=GROOVE,bg='grey20')
drinksFrame.grid(row=0, column=2)

maazaLabel=Label(drinksFrame,text='Maaza',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
maazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

maazaEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
maazaEntry.grid(row=0,column=1,pady=9,padx=10)
maazaEntry.insert(0,0)

pepsiLabel=Label(drinksFrame,text='Pepsi',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

pepsiEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10)
pepsiEntry.insert(0,0)

spriteLabel=Label(drinksFrame,text='Sprite',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

spriteEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=2,column=1,pady=9,padx=10)
spriteEntry.insert(0,0)

dewLabel=Label(drinksFrame,text='Dew',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
dewLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

dewEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
dewEntry.grid(row=3,column=1,pady=9,padx=10)
dewEntry.insert(0,0)

frootiLabel=Label(drinksFrame,text='Frooti',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

frootiEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
frootiEntry.grid(row=4,column=1,pady=9,padx=10)
frootiEntry.insert(0,0)

cococolaLabel=Label(drinksFrame,text='Coco Cola',font=('times new roman',15,'bold')
                ,bg='grey20',fg='white')
cococolaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

cococolaEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cococolaEntry.grid(row=5,column=1,pady=9,padx=10)
cococolaEntry.insert(0,0)

billFrame=Frame(productsFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0,column=3,padx=10)

billareaLabel=Label(billFrame,text=' Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billFrame,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold')
                                  ,fg='gold',bd=8,relief=GROOVE,bg='grey20')
billmenuFrame.pack()

cosmeticspriceLabel=Label(billmenuFrame,text='Cosmetic Price',font=('times new roman',14,'bold')
                ,bg='grey20',fg='white')
cosmeticspriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')
cosmeticspriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cosmeticspriceEntry.grid(row=0,column=1,pady=6,padx=10)
grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=('times new roman',14,'bold')
                ,bg='grey20',fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=6,padx=10,sticky='w')
grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10)
drinkspriceLabel=Label(billmenuFrame,text=' Cold Drinks Price',font=('times new roman',14,'bold')
                ,bg='grey20',fg='white')
drinkspriceLabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')
drinkspriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
drinkspriceEntry.grid(row=2,column=1,pady=6,padx=10)

cosmeticstaxLabel=Label(billmenuFrame,text='Cosmetic Tax',font=('times new roman',14,'bold')
                ,bg='grey20',fg='white')
cosmeticstaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')
cosmeticstaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cosmeticstaxEntry.grid(row=0,column=3,pady=6,padx=10)
grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax',font=('times new roman',14,'bold')
              ,bg='grey20',fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')
grocerytaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10)
drinkstaxLabel=Label(billmenuFrame,text=' Cold Drinks Tax',font=('times new roman',14,'bold')
                ,bg='grey20',fg='white')
drinkstaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')
drinkstaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
drinkstaxEntry.grid(row=2,column=3,pady=6,padx=10)
buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0, column=4,rowspan=3)
totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='grey20',fg='white'
                   ,bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0 ,pady=20,padx=5)
billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='grey20',fg='white'
                   ,bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1 ,pady=20,padx=5)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='grey20',fg='white'
                   ,bd=5,width=8,pady=10 ,command=send_email)
emailButton.grid(row=0,column=2 ,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='grey20',fg='white'
                   ,bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='grey20',fg='white'
                   ,bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4 ,pady=20,padx=5)

root.mainloop()

