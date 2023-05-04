import datetime

class Game:
    def __init__(self, title : str, price : float, details : str,image_url : str):
        self._title = title
        self._price = price
        self._details = details
        self._image_url = image_url
    @property
    def title(self):
        return self._title

    @property
    def price(self):
        return self._price

    @property
    def details(self):
        return self._details
    
    @property
    def image_url(self):
        return self._image_url

class Catalog:
    def __init__(self):
        self._games = []

    @property
    def games(self):
        return self._games 

    def add_game(self, game):
        self._games.append(game)

    def remove_game(self, game):
        self._games.remove(game)

    def search_games(self, query):
        results = {}
        for game in self._games:
            if query in game.title:
                results = game
        return results

class UserManager:
    def __init__(self):
        self._users = []

    @property
    def users(self):
        return self._users
    @users.setter
    def users(self, users):
        self._users = users

    def add(self, user):
        if isinstance(user, User):
            self._users.append(user)
        else:
            raise TypeError("Object is not of type User.")
    def remove(self, user):
        if isinstance(user, User):
            self._users.remove(user)
        else:
            raise TypeError("Object is not of type User.")
    def search_user(self,user_id):
        for user in self._users:
            if user.user_info.user_id == user_id:
                return user

class User:
    def __init__(self, user_info, payment_info, shopping_info):
        self._user_info = user_info
        self._payment_info = payment_info
        self._shopping_info = shopping_info

    @property
    def user_info(self):
        return self._user_info

    @property
    def payment_info(self):
        return self._payment_info

    @property
    def shopping_info(self):
        return self._shopping_info

class Authentication:
    def __init__(self,user_manager):
        self._manager = user_manager

    def sign_up(self, username, password, email):
        # Check if username already exists
        for user in self._manager.users:
            if user.user_info.username == username:
                print("Username already exists.")
                return False
        user_id = len(self._manager.users)+1
        # Create new user
        user_info = UserInfo(username, password, email, user_id)
        payment_info = PaymentInfo(user_id)
        shopping_info = ShoppingInfo(user_id, PurchaseHistory(user_id), UserWishlist(user_id), ShoppingCart(user_id))
        new_user = User(user_info, payment_info, shopping_info)

        # Add the new user to the list of users
        self._manager.add(new_user)
        print(f"User {username} has been successfully registered.")
        return True

    def login(self, username, password):
        for user in self._manager.users:
            if user.user_info.username == username:
                if user.user_info.password == password:
                    print(f"User {username} has successfully logged in.")
                    return user
                else:
                    print("Incorrect password.")
                    return False
        print("User not found.")
        return False

class UserInfo:
    def __init__(self, username, password, email, user_id):
        self._username = username
        self._password = password
        self._email = email
        self._user_id = user_id

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, value):
        self._username = value
    
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        self._password = value
    
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        self._email = value
    
    @property
    def user_id(self):
        return self._user_id

class PaymentInfo:
    def __init__(self, user_id):
        self._user_id = user_id
        self._credit_card = {}
        self._paypal = {}

    @property
    def user_id(self):
        return self._user_id

    @property
    def credit_card(self):
        return self._credit_card
    
    @property
    def paypal(self):
        return self._paypal

    def add_credit_card(self, credit_card):
        self._credit_card[credit_card.name] = credit_card

    def remove_credit_card(self, credit_card):
        del self._credit_card[credit_card.name]
    
    def add_paypal(self, paypal):
        self._paypal[paypal.paypal_email] = paypal
    
    def remove_paypal(self, paypal):
        del self._paypal[paypal.paypal_email]

class CreditCard:
    def __init__(self, name, card_number, expiration_date, cvv):
        self._name = name
        self._card_number = card_number
        self._expiration_date = expiration_date
        self._cvv = cvv
    
    @property
    def name(self):
        return self._name

    @property
    def card_number(self):
        return self._card_number
    
    @property
    def expiration_date(self):
        return self._expiration_date
    
    @property
    def cvv(self):
        return self._cvv

class Paypal:
    def __init__(self, paypal_email, paypal_password):
        self._paypal_email = paypal_email
        self._paypal_password = paypal_password
    
    @property
    def paypal_email(self):
        return self._paypal_email

    @property
    def paypal_password(self):
        return self._paypal_password

class ShoppingInfo:
    def __init__(self, user_id, purchase_history, user_wishlist, user_cart):
        self._user_id = user_id
        self._purchase_history = purchase_history
        self._user_wishlist = user_wishlist
        self._user_cart = user_cart

    @property
    def user_id(self):
        return self._user_id

    @property
    def purchase_history(self):
        return self._purchase_history
    
    @property
    def user_wishlist(self):
        return self._user_wishlist

    @property
    def user_cart(self):
        return self._user_cart

class UserWishlist:
    def __init__(self, user_id):
        self._user_id = user_id
        self._items = {}
    
    @property
    def user_id(self):
        return self._user_id
    
    @property
    def items(self):
        return self._items
    
    def add_item(self, game):
        if game.title not in self.items:
            self.items[game.title] = game

    def remove_item(self, game):
        if game.title in self.items:
            del self.items[game.title]

    def clear_items(self):
        self.items = {}

class ShoppingCart:
    def __init__(self, user_id):
        self._user_id = user_id
        self._items = {}
        self._single_item = {}

    @property
    def user_id(self):
        return self._user_id
    
    @property
    def items(self):
        return self._items
    @items.setter
    def clear_items(self):
        self._items = {}
    def add_item(self, game):
        if game.title not in self.items:
            self.items[game.title] = game
    def remove_item(self, game):
        if game.title in self.items:
            del self.items[game.title]
    def get_total_price(self):
        total_price = 0
        for item in self.items.values():
            total_price += item.price
        return total_price
    
    @property
    def single_item(self):
        return self._single_item
    @single_item.setter
    def single_item(self, value):
        self._single_item = value


class PurchaseHistory:
    def __init__(self, user_id):
        self._user_id = user_id
        self._purchases = []

    @property
    def user_id(self):
        return self._user_id

    @property
    def purchases(self):
        return self._purchases

    def add_purchase(self, purchase):
        self._purchases.append(purchase)
class Purchase_info:
    def __init__(self,game_title,price,date,payment_type,payment_info):
        self._game_title = game_title
        self._price = price
        self._date = date
        self._payment_type = payment_type
        self._payment_info = payment_info
    
    @property
    def title(self):
        return self._game_title
    
    @property
    def price(self):
        return self._price
    
    @property
    def date(self):
        return self._date
    
    @property
    def payment_type(self):
        return self._payment_type
    
    @property
    def payment_info(self):
        return self._payment_info

class Purchase:
    def __init__(self, user):
        self._user = user
    
    def cart_purchase_CC(self,credit_card, save):
        #save new credit card
        if save == True and credit_card.name not in self._user.payment_info.credit_card:    
            self._user.payment_info.add_credit_card(credit_card)
        if self._user.shopping_info.user_cart.items != {}:
            #if purchase process is successful
            for game in self._user.shopping_info.user_cart.items.values():
                self._user.shopping_info.purchase_history.add_purchase(Purchase_info(game.title,game.price,datetime.datetime.now(),'Credit Card',credit_card.card_number))
            total_price = self._user.shopping_info.user_cart.get_total_price()
            self._user.shopping_info.user_cart.clear_items
            return f"Paid {total_price} using Creditcard {credit_card.card_number}"
        else:
            return False
    def one_purchase_CC(self,credit_card, save):
        #save new credit card
        if save == True and credit_card.name not in self._user.payment_info.credit_card:    
            self._user.payment_info.add_credit_card(credit_card)
        if self._user.shopping_info.user_cart.single_item != {}:
        #if purchase process is successful
            game = self._user.shopping_info.user_cart.single_item
            self._user.shopping_info.purchase_history.add_purchase(Purchase_info(game.title,game.price,datetime.datetime.now(),'Credit Card',credit_card.card_number))
            total_price = game.price
            self._user.shopping_info.user_cart.single_item = {}
            return f"Paid {total_price} using Creditcard {credit_card.card_number}"
        else:
            return False
    
    def cart_purchase_PP(self,paypal, save):
        #save new paypal payment
        if save == True and paypal.paypal_email not in self._user.payment_info.paypal:    
            self._user.payment_info.add_paypal(paypal)
        if self._user.shopping_info.user_cart.items != {}:
            #if purchase process is successful
            for game in self._user.shopping_info.user_cart.items.values():
                self._user.shopping_info.purchase_history.add_purchase(Purchase_info(game.title,game.price,datetime.datetime.now(),'Paypal',paypal.paypal_email))
            total_price = self._user.shopping_info.user_cart.get_total_price()
            self._user.shopping_info.user_cart.clear_items
            return f"Paid {total_price} using Paypal {paypal.paypal_email}"
        else:
            return False

    def one_purchase_PP(self,paypal, save):
        #save new paypal payment
        if save == True and paypal.paypal_email not in self._user.payment_info.paypal:    
            self._user.payment_info.add_paypal(paypal)
        if self._user.shopping_info.user_cart.single_item != {}:
            #if purchase process is successful
            game = self._user.shopping_info.user_cart.single_item
            print(game)
            self._user.shopping_info.purchase_history.add_purchase(Purchase_info(game.title,game.price,datetime.datetime.now(),'Paypal',paypal.paypal_email))
            total_price = game.price
            self._user.shopping_info.user_cart.single_item = {}
            return f"Paid {total_price} using Creditcard {paypal.paypal_email}"
        else:
            return False



# python3 -m uvicorn main:app --reload


# esc = False
# while esc == False:
#     login = input("Login or Sign up (1,2): ")
#     while login not in ['1','2']:
#         print('Please enter valid value')
#         login = input("Login or Sign up (1,2): ")
#     user = object()
#     if login == '1':
#         print('Login')
#         username = input("Username : ")
#         password = int(input("Password : "))
#         user = authentication.login(username, password)
#         while user == False:
#             print('Login')
#             username = input("Username : ")
#             password = int(input("Password : "))
#             user = authentication.login(username, password)
#     else:
#         print('Sign up')
#         username = input("Username : ")
#         password = int(input("Password : "))
#         email = input("Email : ")
#         user = authentication.sign_up(username, password, email)
#         while user == False:
#             username = input("Username : ")
#             password = int(input("Password : "))
#             email = input("Email : ")
#             user = authentication.sign_up(username, password, email)
#         user = usermanage.users[-1]
#     shopping = True
#     while shopping == True:
#         select = input("Game/Cart/Wishlist (1,2,3): ")
#         while select not in ['1','2','3']:
#             print('Please enter valid value')
#             select = input("Game/Cart/Wishlist (1,2,3): ")
#         if select == '1':
#             for order,gm in enumerate(catalog.games):
#                 print(f'{order}: {gm.title} / {gm.price} bath / {gm.details}')
#             addwish = input('Which game do you want to add to wishlist? :').split(',')
#             print(addwish)
#             for gm in addwish:
#                 game = catalog.search_games(gm)
#                 user.shopping_info.user_wishlist.add_item(game)
#             addcart = input("Which game do you want to add to cart? : ").split(',')
#             print(addcart)
#             for gm in addcart:
#                 game = catalog.search_games(gm)
#                 user.shopping_info.user_cart.add_item(game)
#             print(user.shopping_info.user_cart.items)
#             print(user.shopping_info.user_wishlist.items)


# user1_info = UserInfo('sunpolll',12345,'64011201@kmitl.ac.th',1)
# payment1 = PaymentInfo(1)
# shopping1 = ShoppingInfo(1,PurchaseHistory(1),UserWishlist(1),ShoppingCart(1))
# user1 = User(user1_info,payment1,shopping1)
# credit1 = CreditCard('card1',12345,'11/24',352)
# paypal1 = Paypal('64011201@kmitl.ac.th',12345)
# user1.payment_info.add_credit_card(credit1)
# user1.payment_info.add_paypal(paypal1)
# for game in catalog.games:
#     print(game.title)
# print(catalog.search_games('GTA V').title)
# game = catalog.search_games('GTA V')
# game1 = catalog.search_games('Minecraft')
# print(game)
# shopping1.user_cart.add_item(game)
# print(shopping1.user_cart.items)
# shopping1.user_cart.single_item = game
# print(shopping1.user_cart.single_item)
# purchase = Purchase(user1)
# paid1 = purchase.cart_purchase_CC(CreditCard('card10',12345,'11/24',352),True)
# print(paid1)
# paid2 = purchase.cart_purchase_PP(Paypal('64011201@kmitl.ac.th',352),True)
# print(paid2)
# paid3 = purchase.one_purchase_CC(CreditCard('card4',12345,'11/24',352),True)
# print(paid3)
# shopping1.user_cart.single_item = game1
# paid4 = purchase.one_purchase_PP(Paypal('64011241@kmitl.ac.th',352),True)
# print(paid4)
# for gm in user1.shopping_info.purchase_history.purchases:
#     print(gm.title, gm.price , gm.date, gm.payment_type, gm.payment_info)
# print(user1.payment_info.credit_card)
# print(user1.payment_info.paypal)