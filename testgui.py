import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import requests
from backendclass import *
import math
from tkvideo import tkvideo


API_URL = "http://127.0.0.1:8000"

root = tk.Tk()
root.title("Epic Game Store")
root.geometry("1200x600")
root.config(bg='white')
root.resizable(False, False)
add_cart = tk.PhotoImage(file="./image/addtocart.png")
add_wishlist = tk.PhotoImage(file="./image/addtowishlist.png")
buy_now = tk.PhotoImage(file="./image/buynow.png")
poohlogin = Image.open("./image/poohlogin.png")
poohlogin = poohlogin.resize((650, 600), Image.ANTIALIAS)
poohlogin = ImageTk.PhotoImage(poohlogin)
login_logo = tk.PhotoImage(file="./image/login.png")
register_logo = tk.PhotoImage(file="./image/register.png")
cart = tk.PhotoImage(file="./image/cart.png")
wishlist = tk.PhotoImage(file="./image/wishlist.png")
account = tk.PhotoImage(file="./image/account.png")
storename = tk.PhotoImage(file="./image/press start.png")
sky = tk.PhotoImage(file="./image/sky.png")
cc_image = tk.PhotoImage(file="./image/cc_image.png")
pp_image = tk.PhotoImage(file="./image/pp_image.png")
saved_image = tk.PhotoImage(file="./image/saved_image.png")
remove = tk.PhotoImage(file="./image/remove.png")
def show_notification(message):
    notification_window = tk.Toplevel(root)
    notification_window.geometry("300x50+500+300")
    notification_window.overrideredirect(True) # Remove title bar and borders
    notification_window.configure(bg="blue") # Set background color
    notification_window.lift(aboveThis=root) # Set window level above root window
    
    notification_label = tk.Label(notification_window, text=message, fg="black", bg="blue")
    notification_label.pack(padx=10,pady=10)
    
    # After 2 seconds, destroy the notification window
    root.after(2000, notification_window.destroy)

class CurrentUser():
    def __init__(self, user_id):
        self._user_id = user_id

    @property
    def user_id(self):
        return self._user_id
    @user_id.setter
    def user_id(self, value):
        self._user_id = value

current_user = CurrentUser(None)


def fetch_games():
    response = requests.get(API_URL + "/")
    if response.status_code == 200:
        return response.json()
    else:
        return []
def add_to_cart():
    pass
def get_images(games):
    images = []
    for gm in games:
        link = gm["_image_url"]
        image = Image.open(requests.get(link, stream=True).raw)
        image = image.resize((200, 270), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        images.append(image)
    return images


class ScrollableFrame(tk.Frame):
    def __init__(self, parent,w, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # create a canvas object and a vertical scrollbar
        canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview,width=20)
        self.scrollable_frame = tk.Frame(canvas,bg='white')
        # configure the canvas to scroll the frame
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # bind the canvas to respond to resize events
        self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.config(bg='white', width = w)
        # pack the canvas and scrollbar widgets
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

class Login(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH,expand=True)
        self.login_bg = tk.Label(self,bg='black')
        self.player = tkvideo("./image/poohfly.mp4",self.login_bg,loop=True,size=(1000,600))
        self.player.play()
        self.login_bg.pack(side =LEFT,fill=BOTH,expand=True)
        self.login_frame = tk.Frame(self,bg='white',width=200,height=400, highlightthickness=2, highlightbackground='black')
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.top_bar = tk.Frame(self,bg='white',width=1000,height=60,highlightthickness=2, highlightbackground='white')
        self.store_name = tk.Label(self.top_bar,image = storename,bg='black')
        self.store_name.pack()
        self.top_bar.place(relx=0.5, rely=0, anchor=N)
        self.button()
        
    def button(self):
        for widget in self.login_frame.winfo_children():
            widget.destroy()
        self.columnconfigure(1,weight=1)
        self.rowconfigure(0, weight=1)
        self.button_login = tk.Label(self.login_frame,image=login_logo,bg='#ffffff')
        self.button_login.bind("<Button-1>", self.login)
        self.button_login.pack(side="top")
        self.button_register = tk.Label(self.login_frame,image=register_logo,bg='#ffffff')
        self.button_register.bind("<Button-1>", self.signup)
        self.button_register.pack(side="top")

    def use_button_func(self,event):
        self.button()

    def login(self,event):
        for widget in self.login_frame.winfo_children():
            widget.destroy()
        self.back_to_choice = tk.Label(self.login_frame,text='Back',font=("Trebuchet MS", 24, "bold"),bg='#E32C1D',fg='#F1F351', bd=2, relief="raised")
        self.back_to_choice.bind("<Button-1>",self.use_button_func)
        self.login_label = tk.Label(self.login_frame,text='Login',font=("Trebuchet MS", 24, "bold"),bg='white',fg='black')
        self.username_label = tk.Label(self.login_frame,text='Username',font=("Trebuchet MS", 14, "bold"),bg='white',fg='black')
        self.username_entry = tk.Entry(self.login_frame,text= 'username', width=30, font=("Trebuchet MS", 14),bg='white',fg='black')
        self.password_label = tk.Label(self.login_frame,text='Password',font=("Trebuchet MS", 14, "bold"),bg='white',fg='black')
        self.password_entry = tk.Entry(self.login_frame,text = 'password', width=30, font=("Trebuchet MS", 14),bg='white',fg='black')
        self.summit_login = tk.Label(self.login_frame,image=login_logo,bg='white')
        self.summit_login.bind("<Button-1>", self.login_authentication)
        self.back_to_choice.pack(side=TOP,padx=10,pady=10)
        self.login_label.pack(side=TOP,padx=10,pady=10)
        self.username_label.pack(side=TOP,padx=10,pady=5)
        self.username_entry.pack(side=TOP,padx=10,pady=5)
        self.password_label.pack(side=TOP,padx=10,pady=5)
        self.password_entry.pack(side=TOP,padx=10,pady=5)
        self.summit_login.pack(side=TOP,padx=10,pady=10)

    def login_authentication(self,event):
        try:
            int(self.password_entry.get())
            pass
        except:
            self.status_label = tk.Label(self.login_frame,text='Invalid Password',bg='#BBF0F0')
            self.status_label.pack()
            return False
        search_query = {'username' : self.username_entry.get(), 'password' : int(self.password_entry.get())}
        response = requests.post(API_URL + "/login", json=search_query)
        if response.status_code == 200:
            result = response.json()
            if result:
                print('success')
                current_user._user_id = result
                self.destroy()
                HomePage(root)
            else:
                print('failure')
                self.status_label = tk.Label(self.login_frame,text='Incorrect Username or Password',bg='#BBF0F0')
                self.status_label.pack()
                root.after(200,self.status_label.destroy())

    def signup(self,event):
        for widget in self.login_frame.winfo_children():
            widget.destroy()
        self.back_to_choice = tk.Label(self.login_frame,text='Back',font=("Trebuchet MS", 24, "bold"),bg='#E32C1D',fg='#F1F351', bd=2, relief="raised")
        self.back_to_choice.bind("<Button-1>",self.use_button_func)
        self.register_label = tk.Label(self.login_frame,text='Register',font=("Trebuchet MS", 24, "bold"),bg='white',fg='black')
        self.username_label = tk.Label(self.login_frame,text='Username',font=("Trebuchet MS", 14, "bold"),bg='white',fg='black')
        self.username_entry = tk.Entry(self.login_frame, width=20, font=("Trebuchet MS", 14),bg='white',fg='black')
        self.password_label = tk.Label(self.login_frame,text='Password',font=("Trebuchet MS", 14, "bold"),bg='white',fg='black')
        self.password_entry = tk.Entry(self.login_frame, width=20, font=("Trebuchet MS", 14),bg='white',fg='black')
        self.email_label = tk.Label(self.login_frame,text='Email',font=("Trebuchet MS", 14, "bold"),bg='white',fg='black')
        self.email_entry = tk.Entry(self.login_frame, width=20, font=("Trebuchet MS", 14),bg='white',fg='black')
        self.summit_register = tk.Label(self.login_frame,image=register_logo,bg='white')
        self.summit_register.bind("<Button-1>", self.register_authentication)
        self.back_to_choice.pack(side=TOP,padx=10,pady=10)
        self.register_label.pack(side=TOP,padx=10,pady=10)
        self.username_label.pack(side=TOP,padx=10,pady=10)
        self.username_entry.pack(side=TOP,padx=10,pady=10)
        self.password_label.pack(side=TOP,padx=10,pady=10)
        self.password_entry.pack(side=TOP,padx=10,pady=10)
        self.email_label.pack(side=TOP,padx=10,pady=10)
        self.email_entry.pack(side=TOP,padx=10,pady=10)
        self.summit_register.pack(side=TOP,padx=10,pady=10)

    def register_authentication(self,event):
        try:
            int(self.password_entry.get())
            pass
        except:
            self.status_label = tk.Label(self.login_frame,text='Invalid Username',bg='#BBF0F0')
            self.status_label.pack()
            return False
        search_query = {'username' : self.username_entry.get(), 'password' : int(self.password_entry.get()),'email' : self.email_entry.get()}
        response = requests.post(API_URL + "/sign_up", json=search_query)
        if response.status_code == 200:
            result = response.json()
            print(result)
            if result:
                print('success')
                current_user._user_id = result
                self.destroy()
                HomePage(root)
            else:
                print('failure')
                self.status_label = tk.Label(self.login_frame,text='Invalid Username',bg='#BBF0F0')
                self.status_label.pack()
        else:
            print('no')

class HomePage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH,expand=True)
        self.games = fetch_games()
        self.images = get_images(self.games)
        self.init_games = self.games
        self.init_images = self.images
        self.topbar()
        self.body_frame()
        self.catalog_frame()
        self.detail_frame()
        self.bottombar()

    def topbar(self):
        self.top_bar = tk.Frame(self, bg="white", height=60)
        self.top_bar.pack(side='top', fill=tk.X)
        self.store_name = tk.Label(self.top_bar, text="NongShan", font=("Trebuchet MS", 36, "bold"), fg="#ABEBC6",bg="white")
        self.store_name.pack(side='left', padx=10, pady=10)
        self.store_name.bind("<Button-1>", self.back_to_homepage)
        self.search_entry = tk.Entry(self.top_bar, width=60, font=("Trebuchet MS", 14),bg='white')
        self.search_entry.bind("<KeyRelease>", self.delayed_on_entry_change)
        self.search_entry.pack(side = 'left',padx=(120, 30), pady=(20, 10),)
        self.cart_view = tk.Button(self.top_bar,image=cart,command=self.view_cart,bg='white')
        self.wishlist_view = tk.Button(self.top_bar,bg='white',image=wishlist,command=self.view_wishlist)
        self.account_view = tk.Button(self.top_bar,bg='white',image=account,command=self.view_account)
        self.account_view.pack(side='right', padx=10, pady=10)
        self.wishlist_view.pack(side='right', padx=10, pady=10)
        self.cart_view.pack(side='right', padx=10, pady=10)

    def view_account(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.topbar()
        self.body_frame()
        self.bottombar()
        self.account_detail = ScrollableFrame(self.body,900)
        self.account_detail.pack(side=LEFT,padx=20,pady=20,fill=BOTH)
        row_frame1 = tk.Frame(self.account_detail.scrollable_frame,bg='white')
        user_info = requests.get(API_URL + f"/user/user_info/{current_user.user_id}").json()
        username = user_info['_username']
        psw = user_info['_password']
        email = user_info['_email']
        title1 = tk.Label(row_frame1,text=f'User Information',font=("Trebuchet MS", 30, "bold"))
        name = tk.Label(row_frame1,text=f'Username : {username}',font=("Trebuchet MS", 20, "bold"))
        password = tk.Label(row_frame1,text=f'Password : {psw}',font=("Trebuchet MS", 20, "bold"))
        Email = tk.Label(row_frame1,text=f'Email : {email}',font=("Trebuchet MS", 20, "bold"))
        title1.pack(side=TOP)
        name.pack(side=TOP,pady=20)
        password.pack(side=TOP,pady=20)
        Email.pack(side=TOP,pady=20)
        row_frame1.pack(side="top", fill="x", padx=5, pady=5)
        row_frame2 = tk.Frame(self.account_detail.scrollable_frame,bg='white')
        payment_info = requests.get(API_URL + f"/user/payment_info/{current_user.user_id}")
        payment_info = payment_info.json()
        cc = payment_info['_credit_card']
        pp = payment_info['_paypal']
        title2 = tk.Label(row_frame2,text=f'Payment Information',font=("Trebuchet MS", 30, "bold"))
        title2.pack(side=TOP)
        cc_title = tk.Label(row_frame2,text=f'Credit Card',font=("Trebuchet MS", 25, "bold"),bg='black')
        cc_title.pack(side=TOP,pady=20)
        for card in cc.values():
            card_name = card['_name']
            card_number = card['_card_number']
            show_card = tk.Label(row_frame2,text=f'Name: {card_name} Card Number: {card_number}',font=("Trebuchet MS", 20, "bold"))
            show_card.pack(side=TOP,pady=20)
        pp_title = tk.Label(row_frame2,text=f'Paypal',font=("Trebuchet MS", 25, "bold"))
        pp_title.pack(side=TOP,pady=20)
        for mail in pp.values():
            email = mail['_paypal_email']
            show_card = tk.Label(row_frame2,text=f'Email: {email}',font=("Trebuchet MS", 20, "bold"))
            show_card.pack(side=TOP,pady=20)
        row_frame2.pack(side="top", fill="x", padx=5, pady=5)
        row_frame3 = tk.Frame(self.account_detail.scrollable_frame,bg='white')
        ph_info = requests.get(API_URL + f"/user/shopping_info/{current_user.user_id}").json()
        ph_title = tk.Label(row_frame3,text='Purchase History',font=("Trebuchet MS", 25, "bold"))
        ph_title.pack(side=TOP,pady=20)
        for info in ph_info:
            title = info['_game_title']
            price = info['_price']
            date = info['_date']
            payment = info['_payment_type']
            payment_detail = info['_payment_info']
            show_ph = tk.Label(row_frame3,text=f'Game: {title} Price: {price} Date: {date} Paid Using {payment}: {payment_detail}',font=("Trebuchet MS", 10, "bold"))
            show_ph.pack(side=TOP,pady=20)
        row_frame3.pack(side="top", fill="x", padx=5, pady=5)
    def back_to_homepage(self,event):
        for widget in self.winfo_children():
            widget.destroy()
        self.games = self.init_games
        self.images = self.init_images
        self.topbar()
        self.body_frame()
        self.catalog_frame()
        self.detail_frame()
        self.bottombar()
    def view_cart(self):
        response = requests.get(API_URL + f"/cart/{current_user.user_id}")
        if response.status_code == 200:
            result = response.json()
            self.game_cart = result
            for widget in self.winfo_children():
                widget.destroy()
            self.games = [x for x in result.values()]
            self.images = get_images(self.games)
            self.game_in_cart()
            self.payment_cart()
        else:print('error')
        
    def game_in_cart(self):
        self.topbar()
        self.body_frame()
        self.bottombar()
        self.cart_catalog = ScrollableFrame(self.body,800)
        self.cart_catalog.pack(side=LEFT,padx=20,pady=20,fill=BOTH)
        
        for gm in range(len(self.games)):
            selected = self.games[gm]
            row_frame = tk.Frame(self.cart_catalog.scrollable_frame,bg='white')
            image = self.images[gm]
            game_image = tk.Label(row_frame,image=image,bg='white')
            game_image.pack(side='left',padx=10,pady=10)
            game_title = tk.Label(row_frame,text= selected['_title'],font=("Times New Roman", 20, "bold"),bg='white',fg='black')
            game_title.pack(side='left',padx=10,pady=10) 
            price = selected['_price']
            game_price = tk.Label(row_frame,text= f'Price : {price} Bath',font=("Times New Roman", 20, "bold"),bg='white',fg='black')
            game_price.pack(side='left',padx=10,pady=10)
            remove_logo = tk.Label(row_frame,image=remove,bg='white')
            remove_logo.pack(side='right',padx=5,pady=10)
            remove_logo.bind('<Button-1>', lambda e, title= selected['_title']:self.remove_cart(title))
            add_wishlist_logo = tk.Label(row_frame,image=add_wishlist,bg='white')
            add_wishlist_logo.pack(side='right',padx=5,pady=10)
            add_wishlist_logo.bind('<Button-1>', lambda e, title= selected['_title']:self.add_wishlist(title))
            row_frame.pack(side="top", fill="x", padx=5, pady=5)
    def payment_cart(self):
        self.detail_cart_frame = tk.Frame(self.body,bg='white')
        self.detail_cart_frame.pack(side=RIGHT,padx=20,pady=20,fill=BOTH,expand=True)
        response = requests.get(API_URL + f"/cart/get_total_price/{current_user.user_id}")
        if response.status_code == 200:
            result = response.json()
            self.total_price = tk.Label(self.detail_cart_frame,text=f'Total Price is {result}',font= ("Times New Roman", 35, "bold"),bg='white',fg='black')
            self.total_price.pack(pady=60)
            self.purchase_button = tk.Button(self.detail_cart_frame, text='Purchase', font=("Times New Roman", 40, "bold"), command=lambda: self.purchase_frame('no'))
            self.purchase_button.pack(pady=60)
        else:print('error')
    def view_wishlist(self):
        response = requests.get(API_URL + f"/wishlist/{current_user.user_id}")
        if response.status_code == 200:
            result = response.json()
            for widget in self.winfo_children():
                widget.destroy()
            print(result)
            self.games = [x for x in result.values()]
            self.images = get_images(self.games)
            self.game_in_wishlist()
        else:print('error')
    def game_in_wishlist(self):
        self.topbar()
        self.body_frame()
        self.bottombar()
        self.wishlist_catalog = ScrollableFrame(self.body,1000)
        self.wishlist_catalog.pack(side=LEFT,padx=20,pady=20,fill=BOTH)
        
        for gm in range(len(self.games)):
            selected = self.games[gm]
            row_frame = tk.Frame(self.wishlist_catalog.scrollable_frame,bg='white')
            image = self.images[gm]
            game_image = tk.Label(row_frame,image=image,bg='white')
            game_image.pack(side='left',padx=10,pady=10)
            game_title = tk.Label(row_frame,text= selected['_title'],font=("Times New Roman", 20, "bold"),bg='white',fg='black')
            game_title.pack(side='left',padx=10,pady=10) 
            price = selected['_price']
            game_price = tk.Label(row_frame,text= f'Price : {price} Bath',font=("Times New Roman", 20, "bold"),bg='white',fg='black')
            game_price.pack(side='left',padx=10,pady=10)
            remove_logo = tk.Label(row_frame,image=remove,bg='white')
            remove_logo.pack(side='right',padx=5,pady=10)
            remove_logo.bind('<Button-1>', lambda e, title= selected['_title']:self.remove_wishlist(title))
            add_cart_logo = tk.Label(row_frame,image=add_cart,bg='white')
            add_cart_logo.pack(side='right',padx=10,pady=10)
            add_cart_logo.bind('<Button-1>', lambda e, title= selected['_title']:self.add_cart(title))
            row_frame.pack(side="top", fill="x", padx=5, pady=5)
    def body_frame(self):
        self.body = tk.Frame(self, bg="#F6A998")
        self.body.pack(side='top',fill=BOTH, expand=True)
        self.body_bg = tk.Label(self.body,image =sky)
        self.body_bg.place(x=0, y=0, relwidth=1, relheight=1)
    def catalog_frame(self):
        self.game_catalog = ScrollableFrame(self.body,750)
        self.game_catalog.pack(side=LEFT,padx=20,pady=20,fill=BOTH)

        for i in range(math.ceil(len(self.games)/3)):
            index = i*3
            row_frame = tk.Frame(self.game_catalog.scrollable_frame,bg='white')
            selected_game1 = self.games[index]
            game1 = tk.Frame(row_frame,bg='white',width=200,height=200)
            game_image1 = self.images[index]
            image_label1 = tk.Label(game1, image=game_image1,bg='white')
            image_label1.pack(padx=5, pady=5, expand=True, fill="x")
            text1 = tk.Label(game1,text=selected_game1["_title"],font = ("Times New Roman", 12, "bold"),bg='white',fg='black')
            text1.pack(side="top", padx=5, pady=5, expand=True, fill="x")
            image_label1.bind('<Button-1>', lambda e, idx=index: self.show_details(self.games[idx]))
            game1.grid(row=0,column=0,padx=10,pady=10)
            if i*3+1 < len(self.games):
                selected_game2 = self.games[index+1]
                game2 = tk.Frame(row_frame,bg='white',width=200,height=200)
                game_image2 = self.images[index+1]
                image_label2 = tk.Label(game2, image=game_image2,bg='white')
                image_label2.pack(padx=5, pady=5, expand=True, fill="x")
                text2 = tk.Label(game2,text=selected_game2['_title'],font = ("Times New Roman", 12, "bold"),bg='white',fg='black')
                text2.pack(side="top", padx=5, pady=5, expand=True, fill="x")
                image_label2.bind('<Button-1>', lambda e, idx=index+1: self.show_details(self.games[idx]))
                game2.grid(row=0,column=1,padx=10,pady=10,)
            if i*3+2 < len(self.games):
                selected_game3 = self.games[index+2]
                game3 = tk.Frame(row_frame,bg='white',width=200,height=200)
                game_image3 = self.images[index+2]
                image_label3 = tk.Label(game3, image=game_image3,bg='white')
                image_label3.pack(padx=5, pady=5, expand=True, fill="x")
                text3 = tk.Label(game3,text=selected_game3['_title'],font = ("Times New Roman", 12, "bold"),bg='white',fg='black')
                text3.pack(side="top", padx=5, pady=5, expand=True, fill="x")
                image_label3.bind('<Button-1>', lambda e, idx=index+2: self.show_details(self.games[idx]))
                game3.grid(row=0,column=2,padx=10,pady=10,sticky=E)
            row_frame.pack(side="top", fill="x", padx=5, pady=5)

    def detail_frame(self):
        self.detail_game_frame = tk.Frame(self.body,bg='white')
        self.detail_game_frame.pack(side=RIGHT,padx=20,pady=20,fill=BOTH,expand=True)

    def show_details(self,selected_game):
        # Clear the game details frame
        for widget in self.detail_game_frame.winfo_children():
            widget.destroy()

        if (selected_game['_price'] == 0):
            selected_game['_price'] = "Free"

        game_image = Image.open(requests.get(selected_game['_image_url'], stream=True).raw)
        game_image = game_image.resize((400, 150), Image.ANTIALIAS)
        game_image = ImageTk.PhotoImage(game_image)

        # Use a label widget to display the game image
        image_label = tk.Label(self.detail_game_frame, image=game_image)
        image_label.image = game_image
        image_label.pack(side="top", padx=10, pady=10)
        
        # Set the font size and style for game title, price, and details
        name_font = ("Times New Roman", 24, "bold")
        details_font = ("Times New Roman", 12)

        # Use a label widget to display the game details
        game_details = tk.Label(self.detail_game_frame, font=name_font, text=selected_game['_title'], fg="black", bg="white")
        game_details.pack(side="top", padx=10, pady=2)

        price_label = tk.Label(self.detail_game_frame, font=("Trebuchet MS", 16, "bold"), text=f"Price: {selected_game['_price']}", fg="black", bg="white")
        price_label.pack(side="top", padx=10, pady=0)

        details_label = tk.Label(self.detail_game_frame, font=details_font, text=selected_game['_details'], wraplength=400, fg="black", bg="white")
        details_label.pack(side="top", padx=10, pady=3)

        shopping_detail_frame = tk.Frame(self.detail_game_frame,bg='white')
        buy_now_logo = tk.Label(shopping_detail_frame,image=buy_now,bg='white')
        buy_now_logo.grid(row= 0,column=0,sticky=N)
        buy_now_logo.bind('<Button-1>', lambda e, game= selected_game:self.purchase_frame(game))
        add_cart_logo = tk.Label(shopping_detail_frame,image=add_cart,bg='white')
        add_cart_logo.grid(row= 1,column=0,sticky=W)
        add_cart_logo.bind('<Button-1>', lambda e, title= selected_game['_title']:self.add_cart(title))
        add_wishlist_logo = tk.Label(shopping_detail_frame,image=add_wishlist,bg='white')
        add_wishlist_logo.grid(row= 0,column=1,rowspan=2,sticky=E)
        add_wishlist_logo.bind('<Button-1>', lambda e, title= selected_game['_title']:self.add_wishlist(title))
        shopping_detail_frame.pack(side = 'bottom', padx=(20,20), pady=20)
    def remove_cart(self, title):
        user_id = current_user.user_id
        game_title = title
        response = requests.delete(API_URL + f"/wishlist/remove_from_cart/{user_id}/{game_title}")
        if response.status_code == 200:
            result = response.json()
            if result:
                show_notification(f'Your {title} game is removed from cart')
        else:
            show_notification(f'Your {title} game is failed to be remmoved from cart')
    def remove_wishlist(self,title):
        user_id = current_user.user_id
        game_title = title
        response = requests.delete(API_URL + f"/wishlist/remove_from_wishlist/{user_id}/{game_title}")
        if response.status_code == 200:
            result = response.json()
            if result:
                show_notification(f'Your {title} game is added to wishlist')
        else:
            show_notification(f'Your {title} game is failed to be added to wishlist')

    def add_wishlist(self,title):
        user_id = current_user.user_id
        game_title = title
        response = requests.post(API_URL + f"/wishlist/add_to_wishlist/{user_id}/{game_title}")
        if response.status_code == 200:
            result = response.json()
            if result:
                show_notification(f'Your {title} game is added to wishlist')
        else:
            show_notification(f'Your {title} game is failed to be added to wishlist')

    def add_cart(self,title):
        user_id = current_user.user_id
        game_title = title
        response = requests.post(API_URL + f"/cart/add_to_cart/{user_id}/{game_title}")
        if response.status_code == 200:
            result = response.json()

            print(result)
            if result:
                print('success')
                show_notification(f'Your {title} game is added to cart')
        else:
            show_notification(f'Your {title} game is failed to be added to cart')
    def bottombar(self):
        self.bottom_bar = tk.Frame(self, bg="black", height=40)
        self.bottom_bar.pack(side='bottom', fill=tk.X)
    #event for searching game
    def delayed_on_entry_change(self, event):
        root.after(400, self.on_entry_change)

    def on_entry_change(self):
        print(self.search_entry.get())
        self.game_catalog.destroy()
        self.game_catalog = None
        
        if self.search_entry.get() == "":
            self.games = self.init_games
            self.images = self.init_images
            self.catalog_frame()
        else:
            search_query = self.search_entry.get().lower()
            self.games = [game for game in self.init_games if search_query in game['_title'].lower()]
            self.images = get_images(self.games)
            self.catalog_frame()
    def purchase_frame(self,games):
        for widget in self.winfo_children():
            widget.destroy()
        self.topbar()
        self.body_frame()
        self.bottombar()
        self.status = games
        self.purchase_games = self.games
        self.purchase_games_images = self.images
        if games != 'no':
            self.purchase_games = games['_title']
            self.purchase_games_images = get_images([games])
        total_price = requests.get(API_URL + f"/cart/get_total_price/{current_user.user_id}").json()
        self.payment_info_frame = tk.Frame(self.body,width=800,bg='white')
        self.payment_info_frame.pack(side=LEFT,padx=40,pady=20,fill=BOTH)
        self.payment_method_frame = tk.Frame(self.payment_info_frame,height=100,bg='white')
        self.credit_card_button = tk.Label(self.payment_method_frame,image=cc_image,bg='white')
        self.credit_card_button.bind('<Button-1>', self.pay_with_credit_card)
        self.credit_card_button.pack(side=LEFT)
        self.paypal_button = tk.Label(self.payment_method_frame,image=pp_image,bg='white')
        self.paypal_button.bind('<Button-1>', self.pay_with_paypal)
        self.paypal_button.pack(side=LEFT)
        self.own_button = tk.Label(self.payment_method_frame,image=saved_image,bg='white')
        self.own_button.bind('<Button-1>', self.pay_with_own)
        self.own_button.pack(side=LEFT)
        self.payment_method_frame.pack(side=TOP,padx=20,pady=10,fill=BOTH)
        self.collect_info_frame = tk.Frame(self.payment_info_frame,bg='white')
        self.collect_info_frame.pack(side=TOP,padx=20,pady=20,fill=BOTH,expand=True)
        self.purchase_scroll = ScrollableFrame(self.body,250)
        self.purchase_scroll.pack(side=LEFT,padx=5,pady=20,fill=BOTH)
        total = tk.Frame(self.purchase_scroll.scrollable_frame,bg='white')
        total_price_label = tk.Label(total,text=f'Total: {total_price}',font = ("Times New Roman", 30, "bold"),bg='white',fg='black')
        total_price_label.pack(pady=10)
        total.pack(side="top", fill="x", padx=5, pady=5)
        for i in range(len(self.purchase_games)):
            row_frame = tk.Frame(self.purchase_scroll.scrollable_frame,bg='white')
            image = tk.Label(row_frame,image=self.purchase_games_images[i],bg='white')
            image.pack(pady=10)
            price = self.purchase_games[i]['_price']
            price = tk.Label(row_frame,text= f'Price: {price}',font = ("Times New Roman", 20, "bold"),bg='white',fg='black')
            price.pack(pady=5)
            row_frame.pack(side="top", fill="x", padx=5, pady=5)
    def pay_with_credit_card(self,event):
        for widget in self.collect_info_frame.winfo_children():
                widget.destroy()
        fullname_label = tk.Label(self.collect_info_frame,text= "Full Name:",font = ("Trebuchet MS", 20, "bold"))
        self.entryname = tk.Entry(self.collect_info_frame,width=10,font=("Trebuchet MS", 14))
        card_label = tk.Label(self.collect_info_frame,text= "Card Number:",font = ("Trebuchet MS", 20, "bold"))
        self.entrycard = tk.Entry(self.collect_info_frame,width=10,font=("Trebuchet MS", 14))
        exp_label = tk.Label(self.collect_info_frame,text= "Expiration Date:",font = ("Trebuchet MS", 20, "bold"))
        self.entryexp = tk.Entry(self.collect_info_frame,width=10,font=("Trebuchet MS", 14))
        cvv_label = tk.Label(self.collect_info_frame,text= "CVV:",font = ("Trebuchet MS", 30, "bold"))
        self.entrycvv = tk.Entry(self.collect_info_frame,width=10,font=("Trebuchet MS", 14))
        save_label = tk.Label(self.collect_info_frame,text='Save (yes/no)',font=("Trebuchet MS",30,'bold'))
        self.entrysave = tk.Entry(self.collect_info_frame,width=10,font=("Trebuchet MS", 14))
        fullname_label.grid(column = 0,row = 0,padx=10,pady=10)
        self.entryname.grid(column=1,row=0,padx=10,pady=10)
        card_label.grid(column = 0,row = 1,padx=10,pady=10)
        self.entrycard.grid(column=1,row=1,padx=10,pady=10)
        exp_label.grid(column = 0,row = 2,padx=10,pady=10)
        self.entryexp.grid(column=1,row=2,padx=10,pady=10)
        cvv_label.grid(column=0,row=3,padx=10,pady=10)
        self.entrycvv.grid(column=1,row=3,padx=10,pady=10)
        save_label.grid(column=0,row=4,padx=10,pady=10)
        self.entrysave.grid(column=1,row=4,padx=10,pady=10)
        self.purchase_summit = tk.Button(self.collect_info_frame, text='Purchase', font=("Trebuchet MS", 40, "bold"), command=self.cc_summit)
        self.purchase_summit.grid(column=0,row=5,padx=10,pady=10)
    def cc_summit(self):
        user_id = current_user.user_id
        name = self.entryname.get()
        card_number = self.entrycard.get()
        expiration = self.entryexp.get()
        cvv = self.entrycvv.get()
        game_title = self.status
        if self.entrysave == 'yes':save = True
        else: save = False
        response = requests.post(API_URL + f"/payment/creditcard/{user_id}/{name}/{card_number}/{expiration}/{cvv}/{save}/{game_title}")
        if response.status_code == 200:
            result = response.json()
            if result:
                print('success')
                show_notification(f'Your Purchase was successfully')

        else:
            show_notification(f'Your Purchase was not successfully')
    def pay_with_paypal(self,event):
        for widget in self.collect_info_frame.winfo_children():
                widget.destroy()
        email_label = tk.Label(self.collect_info_frame,text= "Full Name:",font = ("Trebuchet MS", 20, "bold"))
        self.entryemail = tk.Entry(self.collect_info_frame,width=10,font=("Trebuchet MS", 14))
        psw_label = tk.Label(self.collect_info_frame,text= "Card Number:",font = ("Trebuchet MS", 20, "bold"))
        self.entrypsw = tk.Entry(self.collect_info_frame,width=10,font=("Trebuchet MS", 14))
        save_label = tk.Label(self.collect_info_frame,text='Save (yes/no)',font=("Trebuchet MS",30,'bold'))
        self.entrysave = tk.Entry(self.collect_info_frame,width=10,font=("Trebuchet MS", 14))
        email_label.grid(column = 0,row = 0,padx=10,pady=10)
        self.entryemail.grid(column=1,row=0,padx=10,pady=10)
        psw_label.grid(column = 0,row = 1,padx=10,pady=10)
        self.entrypsw.grid(column=1,row=1,padx=10,pady=10)
        save_label.grid(column=0,row=2,padx=10,pady=10)
        self.entrysave.grid(column=1,row=2,padx=10,pady=10)
        self.purchase_summit = tk.Button(self.collect_info_frame, text='Purchase', font=("Trebuchet MS", 40, "bold"), command=self.pp_summit)
        self.purchase_summit.grid(column=0,row=3,padx=10,pady=10)
    def pp_summit(self):
        user_id = current_user.user_id
        email = self.entryemail.get()
        password = self.entrypsw.get()
        game_title = self.status
        if self.entrysave == 'yes':save = True
        else: save = False
        response = requests.post(API_URL + f"/payment/paypal/{user_id}/{email}/{password}/{save}/{game_title}")
        if response.status_code == 200:
            result = response.json()
            if result:
                print('success')
                show_notification(f'Your Purchase was successfully')

        else:
            show_notification(f'Your Purchase was not successfully')
    def pay_with_own(self):
        pass
signup = Login(root)


root.mainloop()