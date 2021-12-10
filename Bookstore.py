import psycopg2
userid ="test"
passwd ="1111"

def bookstore():
    try:
        conn = psycopg2.connect( host="localhost", port=5432, dbname="bookstore", user=userid, password=passwd)
        cur = conn.cursor() 
        print("Welcome to Look Inna Book")
        response = input("Are you an Owner? (y for yes): ")
        if response != 'y':
            userStore(cur,conn)
        else:
            ownerStore(cur, conn)

    except Exception as sqle:
        print("Exception : ", sqle)

def printUserMenu():
    print("\n\n\n\nMain Menu")
    print("1. View books")
    print("2. Add book to cart")
    print("3. Remove book from cart")
    print("4. View cart")
    print("5. Checkout")
    print("6. Login")
    print("7. Logout")
    print("8. Search for books")
    print("9. view Orders")
    print("10. exit\n\n\n\n")

def userStore(cur,conn):
    ans = 0
    user = ""
    cart = []
    while True:
        printUserMenu()
        ans = input("Choose action (input action number): ")
        try:
            ans = int(ans)
            if ans == 1:
                cur.execute( ("select * from book"))
                print("ISBN", "\t \t Title", " \t\t   Author Name", " \tGenre", "\t Stock", " Price")
                for book in cur: 
                    print ("{} \t {} \t {} \t {} \t {}   {} ".format(book[0], book[1], book[2],book[3], book[4], book[5]))
            elif ans == 2:
                try:
                    bookISBN = input("Write the book\'s ISBN : ")
                    cur.execute( ("select title from book where isbn = %s;"), (bookISBN,) )
                    bookAmount = (int)(input("How many copies do you want? : "))
                    for book in cur:
                        cart.append([bookISBN, book[0], bookAmount])
                    print("\n\n item added to cart")
                except Exception as sqle:
                    print( "Input isn\'t valid ", sqle)
            elif ans == 3:
                bookISBN = input("Write the book\'s ISBN : ")
                removeIndex= -1
                for i in range(len(cart)):
                    if cart[i][0] == bookISBN:
                        removeIndex = i
                if removeIndex == -1:
                    print( "Input is not valid")
                else:
                    cart.pop(removeIndex)
                    print("\n\n item removed from cart")
            elif ans == 4:
                print("CART\n")
                for i in range(len(cart)):
                    print(cart[i])
            elif ans == 5:
                if not user:
                    print ("Must be logged in to checkout")
                else:
                    try:
                        shippingAddress = input("input shipping Address: ")
                        billingInfo = input("input billing info: ")
                        for book in cart:
                            print(book[2])
                            for i in range(book[2]):
                                cur.execute("UPDATE book set  stock = stock - 1 where isbn = %s;", (book[0],))
                                cur.execute("insert into orders  (isbn, email, order_location, shipping_address, billing_info) values(%s, %s, %s, %s, %s)", (book[0],user,"Warehouse", shippingAddress, billingInfo,))
                                conn.commit()
                        print("Purchase complete ") 
                    except Exception as sqle:
                        print("Could not insert tuple. ", sqle)
                         
                        conn.rollback()
            elif ans == 6:
                email = input("email: ")
                password = input("Password: ")
                found = False
                cur.execute( ("select * from users where email = %s AND password = %s ;"), (email, password,) )
                for _ in cur:
                    found = True
                if found:
                    user = email
                    print("Logged in")
                else:
                    print("invalid LOGIN INFO")
            elif ans == 7:
                user = ""
                print("Logged out")
            elif ans == 8:
                search = '%' +  input ("Search : ") + '%' 
                cur.execute( "select * FROM book where title LIKE %s OR genre LIKE %s OR author_name LIKE %s OR isbn LIKE %s", (search,search,search,search))
                print("ISBN", "\t \t Title", " \t\t   Author Name", " \tGenre", "\t Stock", " Price")
                for book in cur: 
                    print ("{} \t {} \t {} \t {} \t {}   {} ".format(book[0], book[1], book[2],book[3], book[4], book[5]))
            elif ans == 9:
                if not user:
                    print ("Must be logged in to view orders")
                else:
                    cur.execute("select * FROM orders where email = %s", (user,))
                    print("Order #", "\tISBN" , "\t\tLocation ")
                    for order in cur:
                        print ("{} \t {} \t {} ".format(order[0], order[1], order[4]))
            elif ans == 10:
                print("Good Bye \n\n")
                break

            
        except  Exception as sqle:
            print( "Input is not valid " , sqle)
       

def printOwnerMenu():
    print("\n\n\n\nMain Menu")
    print("1. View books")
    print("2. Add book to store")
    print("3. Remove book from store")
    print("4. View publishers")
    print("5. View total sales report by author")
    print("6. View sales report by author in last month")
    print("7. View sales report by genre in last month")
    print("8. exit")
    print("\n\n\n\n")

def ownerStore(cur,conn):
    ans = 0
    while True:
        printOwnerMenu()
        ans = input("Choose action (input action number): ")
        try:
            ans = int(ans)
            if ans == 1:
                cur.execute( ("select * from book"))
                print("ISBN", "\t \t Title", " \t\t   Author Name", " \tGenre", "\t Stock", " Price")
                for book in cur: 
                    print ("{} \t {} \t {} \t {} \t {}   {} ".format(book[0], book[1], book[2],book[3], book[4], book[5]))
            elif ans == 2:
                isbn = input ("ISBN: ")
                title = input ("Title: ")
                authorName = input ("Author Name: ")
                genre = input ("genre: ")
                stock = (int)(input ("stock: "))
                price = float(input ("price: "))
                try:
                    cur.execute( "insert into book values (%s, %s, %s, %s, %s, %s);", (isbn,title,authorName,genre,stock,price,))
                    conn.commit()
                    print("book added")
                    
                except  Exception as sqle:
                    print( "Input is not valid " , sqle)
                    conn.rollback()
            elif ans == 3:
                isbn = input ("ISBN: ")
                try:
                    cur.execute( "DELETE FROM book where isbn =%s;", (isbn,))
                    conn.commit()
                    print("book removed")
                except  Exception as sqle:
                    print( "Input is not valid " , sqle)
                    conn.rollback()
            elif ans == 4:
                cur.execute( "Select * FROM publishers")
                print("publisher_id", "\t email", " \t\t  name")
                for publisher in cur:
                    print ("{} \t {} \t {} ".format(publisher[0], publisher[1], publisher[2]))
            elif ans == 5:
                cur.execute( "select author_name, count(author_name) as sale_amount from orders natural join book group by author_name;")
                print("author name", "\t units sold")
                for figure in cur:
                    print ("{} \t {} ".format(figure[0], figure[1]))
            elif ans == 6:
                cur.execute( "select author_name, count(author_name) as sale_amount from orders natural join book where transaction_date > now() - interval '1 month' group by author_name ;")
                print("author name", "\t units sold")
                for figure in cur:
                    print ("{} \t {} ".format(figure[0], figure[1]))
            elif ans == 7:
                cur.execute( "select genre, count(genre) as sale_amount from orders natural join book where transaction_date > now() - interval '1 month' group by genre ;")
                print("Genre", "\t units sold")
                for figure in cur:
                    print ("{} \t {} ".format(figure[0], figure[1]))
            elif ans == 8:
                print("Good Bye \n\n")
                break


        except  Exception as sqle:
            print( "Input is not valid " , sqle)
            

bookstore()
        