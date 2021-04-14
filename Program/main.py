###
#/***************************************************
#File Name: main.py
#Version/Date: V5(2020-06-02)
#Programmer/ID: Kishen Kumar A/L Sivalingam (1191101423), NURUL SYAQEERA BINTI ISMAIL (1191101189)
#Project Name: Fastech Online Shopping
#Teammates: HARRI GANESH A/L G CHANDRA BOSE , SHARVEENA A/P PADMARAJ  
#Course/Term: PSP0201 Mini IT Project (2019/20 T3)
#***************************************************/
###


import re
import os
def main():
    print('\n\n**********************************************************************************')
    print('*                          WELCOME TO FASTECH ONLINE SHOPPING                    *')
    print('**********************************************************************************\n')

    print('Press [1] for Category')  
    print('Press [2] for Shopping Cart')
    print('Press [3] for Customer Service')
    print('Press [4] to quit program')
    userInput = input('\nInput : ')

    if int(userInput) < 5:
        if userInput == '1':              #calling category
            category()
            
        elif userInput == '2':           #calling shopping Cart
            shoppingCart()
            
        elif userInput == '3':
            import customerServices     #calling customer services
            main()
            
        elif userInput == '4':
            import dataStoring           #calling data storing

        else:
            main()
    else:
        main()

#================================================= C A T E G O R Y  S E C T I O N ===================================================

options = ['1','2','3','4']
yes = "y".lower()
no = "n".lower()

option_1 = [yes,no]
option_2 = ['1','2','3','4']
option_3 = ['1','2','3']
option_4 = ['1','2','3','4','5','6']

getList = []

quan_price = 0

def category():  # Defining function for main category
    print("\n*******************CATEGORIES*******************\n")
    print("Choose which category do you want to proceed:\n")  # Displaying the main categories
    print("[1] Flash Sale")
    print("[2] Trending")
    print("[3] Internal Components")
    print("[4] External Components\n")
      
    print("Press '1' for 'Flash Sale' , '2' for 'Trending' , '3' for 'Internal Components' or '4' for 'External Components'")

    input_1 = input("\nInput > ") . lower()

    
    while input_1 not in options: #making sure the input given is valid based on categories' list
        print("ERROR: Invalid Input")
        input_1 = input("Input > ") . lower()
        
    if input_1 == '1':
        print("\nFlash Sale Products:")
        category_1()  # Calling the function for Flash Sale Products Category
        
    elif input_1 == '2':
       print("\nTrending Products:")
       category_2()  # Calling the function for Trending Products Category

        
    elif input_1 == '3':
         print("\nInternal Components:")
         category_3()  # Calling the function for Internal Components Category


    else:
         print("\nExternal Components:")
         category_4()  # Calling the function for External Components Category

    

#If user chooses External Components Category
def category_1():  # Defining function for Flash Sale Category
    str = 'Flash Sale !!!!'
    global quan_price
    print(str.center(140,'='))
    print('\nFlash Sale .....')
    print('Save up to 10 % - 70 %')
    print('Limited time only before it ends grab it.\n')
    print('List of catgory has special off')
    print('|*PRINTER*            |')
    print('|*KEYBOARD*           |')
    print('|*MONITOR*            |')
    print('|*MOUSE*              |')
    print('|*INTERNAL COMPONENTS*|')
    print('|*SUPPLY UNIT*        |')
    print('|*RAM*                |')
    print('|*SSD*                |')
    print('|*COOLING FAN*        |')
    print('|*MOTHERBOARD*        |\n')
    print('Choose the category according to your need.')
    print("Press '1'  for PRINTER")
    print("Press '2'  for KEYBOARD")
    print("Press '3'  for MONITOR") 
    print("Press '4'  for MOUSE")
    print("Press '5'  for INTERNAL COMPONENTS")
    print("Press '6'  for SUPPLY UNIT")
    print("Press '7'  for RAM")
    print("Press '8'  for SSD")
    print("Press '9'  for COOLING FAN") 
    print("Press '10' for MOTHERBOARD")
    preffered_cat = input('Input : ')
    
    if preffered_cat == '1':
        item = "HP Printer 2529 Deskjet Ink Advantage Home Use Printer 3 in 1"
        print('Product Description')
        print('|Product Name         : HP Printer 2529 Deskjet Ink Advantage Home Use Printer 3 in 1 |')
        print('|Price after Discount : RM 499.00  > RM 299.00   (40% off)                            |')
        print('|Warranty Period      : 3 years                                                       |')
        print('|Function             : Print, Copy, Scan                                             |')
        print('|Connectivity,standard: 1 Hi-Speed USB 2.0                                            |')
        print('|Print speed black    : ISO = Up to 7 ppm/Draft = Up to 19 ppm                        |')
        print('|Print speed color    : ISO = Up to 4 ppm/Draft = Up to 15 ppm                        |')
        print('|                                                                                     |')
        print('|Description:                                                                         |')
        print('|                                                                                     |')
        print('|1.Count on thousands of standout pages with this versatile                           |')
        print('|                                                                                     |')
        print('|2.energy-saving HP all-in-one and long-lasting and ultra-high-yield ink cartridges.  |')
        print('|                                                                                     |')
        print('|3.Easily get the job done and print at an impressively low cost per page.            |')
        print('|                                                                                     |')
        print('|4.Print thousands of pages with ultra-high-yield Original HP ink cartridges—for less |')
        print('|                                                                                     |')
        print('|5.Print borderless documents and manage print,scan,and copy jobs right at the device |')
        print('|                                                                                     |')

        quantity_1 = float(input("ENTER NUMBER OF QUANTITY: "))
        quan_price_HP = quantity_1 * 299
        quan_price += quan_price_HP
        
        print(f"\nTotal price: RM {quan_price}")
        con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'Y' for 'yes' or 'N' for 'go back')?: ").lower()
        while con_cart not in option_1:
            print("\nInvalid input...")
            con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'Y' for 'yes' or 'N' for 'go back')?: ").lower()
        if con_cart == yes:
            item = "HP Printer 2529 Deskjet Ink Advantage Home Use Printer 3 in 1"
            getList.append(item)
            print("\nThis product has been added to the shopping cart.")   

        else:
            main()

        con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
        while con_shopping not in option_1:
              print("\nInvalid input...")
              con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 
        if con_shopping == yes:
           category()                 
        else:
             print("\nThank you, See you again !!!")
             shoppingCart()
             
        
        
    elif preffered_cat == '2':
        print('Product Description')
        print('|Product Name         : Wireless 2.4G keyboard Mouse Set With Cover mini keypad Mice K-06 Computer Gaming Accessories |')
        print('|Price after Discount : RM 72.03  > RM 39   (45% off)                                                              |')
        print('|Warranty Period      : 3 months                                                                                      |')
        print('|Function             : Input device used to enter characters and functions into the computer system                  |')
        print('|Model                : K-06                                                                                          |')
        print('|Number of keys       : 101keys                                                                                       |')
        print('|                                                                                                                     |')
        print('|Description:                                                                                                         |')
        print('|                                                                                                                     |')
        print('|1. 2.4G wireless connection with two driven by one receiver, plug and play, drive automatic mounting.                |')
        print('|                                                                                                                     |')
        print('|2. Comfortable and multimedia shortcut key, good bounce with good feedback plus good hand feeling with clear font.   |')
        print('|                                                                                                                     |')
        print('|3. Ergonomic: Ergonomically designed mouse, easy to master, four adjustable DPI with low battery display lamp.       |')
        print('|                                                                                                                     |')
        print('|4. It works on desktop, laptop and TV Box, compatible with three operating systems, for WINDOWS, android and for MAC.|')
        print('|                                                                                                                     |')
        print('|5. Intelligent dormancy with touch waken, save energy. With anti-slip mat, suitable for home and office              |')
        print('|                                                                                                                     |')

        quantity_1 = float(input("ENTER NUMBER OF QUANTITY: "))
        quan_price_keyboard = quantity_1 * 39
        quan_price += quan_price_keyboard
        
        print(f"\nTotal price: RM{quan_price}")
        con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'Y' for 'yes' or 'N' for 'go back')?: ").lower()
        while con_cart not in option_1:
            print("\nInvalid input...")
            con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'Y' for 'yes' or 'N' for 'go back')?: ").lower()
        if con_cart == yes:                 #cart
            item = "Wireless 2.4G keyboard Mouse Set With Cover mini keypad Mice K-06 Computer Gaming Accessories"
            getList.append(item)
            print("\nThis product has been added to the shopping cart.") 
            
        else:
             main()

        con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
        while con_shopping not in option_1:
              print("\nInvalid input...")
              con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

        if con_shopping == yes:
           category()
                 

        else:
             print("\nThank you, See you again !!!")
             shoppingCart()
        
  
   
    elif preffered_cat == '3':
        print('Product Description')
        print('|Product Name            : OYT 24" Curved 75Hz FHD LED Monitor ultra-thin surface HD HDMI Super Slim And Sleek Design Filter bluray |')
        print('|Price after Discount    : RM 699.00 > RM 398   (43% off)                                                                        |')
        print('|Warranty Period         : 3 years                                                                                                  |')
        print('|Function                : Is an output device that displays information in pictorial form                                          |')
        print('|Connectivity Technology : HDMI                                                                                                     |')
        print('|Display Size            : 24"                                                                                                      |')
        print('|Brand                   : OYT                                                                                                      |')
        print('|Screen size             : 23.8 inches                                                                                              |')
        print('|Resolution              : 1920*1080                                                                                                |')
        print('|Screen color            : 16.7 million colors                                                                                      |')
        print('|Screen ratio            : 16:9                                                                                                     |')
        print('|Refresh frequency       : 75Hz                                                                                                     |')
        print('|Response time           : 2ms                                                                                                      |')
        print('|contrast ratio          : 3000:1                                                                                                    |')
        print('|Visual Angle            : 178 ° /178 ° full view                                                                                   |')
        print('|Interface               : HDMI VGA                                                                                                 |')

        quantity_1 = float(input("ENTER NUMBER OF QUANTITY: "))
        quan_price_oyt = quantity_1 * 398
        quan_price += quan_price_oyt
        
        print(f"\nTotal price: RM{quan_price}")
        con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'Y' for 'yes' or 'N' for 'go back')?: ").lower()
        while con_cart not in option_1:
            print("\nInvalid input...")
            con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'Y' for 'yes' or 'N' for 'go back')?: ").lower()
        if con_cart == yes:
            item = 'OYT 24" Curved 75Hz FHD LED Monitor ultra-thin surface HD HDMI Super Slim And Sleek Design Filter bluray'
            getList.append(item)
            print("\nThis product has been added to the shopping cart.")

        else:
             main()

        con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
        while con_shopping not in option_1:
              print("\nInvalid input...")
              con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")

        if con_shopping == yes:
           category()
                 
        else:
             print("\nThank you, See you again !!!\n")
             shoppingCart()

    
    elif preffered_cat == '4':
        print('Product Description')
        print('|Product Name            : Logitech G103 Prodigy Gaming Mouse 910-005481                  |')
        print('|Price after Discount    : RM 129.00 > RM 65.00   (50% off)                               |')
        print('|Warranty Period         : 1 year                                                         |')
        print('|Function                : pointing device used to position a cursor on a computer screen |')
        print('|System Requirements     : Windows® 10, Windows 8.1, Windows 8, Windows 7                 |')
        print('|Durability              : Buttons (Left / Right) = 10 million clicks                     |')
        print('|USB port                : Internet connection for optional software download             |')
        print('|                                                                                         |')
        print('|Physical specifications :                                                                |')
        print('|Height       = 116.6 mm                                                                  |')
        print('|Width        = 62.15 mm                                                                  |')
        print('|Depth        = 38.2 mm                                                                   |')
        print('|Weight       = 85 g mouse only                                                           |')
        print('|Cable Length = 2 m                                                                       |')
        print('|                                                                                         |')

        quantity_1 = float(input("ENTER NUMBER OF QUANTITY: "))
        quan_price_g103 = quantity_1 * 65
        quan_price += quan_price_g103
        
        print(f"\nTotal price: RM{quan_price}")
        con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'Y' for 'yes' or 'N' for 'go back')?: ").lower()
        while con_cart not in option_1:
            print("\nInvalid input...")
            con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'Y' for 'yes' or 'N' for 'go back')?: ").lower()
        if con_cart == yes:
            item = 'Logitech G103 Prodigy Gaming Mouse 910-005481'
            getList.append(item)
            print("\nThis product has been added to the shopping cart.") 
        else:
             main()

        con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
        while con_shopping not in option_1:
              print("\nInvalid input...")
              con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 
        if con_shopping == yes:
           category()
                 

        else:
             print("\nThank you, See you again !!!\n")
             shoppingCart()
        
    elif preffered_cat == '5':
        print('Product Description')
        print('|Product Name         : Intel CORE i5-9400F Processor (9M Cache, up to 4.10 GHz, LGA 1151, W/O GPU)                       |')
        print('|Price after Discount : RM 749.00 > RM 669.00   (11% off)                                                                  |')
        print('|Warranty Period      : 3 years                                                                                            |')
        print('|Function             : acts as the computers brain, running programs and sending and receiving signals to attached devices|')
        print('|Model                : X80684I59400F                                                                                      |')
        print('|Operating Frequency  : 2.9 GHz                                                                                            |')
        print('|Max Turbo Frequency  : 4.1 GHz                                                                                            |')
        print('|64-Bit Support       : Yes                                                                                                |')
        print('|Max Number of PCI    : 16                                                                                                 |')
        print('|Memory Channel       : 2                                                                                                  |')
        print('|Cooling Device       : Heatsink and fan included                                                                          |')
        print('|                                                                                                                          |')

        quantity_1 = float(input("ENTER NUMBER OF QUANTITY: "))
        quan_price_core5 = quantity_1 * 669.00
        quan_price += quan_price_core5
        
        print(f"\nTotal price: RM{quan_price}")
        con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'Y' for 'yes' or 'N' for 'go back')?: ").lower()
        while con_cart not in option_1:
            print("\nInvalid input...")
            con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'Y' for 'yes' or 'N' for 'go back')?: ").lower()
        if con_cart == yes:
            item = 'Intel CORE i5-9400F Processor (9M Cache, up to 4.10 GHz, LGA 1151, W/O GPU)'
            getList.append(item)
            print("\nThis product has been added to the shopping cart.") 
        else:
             main()

        con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
        while con_shopping not in option_1:
              print("\nInvalid input...")
              con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

        if con_shopping == yes:
           category()
                 

        else:
             print("\nThank you, See you again !!!\n")
             shoppingCart()
        
    elif preffered_cat == '6':
        print('Product Description')
        print('|Product Name         : Armaggeddon Voltron Gold 475 RGB Power Supply Unit with RGB Silent Fan                             |')
        print('|Price after Discount : RM 179.00 > RM 129.00   (28% off)                                                                  |')
        print('|Warranty Period      : 1 year                                                                                             |')
        print('|Function             : converts mains AC to low-voltage regulated DC power for the internal components of a computer.     |')
        print('|                                                                                                                          |')
        print('|Specifications:                                                                                                           |')
        print('|- Optimum Power Output 475W                                                                                               |')
        print('|- Ultra high efficiency                                                                                                   |')
        print('|- Build-In 120mm RGB silent fan                                                                                           |')
        print('|- Pure power rated 478 watts                                                                                              |')
        print('|- Sata x 4                                                                                                                |')
        print('|- 20 + 4 PIN                                                                                                              |')
        print('|- MotherBoard x 1                                                                                                         |')
        print('|- 4 + 4 PIN                                                                                                               |')
        print('|- CPU + 12V x 1                                                                                                           |')
        print('|- HDD 4PIN x 3                                                                                                            |')
        print('|- 6 + 2 PIN : PCI-E x 1                                                                                                   |')
        print('|- ATX 24 PIN (20 + 4)                                                                                                     |')
        print('|- AC Input : 170-240VAC 3A 50/60HZ                                                                                        |')
        print('|                                                                                                                          |')

        quantity_1 = float(input("ENTER NUMBER OF QUANTITY: "))
        quan_price_supp = quantity_1 * 129.00
        quan_price += quan_price_supp
        
        print(f"\nTotal price: RM{quan_price}")
        con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'Y' for 'yes' or 'N' for 'go back')?: ").lower()
        while con_cart not in option_1:
            print("\nInvalid input...")
            con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'Y' for 'yes' or 'N' for 'go back')?: ").lower()
        if con_cart == yes:
            item = 'Armaggeddon Voltron Gold 475 RGB Power Supply Unit with RGB Silent Fan'
            getList.append(item)
            print("\nThis product has been added to the shopping cart.")   
        else:
             main()

        con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
        while con_shopping not in option_1:
              print("\nInvalid input...")
              con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

        if con_shopping == yes:
           category()
                 

        else:
             print("\nThank you, See you again !!!\n")
             shoppingCart()


    elif preffered_cat == '7':
        print('Product Description')
        print('|Product Name         : Kingston HyperX FURY 8GB DDR4 2400Mhz/2666Mhz 288Pin PC4 DIMM RAM Desktop Memory |')
        print('|Price after Discount : RM 400.00 > RM 159   (60% off)                                                   |')
        print('|Warranty Period      : Lifetime Warranty                                                                |')
        print('|Function             : Stores data for short-term use                                                   |')
        print('|Type                 : 288-Pin DDR4                                                                     |')
        print('|Brand                : HyperX                                                                           |')
        print('|Capacity             : 8GB (1x8GB)                                                                      |')
        print('|Speed                : 8GB PC4-19200 DDR4 2400 MHz                                                      |')
        print('|Voltage              : 1.2V                                                                             |')
        print('|Heatsink             : Black                                                                            |')
        print('|                                                                                                        |')

        quantity_1 = float(input("ENTER NUMBER OF QUANTITY: "))
        quan_price_hyperx = quantity_1 * 159
        quan_price += quan_price_hyperx
        
        print(f"\nTotal price: RM{quan_price}")
        con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'Y' for 'yes' or 'N' for 'go back')?: ").lower()
        while con_cart not in option_1:
            print("\nInvalid input...")
            con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'Y' for 'yes' or 'N' for 'go back')?: ").lower()
        if con_cart == yes:
            item = 'Kingston HyperX FURY 8GB DDR4 2400Mhz/2666Mhz 288Pin PC4 DIMM RAM Desktop Memory'
            getList.append(item)
            print("\nThis product has been added to the shopping cart.")  
        else:
             main()

        con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
        while con_shopping not in option_1:
              print("\nInvalid input...")
              con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

        if con_shopping == yes:
           category()
                 

        else:
             print("\nThank you, See you again !!!\n")
             shoppingCart()

        
        
    elif preffered_cat == '8':
        print('Product Description')
        print('|Product Name         : Seagate Fast External SSD 2TB/1TB/500GB/250GB Fast SSD USB-C Portable Solid State Drive Portable SSD External Drive |')
        print('|Price after Discount : RM 599.00 > RM 255.00   (57% off)                                                                                   |')
        print('|Warranty Period      : Lifetime Warranty                                                                                                   |')
        print('|Function             : used to store and retrieve data                                                                                     |')
        print('|                                                                                                                                           |')
        print('|Specifications       :                                                                                                                     |')
        print('|- Up to 2 TB of storage                                                                                                                    |')
        print('|- Sleek, stylish and ultra-modern design                                                                                                   |')
        print('|- Lightweight and shock resistant — take it everywhere                                                                                     |')
        print('|- Future-proof USB-C technology                                                                                                            |')
        print('|- Transfer speeds up to 540 MB/s                                                                                                           |')
        print('|- Folder syncing software helps keep your important files up-to-date                                                                       |')
        print('|- Fast SSD will automatically keep up with the latest changes to your files                                                                |')
        print('|- The meticulously crafted Fast SSD is sleek, lightweight, and shock resistant                                                             |')
        print('|                                                                                                                                           |')

        quantity_1 = float(input("ENTER NUMBER OF QUANTITY: "))
        quan_price_seagate = quantity_1 * 255.00
        quan_price += quan_price_seagate
        
        print(f"\nTotal price: RM{quan_price}")
        con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'Y' for 'yes' or 'N' for 'go back')?: ").lower()
        while con_cart not in option_1:
            print("\nInvalid input...")
            con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'Y' for 'yes' or 'N' for 'go back')?: ").lower()
        if con_cart == yes:
            item = 'Seagate Fast External SSD 2TB/1TB/500GB/250GB Fast SSD USB-C Portable Solid State Drive Portable SSD External Drive'
            getList.append(item)
            print("\nThis product has been added to the shopping cart.")   
        else:
             main()

        con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
        while con_shopping not in option_1:
              print("Invalid input...")
              con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

        if con_shopping == yes:
           category()
                 

        else:
             print("\nThank you, See you again !!!\n")
             shoppingCart()

        
    elif preffered_cat == '9':
        print('Product Description')
        print('|Product Name         : Cooler Master MasterLiquid ML120R/ML240R/ML360R RGB All-in-One CPU Liquid Cooler                             |')
        print('|Price after Discount : RM 699.00 > RM 415.00   (41% off)                                                                            |')
        print('|Warranty Period      : 2 years                                                                                                      |')
        print('|Function             : flow cooler air over hot areas in a computer and then exhaust it outside the computer                        |')
        print('|Fan Speed            : 600 – 2000 RPM                                                                                               |')               
        print('|Compatibility        : Intel® LGA 2066/2011-v3/2011 /1151/1150/1155/1156/1366/775socketAMD®AM4/AM3+/AM/AM2+/AM2/FM2+/FM2/FM1 socket |')
        print('|Material             : Aluminum                                                                                                     |')
        print('|Dimensions           : 277 x 119.6 x 27 mm (10.9 x 4.71 x 1.06")                                                                    |')
        print('|Dimensions           : 120 x 120 x 25 mm (4.7 x 4.7 x 1")                                                                           |')
        print('|Quantity             : 2 PCS                                                                                                        |')
        print('|Speed                : 650 ~ 2000 RPM (PWM) ± 10%                                                                                   |')
        print('|Air Flow             : 66.7 CFM (Max)                                                                                               |')
        print('|Air Pressure         : 2.34 mmH2O (Max)                                                                                             |')
        print('|MTTF                 : 160,000 hours                                                                                                |')
        print('|Noise Level          : 6 ~ 30 dBA                                                                                                   |')
        print('|Connector            : 4-Pin (PWM)                                                                                                  |')
        print('|Rated Voltage        : 12 VDC                                                                                                       |')
        print('|Dimensions           : 83.6 x 71.8 x 52.7 mm (3.3 x 2.8 x 2.1")                                                                     |')
        print('|MTTF                 : 70,000 hours                                                                                                 |')
        print('|Noise Level          : < 15 dBA                                                                                                     |')
        print('|Connector            : 3-Pin                                                                                                        |')
        print('|Rated Voltage        : 12 VDC                                                                                                       |')
        print('|                                                                                                                                    |')
        quantity_1 = float(input("ENTER NUMBER OF QUANTITY: "))
        quan_price_ml120 = quantity_1 * 415.00
        quan_price += quan_price_ml120
        
        print(f"\nTotal price: RM{quan_price}")
        con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'Y' for 'yes' or 'N' for 'go back')?: ").lower()
        while con_cart not in option_1:
            print("\nInvalid input...")
            con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'Y' for 'yes' or 'N' for 'go back')?: ").lower()
        if con_cart == yes:
            item = 'Cooler Master MasterLiquid ML120R/ML240R/ML360R RGB All-in-One CPU Liquid Cooler'
            getList.append(item)
            print("\nThis product has been added to the shopping cart.")   
        else:
             main()

        con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
        while con_shopping not in option_1:
              print("\nInvalid input...")
              con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

        if con_shopping == yes:
           category()
                 

        else:
             print("\nThank you, See you again !!!\n")
             shoppingCart()

        
        
    elif preffered_cat == '10':
        print('Product Description')
        print('|Product Name         : GIGABYTE B450 AORUS Elite GAMING MOTHERBOARD (AM4)                                                                                     |')
        print('|Price after Discount : RM 495.00 > RM 435.00   (12% off)                                                                                                      |')
        print('|Warranty Period      : 2 years                                                                                                                                |')
        print('|Function             : links all the individual parts of a computer together and also, allows the CPU to access and control these separate parts              |')
        print('|                                                                                                                                                              |')
        print('|Specifications       :                                                                                                                                        |') 
        print('|-AMD B450 AORUS ELITE Motherboard with Hybrid Digital PWM, Dual M.2 with Dual Thermal Guards, Audio ALC1220-VB, Intel® GbE LAN with cFosSpeed, CEC 2019 ready |')  
        print('|-Supports AMD 2nd Generation Ryzen™/ Ryzen™ with Radeon™ Vega Graphics/ 1st Generation Ryzen™ Processors                                                      |')  
        print('|-Dual Channel Non-ECC Unbuffered DDR4, 4 DIMMs                                                                                                                |')
        print('|-HDMI, DVI-D Ports for Multiple Display                                                                                                                       |')  
        print('|-Integrated I/O Shield of Ultra Durable™ Design                                                                                                               |')  
        print('|-Dual Ultra-Fast NVMe PCIe Gen3 M.2 (x4, x2) with Dual Thermal Guards                                                                                         |')  
        print('|-ALC1220-VB Enhanced 114dB(Rear) / 110dB(Front) SNR in Microphone with WIMA Audio Capacitors                                                                  |')  
        print('|-RGB FUSION with Multi-Zone LED Light Show Design, Supports Digital LED & RGB LED Strips                                                                      |')  
        print('|-Intel® GbE LAN with cFosSpeed Internet Accelerator Software                                                                                                  |')  
        print('|-Smart Fan 5 Features 6 Temperature Sensors and 5 Hybrid Fan Headers with FAN STOP                                                                            |')  
        print('|-APP Center Including EasyTune™ and Cloud Station™ Utilities                                                                                                  |')  
        print('|-CEC 2019 Ready, Save Power with a Single Click                                                                                                               |')  
        print('|                                                                                                                                                              |')
        print('| CPU :                                                                                                                                                        |')  
        print('|-AM4 Socket:                                                                                                                                                  |')  
        print('|-AMD Ryzen™ 2nd Generation processors                                                                                                                         |')  
        print('|-AMD Ryzen™ with Radeon™ Vega Graphics processors                                                                                                             |')  
        print('|-AMD Ryzen™ 1st Generation processors                                                                                                                         |')  
        print('|-AMD B450                                                                                                                                                     |')
        print('|                                                                                                                                                              |')
        print('| Memory:                                                                                                                                                      |')  
        print('| 4 x DDR4 DIMM sockets supporting up to 64 GB of system memory                                                                                                |')  
        print('|-Dual channel memory architecture                                                                                                                             |')  
        print('|-Support for DDR4 3200(O.C.)/2933/2667/2400/2133 MHz memory modules                                                                                           |')  
        print('|-Support for ECC Un-buffered DIMM 1Rx8/2Rx8 memory modules (operate in non-ECC mode)                                                                          |')  
        print('|-Support for non-ECC Un-buffered DIMM 1Rx8/2Rx8/1Rx16 memory modules                                                                                          |')  
        print('|-Support for Extreme Memory Profile (XMP) memory modules                                                                                                      |')   
        print('|                                                                                                                                                              |')
        print('| Integrated Graphics Processor:                                                                                                                               |')  
        print('| 1 x DVI-D port, supporting a maximum resolution of 1920x1200@60 Hz                                                                                           |')  
        print('| * The DVI-D port does not support D-Sub connection by adapter.                                                                                               |')  
        print('| 1 x HDMI port, supporting a maximum resolution of 4096x2160@60 Hz                                                                                            |')  
        print('| * Support for HDMI 2.0 version and HDCP 2.2.                                                                                                                 |')  
        print('| * Actual support may vary by CPU.                                                                                                                            |')  
        print('| Maximum shared memory of 16 GB                                                                                                                               |')  
        print('|                                                                                                                                                              |')
        print('| Operating System:                                                                                                                                            |')  
        print('| Support for Windows 10 64-bit                                                                                                                                |')  
        print('| Support for Windows 7 64-bit                                                                                                                                 |')
        print('| * To support Windows 7 64-bit, you must install an AMD Pinnacle Ridge & Summit Ridge CPU.                                                                    |')  
        print('| * Please download the "Windows USB Installation Tool" from GIGABYTEs website and install it before installing Windows 7.                                     |')
        print('|                                                                                                                                                              |')

        quantity_1 = float(input("ENTER NUMBER OF QUANTITY: "))
        quan_price_aorus = quantity_1 * 435.00
        quan_price += quan_price_aorus
        
        print(f"\nTotal price: RM{quan_price}")
        con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'Y' for 'yes' or 'N' for 'go back')?: ").lower()
        while con_cart not in option_1:
            print("\nInvalid input...")
            con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'Y' for 'yes' or 'N' for 'go back')?: ").lower()
        if con_cart == yes:
            item = 'GIGABYTE B450 AORUS Elite GAMING MOTHERBOARD (AM4)'
            getList.append(item)
            print("\nThis product has been added to the shopping cart.")  
        else:
             main()

        con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
        while con_shopping not in option_1:
              print("\nInvalid input...")
              con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

        if con_shopping == yes:
           category()
                 

        else:
             print("\nThank you, See you again !!!\n")
             shoppinCart()
        
        
        
    else:
        print('Invalid input.Enter a valid Number from the list')
        return category_1()

    

def category_2():    # Defining Trending Products Category
    global quan_price
    print("Choose which sub-category do you want to proceed:\n")
    print("[1] PRINTERS")
    print("[2] MOUSE")
    print("[3] SSD")
    print("[4] PROCESSOR")
    print("Press '1' for 'PRINTERS' , '2' for 'MOUSE' , '3' for 'SSD' or '4' for 'PROCESSOR")
    sub_input = (input("INPUT > "))

    while sub_input not in (option_2):
        print("Invalid input.\n")
        print("Choose which sub-category do you want to proceed:\n")
        print("[1] PRINTERS")
        print("[2] MOUSE")
        print("[3] SSD")
        print("[4] PROCESSOR")
        print("Press '1' for 'PRINTERS' , '2' for 'MOUSE' , '3' for 'SSD' or '4' for 'PROCESSOR")
        sub_input = (input("INPUT > "))

    if sub_input == '1':
         print("\nPRINTERS :-\n")
         print("[1] CANON SELPHY CP1300")
         print("[2] HP SPROKET 200")
         print("[3] EPSON LQ-590 II")
         print("Press '1', '2', or '3' to know more about the specified printer that you chose through the index.\n")
         prin_input = (input("INPUT > "))
         print()

         while prin_input not in (option_3):
             print("Invalid input.")
             print("\nPRINTERS :-\n")
             print("[1] CANON SELPHY CP1300 ")
             print("[2] HP SPROKET 200")
             print("[3] EPSON LQ-590 II")
             print("Press '1', '2', or '3' to know more about the specified printer that you chose through the index.\n")
             prin_input = (input("INPUT > "))
             print()
             


         if prin_input == '1':
             print("NAME: Canon imageCLASS LBP6030 (Print Only) Mono Laser Printer - compatible with toner cartridge 325\n")
             print("PRODUCT DETAILS:-\n")
             print("- 3.2' tilt-up LCD screen")
             print("- Wireless printing support (including AirPrint and Mopria Print Service)")
             print("- Optional battery pack (print up to 54 prints on a single charge")
             print("- 3 stylish colors (Black, White and Pink)")
             print("WARRANTY PERIOD: 12 months\n")
             print("RATINGS: 4.2/5\n")
             print("PRICE: RM540.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_canonlbp = quantity_1 * 540
             quan_price += quan_price_canonlbp
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = 'Canon imageCLASS LBP6030 (Print Only) Mono Laser Printer - compatible with toner cartridge 325'
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")

             else:
                 main()

             con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

             if con_shopping == yes:
                 category()
                 

             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()

         elif prin_input == '2':
            print("NAME: HP SPROCKET 200 ")
            print("PRODUCT DETAILS:-\n")
            print("- INSTANTLY TURN YOUR INSTAS AND SNAPS INTO 2 X 3 INCH (5 X 7.6 CM) STICKABLE PHOTOS.")
            print("- EASILY CONNECT FRIENDS AND FAMILY SO EVERYONE CAN PRINT AND VIEW A SHARED ALBUM.")
            print("- EDIT AND PRINT PHOTOS FROM YOUR CAMERA ROLL AND SOCIAL MEDIA")
            print("- ADD FILTERS, STICKERS, AND MORE")
            print("WARRANTY PERIOD: 12 months\n")
            print("RATINGS: 4.5/5\n")
            print("PRICE: RM439.00\n")
            
            quantity_1 = float(input("QUANTITY(in digits): "))
            quan_price_sprocket = quantity_1 * 439
            quan_price += quan_price_sprocket
            
            print(f"\nTotal price: RM{quan_price}")
            con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
            while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

            if con_cart == yes:
                item = 'HP SPROCKET 200'
                getList.append(item)
                print("\nThis product has been added to the shopping cart.") 

            else:
                 main()

            con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
            while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

            if con_shopping == yes:
                 category()

            else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()


         elif prin_input == '3':
            print("NAME: EPSON LQ-590 II  ")
            print("PRODUCT DETAILS:-\n")
            print("- 24-pins Impact Printer")
            print("- Print speeds of up to 487 cps (10 cpi)")
            print("- 128 kb memory buffer")
            print("- Built-in network connectivity\n")
            print("WARRANTY PERIOD: 3 Years\n")
            print("RATINGS: 4.2/5\n")
            print("PRICE: RM1600.00\n")
            
            quantity_1 = float(input("QUANTITY(in digits): "))
            quan_price_lq = quantity_1 * 1600
            quan_price += quan_price_lq
            
            print(f"\nTotal price: RM{quan_price}")
            con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
            while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

            if con_cart == yes:
                item = 'EPSON LQ-590 II'
                getList.append(item)
                print("\nThis product has been added to the shopping cart.")   

            else:
                 main()

            con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
            while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

            if con_shopping == yes:
                 category()
                 

            else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()


    elif sub_input == '2':
        print("\nMOUSE :-\n")
        print("[1]  HP X3000 WIRELESS")
        print("[2]  AVF GAMING FREAK RGB")
        print("[3]  LOGITECH M590 B/T\n")
        print("Press '1', '2', or '3' to know more about the specified keyboard that you chose through the index.\n")
        key_input = (input("INPUT > "))
        print()

        while key_input not in (option_3):
            print("Invalid input.")
            print("\nMOUSE :-\n")
            print("[1] HP X3000 WIRELESS ")
            print("[2] AVF GAMING FREAK RGB")
            print("[3] LOGITECH M590 B/T\n")
            print("Press '1', '2', or '3' to know more about the specified keyboard that you chose through the index.\n")
            key_input = (input("INPUT > "))
            print()
            
             

        if key_input == '1':
             print("NAME: HP X3000 WIRELESS\n")
             print("PRODUCT DETAILS:-\n")
             print("- Premium HP standards")
             print("- Stylish, attractive design")
             print("- No more pulling. No more tugging.")
             print("- Scroll wheel\n")
             print("WARRANTY PERIOD: 1 Years\n")
             print("RATINGS: 4.8/5\n")
             print("PRICE: RM70.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_hp = quantity_1 * 70
             quan_price += quan_price_hp
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                item = 'HP X3000 WIRELESS'
                getList.append(item)
                print("\nThis product has been added to the shopping cart.")   

             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

             if con_shopping == yes:
                 category()
                 

             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()
        
         
        elif key_input == '2':
             print("NAME: AVF GAMING FREAK RGB\n")
             print("PRODUCT DETAILS:-\n")
             print("- ERGONOMICALLY DESIGN.")
             print("- PERFECT FIT HAND-SHAPED CURVE.")
             print("- NON-SLIP SURFACE TREATMENT.")
             print("- LED with 7 colours\n")
             print("WARRANTY PERIOD: 12 Months\n")
             print("RATINGS: 4.8/5\n")
             print("PRICE: RM100.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_avf = quantity_1 * 100
             quan_price += quan_price_avf
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = 'AVF GAMING FREAK RGB'
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")   

             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

             if con_shopping == yes:
                 category()
                 

             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()


        
        elif key_input == '3':
             print("NAME: LOGITECH M590 B/T\n")
             print("PRODUCT DETAILS:-\n")
             print("- Connection type: Bluetooth Smart and 2.4GHz wireless connection")
             print("- Standard and Special buttons: Tilt wheel with middle click, Easy Switch")
             print("- Sensor resolution: 1000 dpi")
             print("- Battery life: 2 years*\n")
             print("WARRANTY PERIOD: 12 Months\n")
             print("RATINGS: 4.5/5\n")
             print("PRICE: RM129.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_m590 = quantity_1 * 129
             quan_price += quan_price_m590
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("vAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = 'LOGITECH M590 B/T'
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")   

             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

             if con_shopping == yes:
                 category()
                 

             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()


        
    elif sub_input == '3':
        print("\nSSD :-\n")
        print("[1] A400 SATA SSD in 2.5' and M.2 Form Factors")
        print("[2] SAMSUNG 970 PRO NVMe M.2 SSD 1TB")
        print("[3] APACER AS340 PANTHER SATA III SSD\n")
        print("Press '1', '2', or '3' to know more about the specified monitor that you chose through the index.\n")
        mon_input = (input("INPUT > "))
        print()

        while mon_input not in (option_3):
            print("Invalid input.")
            print("\nSSD :-\n")
            print("[1] A400 SATA SSD in 2.5' and M.2 Form Factors")
            print("[2] SAMSUNG 970 PRO NVMe M.2 SSD 1TB")
            print("[3] APACER AS340 PANTHER SATA III SSD\n")
            print("Press '1', '2', or '3' to know more about the specified monitor that you chose through the index.\n")
            mon_input = (input("INPUT > "))
            print()
            
             

        if mon_input == '1':
             print("NAME: A400 SATA SSD in 2.5' and M.2 Form Factors\n")
             print("PRODUCT DETAILS:-\n")
             print("- SATA Rev. 3.0 (6Gb/s) – with backwards compatibility to SATA Rev. 2.0 (3Gb/s)")
             print("- CAPACITY: 120GB, 240GB, 480GB, 960GB, 1.92TB")
             print("- Power Consumption:0.195W Idle / 0.279W Avg / 0.642W (MAX) Read / 1.535W (MAX) Write")
             print("-Total Bytes Written (TBW)4	120GB: 40TB\n")
             print("WARRANTY PERIOD: 3 Years\n")
             print("RATINGS: 4.8/5\n")
             print("PRICE: RM120.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_sata = quantity_1 * 120
             quan_price += quan_price_sata
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "A400 SATA SSD in 2.5' and M.2 Form Factors"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")  

             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 
             if con_shopping == yes:
                 category()

             else:
                 print("\nThank you, See you again !!!/n")
                 shoppingCart()


        elif mon_input == '2':
             print("NAME: SAMSUNG 970 PRO NVMe M.2 SSD 1TB\n")
             print("PRODUCT DETAILS:-\n")
             print("- NVMe SSD powered by Samsung VNAND technology")
             print("- Up to 3,500MB/s sequential read and 2,700MB/s write sppeds")
             print("- Up to 1,200 TBW")
             print("WARRANTY PERIOD:  5 Years\n")
             print("RATINGS: 4.9/5\n")
             print("PRICE: RM765.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_nvm = quantity_1 * 765
             quan_price += quan_price_nvm
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "SAMSUNG 970 PRO NVMe M.2 SSD 1TB"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")    

             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

             if con_shopping == yes:
                 category()
                 

             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()

    
        elif mon_input == '3':
             print("NAME: APACER AS340 PANTHER SATA III SSD\n")
             print("PRODUCT DETAILS:-\n")
             print("- Advance Wear leveling & ECC Functions ")
             print("- Support Window 7 Trim Command")
             print("- Support NCQ Command")
             print("- Interface: SATA III 6Gb/s\n")
             print("WARRANTY PERIOD: 3 Years\n")
             print("RATINGS: 4.8/5\n")
             print("PRICE: RM120.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_apacer = quantity_1 * 120
             quan_price += quan_price_apacer
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "APACER AS340 PANTHER SATA III SSD"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")   

             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

             if con_shopping == yes:
                 category()
                 

             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()


    elif sub_input == '4':
         print("\nPROCESSOR :-\n")
         print("[1] AMD Ryzen™ 9 3900X")
         print("[2] Intel® Core™ i7-10700T Processor")
         print("[3] Intel® Xeon® D-1602 Processor\n")
         print("Press '1', '2', or '3' to know more about the specified mouse that you chose through the index.\n")
         pro_input = (input("INPUT > "))
         print()

         while pro_input not in (option_3):
             print("Invalid input.")
             print("\nPROCESSOR :-\n")
             print("[1] AMD Ryzen™ 9 3900X")
             print("[2] Intel® Core™ i7-10700T Processor")
             print("[3] Intel® Xeon® D-1602 Processor\n")
             print("Press '1', '2', or '3' to know more about the specified mouse that you chose through the index.\n")
             pro_input = (input("INPUT > "))
             print()

         if pro_input == '1':
             print("NAME:AMD Ryzen 9 3900X\n")
             print("PRODUCT DETAILS:-\n")
             print("- Total L3 Cache 64MB")
             print("- Thermal Solution (MPK) Wraith PRISM")
             print("- PCI Express® Version PCIe 4.0 x16")
             print("- Thermal Solution (PIB) Wraith Prism with RGB LED\n")
             print("WARRANTY PERIOD: 1 Year\n")
             print("RATINGS: 4.4/5\n")
             print("PRICE: RM2100.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_amd = quantity_1 * 2100
             quan_price += quan_price_amd
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "AMD Ryzen 9 3900X"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")   

             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

             if con_shopping == yes:
                 category()
                 

             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()


         elif pro_input == '2':
             print("NAME: Intel Core i7-10700T Processor\n")
             print("PRODUCT DETAILS:-\n")
             print("- Processor Base Frequency 2.00 GHz")
             print("- Intel® Turbo Boost Max Technology 3.0 Frequency ‡ 4.50 GHz")
             print("- Configurable TDP-down Frequency 1.30 GHz")
             print("- Bus Speed 8 GT/s\n")
             print("WARRANTY PERIOD: 1 Year\n")
             print("RATINGS: 4.9/5\n")
             print("PRICE: RM960.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_intel7 = quantity_1 * 960.00
             quan_price += quan_price_intel7
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "Intel Core i7-10700T Processor"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")  

             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

             if con_shopping == yes:
                 category()
                 

             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()



         elif pro_input == '3':
             print("NAME: Intel Xeon D-1602 Processor\n")
             print("PRODUCT DETAILS:-\n")
             print("- Max Memory Size (dependent on memory type) 128 GB")
             print("- Maximum Memory Speed2133 MHz")
             print("- Memory Types DDR4, DDR3\n")
             print("WARRANTY PERIOD: 1 Year\n")
             print("RATINGS: 4.6/5\n")
             print("PRICE: RM2000.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_xeon = quantity_1 * 2000.00
             quan_price += quan_price_xeon
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "Intel Xeon D-1602 Processor"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.") 

             else:
                 main()


             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

             if con_shopping == yes:
                 category()
                 

             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()


def category_3():   # Defining function for Internal Components Category
    global quan_price
    print("Choose which sub-category do you want to proceed:\n")
    print("[1] PROCESSORS")
    print("[2] POWER SUPPLY UNIT")
    print("[3] RAM")
    print("[4] SSD CARD")
    print("[5] COOLING FAN")
    print("[6] MOTHERBOARD\n")
    print("Press '1' for 'PROCESSORS' , '2' for 'POWER SUPPLY UNIT' , '3' for 'RAM' or '4' for 'SSD CARD' ")
    print("'5' for 'COOLING FAN' , '6' for 'MOTHERBOARD'")
    sub_input = (input("INPUT > "))


    while sub_input not in (option_4):
        print("Invalid input.\n")
        print("Choose which sub-category do you want to proceed:\n")
        print("[1] PROCESSORS")
        print("[2] POWER SUPPLY UNIT")
        print("[3] RAM")
        print("[4] SSD CARD")
        print("[5] COOLING FAN")
        print("[6] MOTHERBOARD\n")
        print("Press '1' for 'PROCESSORS' , '2' for 'POWER SUPPLY UNIT' , '3' for 'RAM' or '4' for 'SSD CARD' ")
        print("'5' for 'COOLING FAN' , '6' for 'MOTHERBOARD'")
        sub_input = (input("INPUT > "))

    if sub_input == '1':
         print("\nPROCESSORS :-\n")
         print("[1] Intel i5 3470 3.20 Ghz")
         print("[2] Intel Core i7 8700K")
         print("[3] Intel Core i5 9600\n")
         print("Press '1', '2', or '3' to know more about the specified processors that you chose through the index.\n")
         pros_input = (input("INPUT > "))
         print()

         while pros_input not in (option_3):
             print("Invalid input.")
             print("\nPROCESSORS :-\n")
             print("[1] Intel i5 3470 3.20 Ghz")
             print("[2] Intel Core i7 8700K")
             print("[3] Intel Core i5 9600\n")
             print("Press '1', '2', or '3' to know more about the specified processors that you chose through the index.\n")
             pros_input = (input("INPUT > "))
             print()
             

         if pros_input == '1':
             print("NAME: Intel i5 3470 3.20 Ghz\n") 
             print("PRODUCT DETAILS:-\n")
             print("- Quad Core")
             print("- i5-3470 up to 3.6 Ghz")
             print("WARRANTY PERIOD: 1 Month\n")
             print("RATINGS: 4.8/5\n")
             print("PRICE: RM 229.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_intel5 = quantity_1 * 229
             quan_price += quan_price_intel5
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "Intel i5 3470 3.20 Ghz"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.") 

             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

             if con_shopping == yes:
                 category()
                 

             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()


         elif pros_input == '2':
            print("NAME: Intel Core i7 8700K ")
            print("PRODUCT DETAILS:-\n")
            print("- 6 Cores, 12 Threads")
            print("- CPU speed 3-4 Ghz")
            print("- Processor number i7-8700K")
            print("- Bus speed 8GT/sDMI3\n")
            print("WARRANTY PERIOD: 3 Years\n")
            print("RATINGS: 4.3/5\n")
            print("PRICE: RM 1559.00\n")
            
            quantity_1 = float(input("QUANTITY(in digits): "))
            quan_price_core7 = quantity_1 * 1559
            quan_price += quan_price_core7
            
            print(f"\nTotal price: RM{quan_price}")
            con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
            while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

            if con_cart == yes:
                item = "Intel Core i7 8700K"
                getList.append(item)
                print("\nThis product has been added to the shopping cart.")   
                 
            else:
                 main()

            con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
            while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

            if con_shopping == yes:
                 category()
                 

            else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()

        

         elif pros_input == '3':
            print("NAME: Intel Core i5 9600  ")
            print("PRODUCT DETAILS:-\n")
            print("- Brand OEM")
            print("- 6 Cores")
            print("- Interface : INTEL1151(the nine generation)")
            print("WARRANTY PERIOD: 1 Year\n")
            print("RATINGS: 4.5/5\n")
            print("PRICE: RM 959.00\n")
            
            quantity_1 = float(input("QUANTITY(in digits): "))
            quan_price_9600 = quantity_1 * 959
            quan_price += quan_price_9600
            
            print(f"\nTotal price: RM{quan_price}")
            con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
            while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

            if con_cart == yes:
                item = "Intel Core i5 9600"
                getList.append(item)
                print("\nThis product has been added to the shopping cart.") 
                 
            else:
                 main()

            con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
            while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

            if con_shopping == yes:
                 category()
                 

            else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()
                 

    elif sub_input == '2':
        print("\nPOWER SUPPLY UNIT :-\n")
        print("[1] Supply Unit PSU (PB500) ")
        print("[2] Cooler Master M.WATT LITE")
        print("[3] Thermaltake SMART PRO RGB\n")
        print("Press '1', '2', or '3' to know more about the specified power supply unit that you chose through the index.\n")
        supply_input = (input("INPUT > "))
        print()

        while supply_input not in (option_3):
            print("Invalid input.")
            print("\nPOWER SUPPLY UNIT :-\n")
            print("[1] Supply Unit PSU (PB500) ")
            print("[2] Cooler Master M.WATT LITE")
            print("[3] Thermaltake SMART PRO RGB\n")
            print("Press '1', '2', or '3' to know more about the specified power supply unit that you chose through the index.\n")
            supply_input = (input("INPUT > "))
            print()
            
             
        if supply_input == '1':
             print("NAME: Supply Unit PSU (PB500)\n")
             print("PRODUCT DETAILS:-\n")
             print("- 120mm Silent Fan")
             print("- Single +12V rail")
             print("- Intel Form factor ATX 12V v2.31")
             print("- input frequency 50-60Hz, output capacity 500W\n")
             print("WARRANTY PERIOD: 3 Years\n")
             print("RATINGS: 4.9/5\n")
             print("PRICE: RM 199.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_psu = quantity_1 * 199
             quan_price += quan_price_psu
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "Supply Unit PSU (PB500)"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")      
             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

             if con_shopping == yes:
                 category()
                 

             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()
        
         
        elif supply_input == '2':
             print("NAME: Cooler Master M.WATT LITE\n")
             print("PRODUCT DETAILS:-\n")
             print("- Input voltage 200-240Vac")
             print("- Input current 3.5-5A")
             print("- Input frequency 47-63Hz")
             print("- Fan type: Silent 120mm HDB fan\n")
             print("WARRANTY PERIOD: 3 Years\n")
             print("RATINGS: 4.8/5\n")
             print("PRICE: RM 279.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_mwatt = quantity_1 * 279
             quan_price += quan_price_mwatt
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "Cooler Master M.WATT LITE"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")      
             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

             if con_shopping == yes:
                 category()
                 

             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()

        
        elif supply_input == '3':
             print("NAME: Thermaltake SMART PRO RGB\n")
             print("PRODUCT DETAILS:-\n")
             print("- Pre-intalled, patented 256 colours riing 14 RGB fan ")
             print("- Capacity ranging 650-850W")
             print("- High quality components and fully modular design")
             print("WARRANTY PERIOD: 5 Years\n")
             print("RATINGS: 4.9/5\n")
             print("PRICE: RM 349.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_smart = quantity_1 * 349 
             quan_price += quan_price_smart
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "Thermaltake SMART PRO RGB"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")  
             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

             if con_shopping == yes:
                 category()

             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()

            
    elif sub_input == '3':
        print("\nRAM :-\n")
        print("[1] Kingston ValueRAM 8GB ")
        print("[2] Kingston D4 Predator 3200 2X RGB 16GB")
        print("[3] Corsair D4 VG 3200 C16 RGB PRO 2X 32BG\n")
        print("Press '1', '2', or '3' to know more about the specified RAM that you chose through the index.\n")
        ram_input = (input("INPUT > "))
        print()

        while ram_input not in (option_3):
            print("Invalid input.")
            print("\nRAM :-\n")
            print("[1] Kingston ValueRAM 8GB ")
            print("[2] Kingston D4 Predator 3200 2X RGB 16GB")
            print("[3] Corsair D4 VG 3200 C16 RGB PRO 2X 32BG\n")
            print("Press '1', '2', or '3' to know more about the specified RAM that you chose through the index.\n")
            ram_input = (input("INPUT > "))
            print()
            
             

        if ram_input == '1':
             print("NAME: Kingston ValueRAM 8GB \n")
             print("PRODUCT DETAILS:-\n")
             print("- Pins: 260")
             print("- VDD: 1.2V Typical")
             print("- 16 internal banks; 4 groups of 4 banks each")
             print("- Nominal and dynamic on-die termination(ODT) for data, strobe and mask signal\n")
             print("WARRANTY PERIOD: 3 Years\n")
             print("RATINGS: 4.9/5\n")
             print("PRICE: RM 167.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_king = quantity_1 * 167
             quan_price += quan_price_king
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "Kingston ValueRAM 8GB"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.") 
                 
             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

             if con_shopping == yes:
                 category()
                 

             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()

                 
        elif ram_input == '2':
             print("NAME: Kingston D4 Predator 3200 2X RGB 16GB\n")
             print("PRODUCT DETAILS:-\n")
             print("- VDD: 1.2V Typical")
             print("- VDDQ: 1.2V TYpical, VPP: 2.5V Typical")
             print("- On-die termination(ODT)")
             print("WARRANTY PERIOD: 2 Years\n")
             print("RATINGS: 4.9/5\n")
             print("PRICE: RM 419.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_d4 = quantity_1 * 419
             quan_price += quan_price_d4
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "Kingston D4 Predator 3200 2X RGB 16GB"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")  

             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 
             if con_shopping == yes:
                 category()
                 
             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()


        elif ram_input == '3':
             print("NAME: Corsair D4 VG 3200 C16 RGB PRO 2X 32BG\n")
             print("PRODUCT DETAILS:-\n")
             print("- Dynamic Multi Zone RGB Lighting")
             print("- Custom performance PCB")
             print("- Speed 2133MHz")
             print("- Memory Type: DDR4\n")
             print("WARRANTY PERIOD: 3 Years\n")
             print("RATINGS: 5/5\n")
             print("PRICE: RM 759.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_vg = quantity_1 * 759
             quan_price += quan_price_vg
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "Corsair D4 VG 3200 C16 RGB PRO 2X 32BG"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")  

             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

             if con_shopping == yes:
                 category()
             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()
                 

    elif sub_input == '4':
         print("\nSSD Card :-\n")
         print("[1] Intel 545s Series 128GB")
         print("[2] Kingston HyperX Savage 240GB")
         print("[3] Adata SX-8200 M.2 PCIE NVME 240GB\n")
         print("Press '1', '2', or '3' to know more about the specified SSD Card that you chose through the index.\n")
         ssd_input = (input("INPUT > "))
         print()

         while ssd_input not in (option_3):
             print("Invalid input.")
             print("\nSSD Card :-\n")
             print("[1] Intel 545s Series 128GB")
             print("[2] Kingston HyperX Savage 240GB")
             print("[3] Adata SX-8200 M.2 PCIE NVME 240GB\n")
             print("Press '1', '2', or '3' to know more about the specified SSD Card that you chose through the index.\n")
             ssd_input = (input("INPUT > "))
             print()



         if ssd_input == '1':
             print("NAME: Intel 545s Series\n")
             print("PRODUCT DETAILS:-\n")
             print("- Storage capacity : 128 GB")
             print("- Power : Active 4.5W, Idle: 50mW")
             print("- Sequential read 550MB/s, write 440MB/s")
             print("- Vibration operating: 5-700Hz, non-operaring: 5-800Hz\n")
             print("WARRANTY PERIOD: 3 Years\n")
             print("RATINGS: 4.8/5\n")
             print("PRICE: RM 149.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_545 = quantity_1 * 149
             quan_price += quan_price_545
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "Intel 545s Series"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")       

             else:
                 main()


             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 
             if con_shopping == yes:
                 category()
             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()


         elif ssd_input == '2':
             print("NAME: Kingston HyperX Savage 240GB\n")
             print("PRODUCT DETAILS:-\n")
             print("- Quad-core")
             print("- 8-channel Phison S10 controller")
             print("- read at speed 560MB/s, write speed 530MB/s ")
             print("- Storage capacity 240GB\n")
             print("WARRANTY PERIOD: 3 Year\n")
             print("RATINGS: 4.9/5\n")
             print("PRICE: RM 389\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_svg = quantity_1 * 389
             quan_price += quan_price_svg
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "Kingston HyperX Savage 240GB"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")  

             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 

             if con_shopping == yes:
                 category()
                 

             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()


         elif ssd_input == '3':
             print("NAME: Adata SX-8200 M.2 PCIE NVME 240GB\n")
             print("PRODUCT DETAILS:-\n")
             print("- Capacity: 240GB")
             print("- Controller: SMI")
             print("- Read 2500MB/s, write 3000MB/s\n")
             print("WARRANTY PERIOD: 5 Years\n")
             print("RATINGS: 5/5\n")
             print("PRICE: RM 230\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_pcie = quantity_1 * 230
             quan_price += quan_price_pcie
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "Adata SX-8200 M.2 PCIE NVME 240GB"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")      

             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 
             if con_shopping == yes:
                 category()
             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()

                
    elif sub_input == '5':
         print("\nCOOLING FAN :-\n")
         print("[1] Thermaltake Riing Plus TT Premium Edition")
         print("[2] Cooler Master ML360R RGB")
         print("[3] Corsair HYDRO H100i PRO PLT\n")
         print("Press '1', '2', or '3' to know more about the specified Cooling Fan that you chose through the index.\n")
         fan_input = (input("INPUT > "))
         print()

         while fan_input not in (option_3):
             print("Invalid input.")
             print("\nCOOLING FAN :-\n")
             print("[1] Thermaltake Riing Plus TT Premium Edition")
             print("[2] Cooler Master ML360R RGB")
             print("[3] Corsair HYDRO H100i PRO PLT\n")
             print("Press '1', '2', or '3' to know more about the specified Cooling Fan that you chose through the index.\n")
             fan_input = (input("INPUT > "))
             print()

         if fan_input == '1':
             print("NAME: Thermaltake Riing Plus TT Premium Edition\n")
             print("PRODUCT DETAILS:-\n")
             print("- 12 LED RGB radiator fan (5 Fan Pack)")
             print("- 120mm high-static pressure fan")
             print("- Fan speed: 500-1600 RPM")
             print("WARRANTY PERIOD: 2 Years\n")
             print("RATINGS: 4.8/5\n")
             print("PRICE: RM 539\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_tt = quantity_1 * 539
             quan_price += quan_price_tt
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "Thermaltake Riing Plus TT Premium Edition"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")       

             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 
             if con_shopping == yes:
                 category()
             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()


         elif fan_input == '2':
             print("NAME: Cooler Master ML360R RGB\n")
             print("PRODUCT DETAILS:-\n")
             print("- Speed Controller: BIOS")
             print("- Fan Speed: 650 - 2000 RPM")
             print("- Fan Airflow: 66.7 CFM ")
             print("- Quiet operation; Fan Noise: 6.0 - 30 dBA\n")
             print("WARRANTY PERIOD: 2 Years\n")
             print("RATINGS: 4.9/5\n")
             print("PRICE: RM 489\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_ml = quantity_1 * 489
             quan_price += quan_price_ml
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "Cooler Master ML360R RGB"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")       

             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")

             if con_shopping == yes:
                 category()
             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()


         elif fan_input == '3':
             print("NAME: Corsair HYDRO H100i PRO PLT\n")
             print("PRODUCT DETAILS:-\n")
             print("- Number of Fans 2")
             print("- Radiator Size 240mm")
             print("- Fan Airflow 75 CFM, Fan Static Pressure 4.2 mm-H2O\n")
             print("WARRANTY PERIOD: 5 Years\n")
             print("RATINGS: 5/5\n")
             print("PRICE: RM 599\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_hydro = quantity_1 * 599
             quan_price += quan_price_hydro
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "Corsair HYDRO H100i PRO PLT"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")  
             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 
             if con_shopping == yes:
                 category()
             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()


    elif sub_input == '6':
         print("\nMOTHERBOARD :-\n")
         print("[1] Micro-ATX Motherboard")
         print("[2] MSI B450M PRO-M2 V2")
         print("[3] ASUS PRIME B450M-K\n")
         print("Press '1', '2', or '3' to know more about the specified mouse that you chose through the index.\n")
         board_input = (input("INPUT > "))
         print()

         while board_input not in (option_3):
             print("Invalid input.")
             print("\nMOTHERBOARD :-\n")
             print("[1] Micro-ATX Motherboard")
             print("[2] MSI B450M PRO-M2 V2")
             print("[3] ASUS PRIME B450M-K\n")
             print("Press '1', '2', or '3' to know more about the specified mouse that you chose through the index.\n")
             board_input = (input("INPUT > "))
             print()

         if board_input == '1':
             print("NAME: Micro-ATX Motherboard\n")
             print("PRODUCT DETAILS:-\n")
             print("- Supported RAM Speed: PC2-6400, PC2-8500")
             print("- Power Connectors: 24-pin main power connector")
             print("- BIOS FeaturesDMI 2.0 support, ACPI 1.0b support")
             print("- Software Included: Norton Internet Security\n")
             print("WARRANTY PERIOD: 3 Years\n")
             print("RATINGS: 4.8/5\n")
             print("PRICE: RM 259\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_atx = quantity_1 * 259
             quan_price += quan_price_atx
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "Micro-ATX Motherboard"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")  

             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 
             if con_shopping == yes:
                 category()
             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()
                 

         elif board_input == '2':
             print("NAME: MSI B450M PRO-M2 V2\n")
             print("PRODUCT DETAILS:-\n")
             print("- CPU (MAX SUPPORT): Ryzen 9")
             print("- MEMORY CHANNEL: Dual")
             print("- MAX MEMORY: 64GB ")
             print("- 1 x 24-pin ATX main power connector\n")
             print("WARRANTY PERIOD: 3 Year\n")
             print("RATINGS: 4.9/5\n")
             print("PRICE: RM 310\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_v2 = quantity_1 * 310
             quan_price += quan_price_v2
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "MSI B450M PRO-M2 V2"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")   

             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")

             if con_shopping == yes:
                 category()
             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()


         elif board_input == '3':
             print("NAME: ASUS PRIME B450M-K\n")
             print("PRODUCT DETAILS:-\n")
             print("- MEMORY: AMD Ryzen 2nd Generation/Ryzen with Radeon Vega Graphics/Ryzen 1st Generation Processors")
             print("- Dual Channel Memory Architecture")
             print("- Storage: 4 x SATA 6Gb/s port(s), gray\n")
             print("WARRANTY PERIOD: 3 Years\n")
             print("RATINGS: 5/5\n")
             print("PRICE: RM 359\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_prime = quantity_1 * 359
             quan_price += quan_price_prime
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "ASUS PRIME B450M-K"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")      

             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 
             if con_shopping == yes:
                 category()
             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()

    
def category_4():  # Defining function for External Components Category
    global quan_price
    print("Choose which sub-category do you want to proceed:\n")
    print("[1] PRINTERS")
    print("[2] KEYBOARDS")
    print("[3] MONITORS")
    print("[4] MICE\n")
    print("Press '1' for 'PRINTERS' , '2' for 'KEYBOARDS' , '3' for 'MONITORS' or '4' for 'MICE'\n")
    sub_input = (input("INPUT > "))

    while sub_input not in (option_2):
        print("\nInvalid input.\n")
        print("Choose which sub-category do you want to proceed:\n")
        print("[1] PRINTERS")
        print("[2] KEYBOARDS")
        print("[3] MONITORS")
        print("[4] MICE\n")
        print("Press '1' for 'PRINTERS' , '2' for 'KEYBOARDS' , '3' for 'MONITORS' or '4' for 'MICE'\n")
        sub_input = (input("INPUT > "))

    if sub_input == '1':
         print("\nPRINTERS :-\n")
         print("[1] Canon imageCLASS LBP6030 (Print Only) Mono Laser Printer")
         print("[2] Epson EcoTank L3150 Wi-Fi All-in-One Ink Tank Printer")
         print("[3] BROTHER DCP-T510W DCP T510W 3in1 Printer\n")
         print("Press '1', '2', or '3' to know more about the specified printer that you chose through the index.\n")
         prin_input = (input("INPUT > "))
         print()

         while prin_input not in (option_3):
             print("Invalid input.")
             print("\nPRINTERS :-\n")
             print("[1] Canon imageCLASS LBP6030 (Print Only) Mono Laser Printer")
             print("[2] Epson EcoTank L3150 Wi-Fi All-in-One Ink Tank Printer")
             print("[3] BROTHER DCP-T510W DCP T510W 3in1 Printer\n")
             print("Press '1', '2', or '3' to know more about the specified printer that you chose through the index.\n")
             prin_input = (input("INPUT > "))
             print()
             

         if prin_input == '1':
             print("NAME: Canon imageCLASS LBP6030 (Print Only) Mono Laser Printer - compatible with toner cartridge 325\n")
             print("PRODUCT DETAILS:-\n")
             print("- Print")
             print("- Print Speed (A4): Up to 18ppm")
             print("- Recommended monthly print volume: 200 - 800 pages")
             print("- Sleep mode and Auto Shutdown feature\n")
             print("WARRANTY PERIOD: 3 Years\n")
             print("RATINGS: 4.6/5\n")
             print("PRICE: RM312.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_lbp = quantity_1 * 312
             quan_price += quan_price_lbp
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("\nAre you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "Canon imageCLASS LBP6030 (Print Only) Mono Laser Printer"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")
                 
             else:
                 main()

             con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("\nAre you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")

             if con_shopping == yes:
                 category()
             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()
                 

         elif prin_input == '2':
            print("NAME: Epson EcoTank L3150 Wi-Fi All-in-One Ink Tank Printer with Hybrid Ink ")
            print("PRODUCT DETAILS:-\n")
            print("- Compact integrated tank design")
            print("- High yield ink bottles")
            print("- Spill-free, error-free refilling")
            print("- Wi-Fi, Wi-Fi Direct\n")
            print("WARRANTY PERIOD: 1 Year\n")
            print("RATINGS: 4.8/5\n")
            print("PRICE: RM569.00\n")
            
            quantity_1 = float(input("QUANTITY(in digits): "))
            quan_price_eco = quantity_1 * 569
            quan_price += quan_price_eco
            
            print(f"\nTotal price: RM{quan_price}")
            con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
            while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

            if con_cart == yes:
                item = "Epson EcoTank L3150 Wi-Fi All-in-One Ink Tank Printer"
                getList.append(item)
                print("\nThis product has been added to the shopping cart.")   
            else:
                 main()

            con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
            while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 
            if con_shopping == yes:
                 category()
            else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()

        
         elif prin_input == '3':
            print("NAME: BROTHER DCP-T510W DCP T510W 3in1 ")
            print("PRODUCT DETAILS:-\n")
            print("- Print, Scan & Copy with Built-in Wireless.Wifi-Direct, Direct Mobile Print/Scan")
            print("- Low cost quality printing with Ultra-high 6500 page yield (black ink) / 5000 page yield (colour ink)")
            print("- Flexible paper handling with Default Paper Tray & 1-sheet Manual Feed Slot")
            print("- Borderless printing\n")
            print("WARRANTY PERIOD: 3 Years\n")
            print("RATINGS: 5/5\n")
            print("PRICE: RM689.00\n")
            
            quantity_1 = float(input("QUANTITY(in digits): "))
            quan_price_dcp = quantity_1 * 689
            quan_price += quan_price_dcp
            
            print(f"\nTotal price: RM{quan_price}")
            con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
            while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

            if con_cart == yes:
                item = "BROTHER DCP-T510W DCP T510W 3in1"
                getList.append(item)
                print("\nThis product has been added to the shopping cart.")  

            else:
                 main()
                 
            con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
            while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")

            if con_shopping == yes:
                 category()
            else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()


    elif sub_input == '2':
        print("\nKEYBOARDS :-\n")
        print("[1] Razer Cynosa Chroma Gaming Keyboard ")
        print("[2] AULA F2058/F2088 Mechanical Gaming Keyboard")
        print("[3] FANTECH WK-893 Keyboard\n")
        print("Press '1', '2', or '3' to know more about the specified keyboard that you chose through the index.\n")
        key_input = (input("INPUT > "))
        print()

        while key_input not in (option_3):
            print("Invalid input.")
            print("\nKEYBOARDS :-\n")
            print("[1] Razer Cynosa Chroma Gaming Keyboard ")
            print("[2] AULA F2058/F2088 Mechanical Gaming Keyboard")
            print("[3] FANTECH WK-893 Keyboard\n")
            print("Press '1', '2', or '3' to know more about the specified keyboard that you chose through the index.\n")
            key_input = (input("INPUT > "))
            print()
            
        if key_input == '1':
             print("NAME: Razer Cynosa Chroma Gaming Keyboard\n")
             print("PRODUCT DETAILS:-\n")
             print("- Soft cushioned keys with gaming-grade performance")
             print("- 104 individually customizable backlit keys")
             print("- Spill-resistant durable design")
             print("- 10 key roll-over with anti-ghosting\n")
             print("WARRANTY PERIOD: 2 Years\n")
             print("RATINGS: 4.9/5\n")
             print("PRICE: RM239.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_cynosa = quantity_1 * 239
             quan_price += quan_price_cynosa
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "Razer Cynosa Chroma Gaming Keyboard"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")

             else:
                 main()
                 
             con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")

             if con_shopping == yes:
                 category()
             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()
   
        elif key_input == '2':
             print("NAME: AULA F2058/F2088 Mechanical Gaming Keyboard\n")
             print("PRODUCT DETAILS:-\n")
             print("- Real machanical keyboard with blue switch.")
             print("- 104 Anti-ghosting Keys,Full Key without Conflict")
             print("- 22 kinds of illusion lighting effects can be realized through the reactor button")
             print("- Multi-function Alloy Knob,Knob controls volume\n")
             print("WARRANTY PERIOD: 6 Months\n")
             print("RATINGS: 4.8/5\n")
             print("PRICE: RM219.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_aula = quantity_1 * 219
             quan_price += quan_price_aula
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "AULA F2058/F2088 Mechanical Gaming Keyboard"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")   

             else:
                 main()

             con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 
             if con_shopping == yes:
                 category()
             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()
        
        elif key_input == '3':
             print("NAME: FANTECH WK-893 Keyboard\n")
             print("PRODUCT DETAILS:-\n")
             print("- Keyboard: With rear stand, convenient to use.")
             print("- Standard 104 buttons keyboard")
             print("- Water leakge type structural design")
             print("- System support: Windows 7, Windows 8 and latest, Mac OS, linux ,Chrome OS\n")
             print("WARRANTY PERIOD: 3 Months\n")
             print("RATINGS: 4.9/5\n")
             print("PRICE: RM89.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_wk = quantity_1 * 89
             quan_price += quan_price_wk
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = "FANTECH WK-893 Keyboard"
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")  
             else:
                 main()

             con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                
             if con_shopping == yes:
                 category()
             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()

    elif sub_input == '3':
        print("\nMONITORS :-\n")
        print("[1] HP 24y 23.8' Full HD 60Hz IPS Monitor")
        print("[2] Xiaomi 34 Inch Ultrawide monitor 2k 144hz")
        print("[3] BenQ EW2780 27 inch HDRi Screen\n")
        print("Press '1', '2', or '3' to know more about the specified monitor that you chose through the index.\n")
        mon_input = (input("INPUT > "))
        print()

        while mon_input not in (option_3):
            print("Invalid input.")
            print("\nMONITORS :-\n")
            print("[1] HP 24y 23.8' Full HD 60Hz IPS Monitor")
            print("[2] Xiaomi 34 Inch Ultrawide monitor 2k 144hz")
            print("[3] BenQ EW2780 27 inch HDRi Screen\n")
            print("Press '1', '2', or '3' to know more about the specified monitor that you chose through the index.\n")
            mon_input = (input("INPUT > "))
            print() 

        if mon_input == '1':
             print('NAME: HP 24y 23.8" Full HD 60Hz IPS Monitor\n')
             print("PRODUCT DETAILS:-\n")
             print("- 23.8' diagonal screen")
             print("- IPS panel with LED backlight")
             print("- Get crisp, clear picture with 1080p resolution")
             print("- VGA, DVI, and HDMI ports\n")
             print("WARRANTY PERIOD: 3 Years\n")
             print("RATINGS: 4.9/5\n")
             print("PRICE: RM439.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_ips = quantity_1 * 439
             quan_price += quan_price_ips
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = 'HP 24y 23.8" Full HD 60Hz IPS Monitor'
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")   

             else:
                 main()

             con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")

             if con_shopping == yes:
                 category()
             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()

        elif mon_input == '2':
             print("NAME: Xiaomi 34 Inch Ultrawide monitor 2k 144hz\n")
             print("PRODUCT DETAILS:-\n")
             print("- Ultra clear image with clear details")
             print("- 21:9 wide panoramic view")
             print("- 1500R large curvature surrounded visual field")
             print("- 144Hz high refresh rate\n")
             print("WARRANTY PERIOD: 2 Years\n")
             print("RATINGS: 4.9/5\n")
             print("PRICE: RM2199.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_xiaomi = quantity_1 * 2199
             quan_price += quan_price_xiaomi
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = 'Xiaomi 34 Inch Ultrawide monitor 2k 144hz'
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")  
                 
             else:
                 main()

             con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 
             if con_shopping == yes:
                 category()                 
             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()


        elif mon_input == '3':
             print("NAME: BenQ EW2780 27 inch HDRi Screen Monitor\n")
             print("PRODUCT DETAILS:-\n")
             print("- Entertainment Monitor with Eye-care Tech")
             print("- 27 inch FHD 16:9 IPS Display")
             print("- Edge to Edge Slim Bezel Design")
             print("- High Dynamic Range (HDR)\n")
             print("WARRANTY PERIOD: 3 Years\n")
             print("RATINGS: 5/5\n")
             print("PRICE: RM829.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_benq = quantity_1 * 829
             quan_price += quan_price_benq
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = 'BenQ EW2780 27 inch HDRi Screen Monitor'
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")   

             else:
                 main()

             con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 
             if con_shopping == yes:
                 category()
             else:
                 print("\nThank you, See you again !!!/")
                 shoppingCart()


    elif sub_input == '4':
         print("\nMICE :-\n")
         print("[1] Logitech® M330 Silent Mouse")
         print("[2] AULA S20 Gaming Mouse")
         print("[3] Razer DeathAdder Elite Gaming Mouse\n")
         print("Press '1', '2', or '3' to know more about the specified mouse that you chose through the index.\n")
         mice_input = (input("INPUT > "))
         print()

         while mice_input not in (option_3):
             print("Invalid input.")
             print("\nMICE :-\n")
             print("[1] Logitech® M330 Silent Mouse")
             print("[2] AULA S20 Gaming Mouse")
             print("[3] Razer DeathAdder Elite Gaming Mouse\n")
             print("Press '1', '2', or '3' to know more about the specified mouse that you chose through the index.\n")
             mice_input = (input("INPUT > "))
             print()

         if mice_input == '1':
             print("NAME: Logitech M330 Silent Mouse\n")
             print("PRODUCT DETAILS:-\n")
             print("- Over 90% noise reduction")
             print("- Reliable Logitech 2.4GHz wireless technology")
             print("- 24-month battery life")
             print("- Plug-and-play connection - Universal\n")
             print("WARRANTY PERIOD: 1 Year\n")
             print("RATINGS: 4.8/5\n")
             print("PRICE: RM71.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_m330 = quantity_1 * 71
             quan_price += quan_price_m330
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = 'Logitech M330 Silent Mouse'
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")  

             else:
                 main()

             con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")

             if con_shopping == yes:
                 category()
             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()

         
         elif mice_input == '2':
             print("NAME: AULA S20 Gaming Mouse\n")
             print("PRODUCT DETAILS:-\n")
             print("- 4-Color breathing light")
             print("- DPI 800/1200/1600/2400 Four-stage DPI regulation")
             print("- Switch about 10 million times")
             print("- Ergonomic design feel comfortable\n")
             print("WARRANTY PERIOD: 1 Year\n")
             print("RATINGS: 4.9/5\n")
             print("PRICE: RM 51\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_s20 = quantity_1 * 51.90
             quan_price += quan_price_s20
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = 'AULA S20 Gaming Mouse'
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")     

             else:
                 main()

             con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 
             if con_shopping == yes:
                 category()
             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()


         elif mice_input == '3':
             print("NAME: Razer DeathAdder Elite Gaming Mouse\n")
             print("PRODUCT DETAILS:-\n")
             print("- THE WORLD'S MOST ADVANCED OPTICAL SENSOR")
             print("- GAMING-OPTIMIZED RAZER MECHANICAL MOUSE SWITCHES")
             print("- ERGONOMIC FORM FACTOR\n")
             print("WARRANTY PERIOD: 1 Year\n")
             print("RATINGS: 5/5\n")
             print("PRICE: RM279.00\n")
             
             quantity_1 = float(input("QUANTITY(in digits): "))
             quan_price_razer = quantity_1 * 279.00
             quan_price += quan_price_razer
             
             print(f"\nTotal price: RM{quan_price}")
             con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")
             while con_cart not in option_1:
                 print("\nInvalid input...")
                 con_cart = input("Are you sure that you want to add this product in the shopping cart(press 'y' for 'yes' or 'n' for 'go back')?: ")

             if con_cart == yes:
                 item = 'Razer DeathAdder Elite Gaming Mouse'
                 getList.append(item)
                 print("\nThis product has been added to the shopping cart.")    
             else:
                 main()

             con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
             while con_shopping not in option_1:
                 print("\nInvalid input...")
                 con_shopping = input("Are you sure that you want to continue shopping?(Press 'y' for 'yes' or 'n' for 'no'): ")
                 
             if con_shopping == yes:
                 category()
             else:
                 print("\nThank you, See you again !!!\n")
                 shoppingCart()


#================================================= R E V I E W  &  R A T I N G S ======================================================================


def review(): # Defining function for Reviews from Customers
    customer_name = input('\nEnter your Name: ')
    comments = input('\nLeave a comment about our services and the products: ')
    print('\n*Customer Review*')
    print(f'{customer_name}:{comments}')

def ratings(): # Defining function for Ratings from Customers
    print('\n****** Rate our products and services ******')
    print('\nRate us a number between 1 - 5')
    Product  = input('\nProduct Ratings  : ')
    if Product == '1':
        print('*')
    elif Product == '2':
        print('* *')
    elif Product == '3':
        print('*  *  *')
    elif Product == '4':
        print('*  *  *  *')
    elif Product == '5':
        print('*  *  *  *  *')
    else:
        print("I'm not satisfied with your products")
    Services = input('\nServices Ratings : ')
    if Services == '1':
        print('*')
    elif Services == '2':
        print('* *')
    elif Services == '3':
        print('*  *  *')
    elif Services == '4':
        print('*  *  *  *')
    elif Services == '5':
        print('*  *  *  *  *')
    else:
        print("I'm disappointed about your services")
    
    print('\nThank You For Your Response.  :)')
    main()

#============================================ S H O P P I N G  C A R T  S E C T I O N ===============================================

def shoppingCart():                                         # Display option user want to input
    print('\n\n++++++++++++++++++++++++++++++++')
    print('          SHOPPING CART         ')
    print('++++++++++++++++++++++++++++++++')
    print('\nYou got ', len(getList),'items.\n')
    print('Press A to add item ')
    print('Press V to view item ')
    print('Press D to delete item')
    print('Press P for proceed to checkout')
    print('Press M to return to main page')
    print('\nKindly double check your item in "view item(v)" before proceed to payment\n')
    choose = input('choose: ')
    
    if len(choose) > 0:
        if choose.lower()[0] == 'a':
            category()
        elif choose.lower()[0] == 'd':
            delItem()
        elif choose.lower()[0] == 'v':      # Before proceed payment, user need to view item first in order to finalise the total price
            viewList()
        elif choose.lower()[0] == 'p':
            paymentService()                         #kishen's module
            main()
        elif choose.lower()[0] == 'm':
            main()
        else:
            shoppingCart()
    else:
        shoppingCart()
        

def delItem():                           # Delete selected item
    global getList
    count = 0
    for item in getList:
        print(count, ' - ', item)
        count = count + 1

    print('Which number you want to delete? ')          # Delete product by choosing number
    print('\nPress ENTER to return to shopping cart.')
    choice = input('Number: ')
    if len(choice) > 0:
        try:
            del getList[int(choice)]
            print('Item has been deleted\n')
            
        except:
            print('Invalid number\n')
        delItem()
    else:
        shoppingCart()

def viewList():                              #Display output of choosen item
    global getList
    global final
    global name
    global address
    print('\n\n++++++++++++++++++++++++++++++++++++++++++')
    print('                 SHOPPING CART                ')
    print('++++++++++++++++++++++++++++++++++++++++++')

    n = 0
    total = 0
    sp = 3

    while n < len(getList): 
        print('\nItem: ', getList[n])
        n += 1

    print('\n-----------------------------------------\n')
    print('Subtotal : RM ', quan_price)
    print('Shipping delivery = RM 3')
    print('Total payment : RM ', quan_price + sp)   # Subtotal + shipping delivery
    final = quan_price + sp
    name = input('\nPlease enter your name and the shipping address. \nName: ')
    address = input('Enter the shipping address : ')
    print('\n-----------------------------------------')
    print('\nDo you want to proceed to payment? if YES, press "y"')
    pay = input('\nIf NO, press ENTER to return to shopping cart : ')
    
    if pay.lower() == 'y':
        paymentService()
    else:
        shoppingCart()


def reciept():              # Display reciept after payment succeed
    global getList
    global final
    global name
    global address
    print('\n++++++++++++++++++++++++++++++++++++++++++')
    print('               PAYMENT RECIEPT             ')
    print('++++++++++++++++++++++++++++++++++++++++++\n')
    for item in getList:
        print(item)

    print('\n-----------------------------------------')
    print('Subtotal : RM ', quan_price)
    print('Shipping delivery = RM 3')
    print('Total payment : RM ', final)
    print('Name : ', name)
    print('Shipping Address : ', address)
    print('-------------------------------')
    print('\n\nThank You for your purchase, See You Again!\n')

#=================================================== P A Y M E N T  S E R V I C E ======================================================

def paymentService():
    global final
    print("\n\n*******************Welcome to the payment services*******************\n")
    print("Choose which method do you want to proceed:\n")  # Displaying the option
    print("[1] CREDIT CARD")
    print("[2] DEBIT CARD")
    print("[3] ONLINE BANKING\n")
    print("Press '1' for 'Credit Card' , '2' for 'Debit Card' or '3' for 'Online Banking.'")

    input_1 = input("\nInput > ") . lower()

    options = ['1','2','3','4']
        
    while input_1 not in options:                       #making sure the input given is valid based on options list
        print("ERROR: Invalid Input")
        input_1 = input("Input > ") . lower()
        
    yes = "y".lower()
    no = "n".lower()

    option_1 = [yes,no]
    option_2 = ['1','2']
    option_3 = ['1','2','3','4','5']

    if input_1 == '1':              
        print("\nThrough Credit Card Payment:")
        pay_1()                                          # Calling the function for credit card payment
    elif input_1 == '2':
        print("\nThrough Debit Card Payment:")
        pay_1()                                          # Calling the function for debit card payment
    elif input_1 == '3':
        print("\nThrough Online Banking:")
        pay_2()                                          # Calling the function for online banking payment
    else:
        main()
    

#If user chooses payment through 'Credit Card' or 'Debit Card'
def pay_1():  # Defining the function for payment using credit card and debit card
    list_1 = []
    print("\nType of card:\n\n[1] Visa\n[2] Mastercard\n") #Ask the user for type of card
    print("Press '1' for 'Visa' or '2' for 'Mastercard'.")
    card_type = (input("\nInput > "))

    while card_type not in (option_2):
        print("ERROR: Invalid Input")
        print("\nType of card:\n\n[1] Visa\n[2] Mastercard\n")
        print("Press '1' for 'Visa' or '2' for 'Mastercard'.")
        card_type = (input("\nInput > "))
        
    if card_type == '1':
        list_1.append("Visa")
    elif card_type == '2':
        list_1.append("Master Card")
        
    card_name = (input("\nEnter your card name(***Must only contain alphabets which is in the form of only 'UPPERCASE'***): "))  #Ask the user for name of the card
    while (card_name.isalpha() and card_name.isupper()) == False:
         print("\nInvalid Card Name...")
         card_name = (input("\nEnter your card name(***Must only contain alphabets which is in the form of only 'UPPERCASE'***): "))
    if (card_name.isalpha() and card_name.isupper())== True:
      list_1.append(card_name)
      
      card_num = int(input("\nEnter your card number(***Must only contain 16 digits***): "))    #Ask the user for card number
      count_num = (len(str(abs(card_num))))
      while count_num != 16:
          print("\nInvalid card number, Please try again...")
          card_num = int(input("\nEnter your card number(***Must only contain 16 digits***): "))
          count_num = (len(str(abs(card_num))))
      if count_num == 16:
          list_1.append(card_num)
          
          exp_date = (input("\nEnter the expiry date(***Must only contain symbol('/') and digits***)\nFor example: '12/20': "))        #Ask the user for expiry date of the card
          count_exp = exp_date.count('/')
          while count_exp != 1:
              print("\nInvalid expiry date, Please try again...")
              exp_date = (input("\nEnter the expiry date(***Must contain symbol('/') and digits***)\nFor example: '12/20': "))
              count_exp = exp_date.count('/')
          if count_exp == 1:
              list_1.append(exp_date)
                            
              cvv = int(input("\nEnter CVV(***Must only contain 3 digits***): "))           #Ask the user for CVV of the card
              count_cvv = (len(str(abs(cvv))))
              while count_cvv != 3:
                  print("\nInvalid CVV, Please try again...")
                  cvv = int(input("\nEnter CVV(***Must only contain 3 digits***): "))
                  count_cvv = (len(str(abs(cvv))))
              if count_cvv == 3:
                  list_1.append(cvv)
                  
                  print("\nSecure TAC code has been sent to your mobile phone number via SMS...\n")
                  tac_code = int(input("Enter 6-digit secure TAC-Code: "))               #Ask the user for Secure TAC Code
                  count_tac = (len(str(abs(tac_code))))
                  while count_tac != 6:
                      print("\nInvalid TAC Code, Please try again...")
                      tac_code = int(input("\nEnter 6-digit secure TAC-Code: "))
                      count_tac = (len(str(abs(tac_code))))
                  if count_tac == 6:
                    print("Here is the card information of the user:\n")                 # Displaying the information of the user's card
                    print("Card Type:",list_1[0])
                    print("Card Name:",list_1[1])
                    print("Card Number:",list_1[2])
                    print("Card Expiry Date:",list_1[3])
                    print("Card CVV:",list_1[4])
                    print("Secure TAC Code: ******")
                    print()
                    
                    con_info = input("Is your card details correct(press 'y' for Yes or 'n' for No): ").lower()    # Asking the user for the validity of the information in the card
                    while con_info not in option_1:
                        print("\nInvalid input")
                        con_info = input("\nIs your card details correct(press 'y' for Yes or 'n' for No): ").lower()
                    if con_info == yes:
                       print("\nTotal payment: RM ", final)            
                       
                       con_pay = input("\nDo u want to proceed to the confirmation of payment (press 'y' for Yes or 'n' for No): ").lower() # Asking the user for proceed to the confirmation of payment
                       while con_pay not in option_1:
                        print("\nInvalid input")
                        con_pay = input("\nDo u want to proceed to the confirmation of payment (press 'y' for Yes or 'n' for No): ").lower()
                       if con_pay == yes:
                            print("\nPayment Successful !!!\n")                        # Displaying result
                            print("Your order has been placed...\n\n")
                            reciept()
                            print("\nWould you help us to review our product?\nThank you! :) ")
                            review()
                            ratings()
                            
                       elif con_pay == no:
                            print("\nPayment Unsuccessful\n")
                            main()
                          
                    elif con_info == no:
                        pay_1()


#If user chooses payment through 'Online Banking'
def pay_2():  # Defining the function for payment using online banking services
   print("\nChoose which bank do you want to login:\n")  # Displaying the options
   print("[1] Maybank2U")
   print("[2] CIMB Clicks")
   print("[3] Public Bank")
   print()
   print("Press '1' for 'Maybank2u' , '2' for 'CIMB Clicks', '3' for 'Public Bank'")

   
   input_2 = input("\nInput > ") . lower()

   while input_2 not in option_3: #making sure the input given is valid based on options list
    print("\nERROR: Invalid Input")
    input_2 = input("\nInput > ") . lower()

   if input_2 == "1":      # If user chooses option '1'
     print("\nProceeding to the Maybank2U Online Services...\n")
     print("maybank2u.com\n")
     print("Note:-")
     print("- You are in a secured site.")
     print("- Never login via email links.")
     print("- Never reveal your pin and/or Password to anyone.\n")
     
     user_id = input("User ID(Must only contains alphabets which is in the form of only 'UPPERCASE' and digits): ")         # Asking the user for user id of the bank
     while (user_id.isalnum() and user_id.isupper()) == False:
         print("\nInvalid User ID...")
         user_id = input("\nUser ID(Must only contains alphabets which is in the form of only 'UPPERCASE' and digits): ")
         
     if (user_id.isalnum() and user_id.isupper()) == True:
         secure_word = print("\nSecure Word: DIGITRONICS2813\n")       # Displaying Secure Word
         print("-If this is your Secure Word, type:'y'")
         print("-If this is not your Secure Word, type:'n'")
         print("-Do not proceed unless this is not your secure word")
         print()
         
         con_secure = input("Input: ")
         while con_secure not in option_1:
             print("\nInvalid input")
             secure_word = print("\nDIGITRONICS2813")

         if con_secure == 'y':
            pass_word = input("\nPassword(Must contain at least 1 special character and all must be 'UPPERCASE' letters and digits): ")   # Asking the user for the password of the online banking services
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if(regex.search(pass_word) == None):
              while (pass_word.isupper()) == False:
                   print("\nInvalid Pass Word")
                   pass_word = input("\nPassword(Must contain at least 1 special character and all must be 'UPPERCASE' letters and digits): ")
                 
            else:
                 if(pass_word.isupper()) == True:
                     print("\nTotal Payment: RM ", final)
                     
                     
                     con_pay1 = input("\nDo u want to proceed to the confirmation of payment (press 'y' for Yes or 'n' for No): ").lower()   # Asking the user for the confirmation of payment
                     while con_pay1 not in option_1:
                        print("\nInvalid input")
                        con_pay1 = input("\nDo u want to proceed to the confirmation of payment (press 'y' for Yes or 'n' for No): ").lower()
                     if con_pay1 == yes:
                           print("\nSecure TAC code has been sent to your mobile phone number via SMS...\n")
                           tac_code1 = int(input("Enter 6-digit secure TAC-Code: ")) # Asking the user for the Secure TAC-Code
                           count_tac1 = (len(str(abs(tac_code1))))
                           while count_tac1 != 6:
                                print("\nInvalid TAC Code, Please try again...")
                                tac_code1 = int(input("\nEnter 6-digit secure TAC-Code: "))
                                count_tac1 = (len(str(abs(tac_code1))))
                                
                           if count_tac1 == 6:
                               print("\nPayment Successful !!!\n")     # Displaying the result
                               print("We have notified the seller to ship out your order.\n\n")
                               reciept()
                               print("\nWould you help us to review our product?\nThank you! :) ")
                               review()
                               ratings()
                               
                     elif con_pay1 == no:
                           print("\nPayment Unsuccessful\n")
                           main()

         elif con_secure == 'n':
             pay_2()
    
                            
   elif input_2 == "2":          # If user chooses option '2'
     print("\nProceeding to the CIMBCLICKS Online Services...\n")
     print("CIMBCLICKS.com\n")
     print("Note:-")
     print("- You are in a secured site.")
     print("- Never login via email links.")
     print("- Never reveal your pin and/or Password to anyone.\n")
     
     user_id = input("User ID(Must only contains alphabets which is in the form of only 'UPPERCASE' and digits): ")
     while (user_id.isalnum() and user_id.isupper()) == False:
         print("\nInvalid User ID...")
         user_id = input("\nUser ID(Must only contains alphabets which is in the form of only 'UPPERCASE' and digits): ")
         
     if (user_id.isalnum() and user_id.isupper()) == True:
         secure_word = print("\nSecure Word: MAKERED_KING\n")
         print("-If this is your Secure Word, type:'y'")
         print("-If this is not your Secure Word, type:'n'")
         print("-Do not proceed unless this is not your secure word")
         print()
         
         con_secure = input("\nInput: ")
         while con_secure not in option_1:
             print("\nInvalid input")
             secure_word = print("\nMAKERED_KING")

         if con_secure == 'y':
            pass_word = input("\nPassword(Must contain at least 1 special character and all must be 'UPPERCASE' letters and digits): ")
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if(regex.search(pass_word) == None):
              while (pass_word.isupper()) == False:
                   print("\nInvalid Pass Word")
                   pass_word = input("\nMust contain at least 1 special character all must be 'UPPERCASE' letters and digits): ")
                 
            else:
                 if(pass_word.isupper()) == True:
                     print("\nTotal Payment: RM ", final)             
                     
                     con_pay1 = input("\nDo u want to proceed to the confirmation of payment (press 'y' for Yes or 'n' for No): ").lower()
                     while con_pay1 not in option_1:
                        print("\nInvalid input")
                        con_pay1 = input("\nDo u want to proceed to the confirmation of payment (press 'y' for Yes or 'n' for No): ").lower()
                     if con_pay1 == yes:
                           print("\nSecure TAC code has been sent to your mobile phone number via SMS...\n")
                           tac_code1 = int(input("Enter 6-digit secure TAC-Code: "))
                           count_tac1 = (len(str(abs(tac_code1))))
                           while count_tac1 != 6:
                                print("\nInvalid TAC Code, Please try again...")
                                tac_code1 = int(input("\nEnter 6-digit secure TAC-Code: "))
                                count_tac1 = (len(str(abs(tac_code1))))
                                
                           if count_tac1 == 6:
                               print("\nPayment Successful !!!\n")
                               print("We have notified the seller to ship out your order.\n\n")
                               reciept()
                               print("\nWould you help us to review our product?\nThank you! :) ")
                               review()
                               ratings()
                               
                            
                     elif con_pay1 == no:
                           print("\nPayment Unsuccessful\n")
                           main()
                
         elif con_secure == 'n':
             pay_2()


             
   elif input_2 == "3":        # If user chooses option '3'
     print("\nProceeding to the Public Bank Berhad Online Services...\n")
     print("PBE.com\n")
     print("Note:-")
     print("- You are in a secured site.")
     print("- Never login via email links.")
     print("- Never reveal your pin and/or Password to anyone.\n")
     
     user_id = input("User ID(Must only contains alphabets which is in the form of only 'UPPERCASE' and digits): ")
     while (user_id.isalnum() and user_id.isupper()) == False:
         print("\nInvalid User ID...")
         user_id = input("\nUser ID(Must only contains alphabets which is in the form of only 'UPPERCASE' and digits): ")
         
     if (user_id.isalnum() and user_id.isupper()) == True:
         secure_word = print("\nSecure Word: KENNY_WENDY\n")
         print("-If this is your Secure Word, type:'y'")
         print("-If this is not your Secure Word, type:'n'")
         print("-Do not proceed unless this is not your secure word")
         print()
         
         con_secure = input("Input: ")
         while con_secure not in option_1:
             print("\nInvalid input")
             secure_word = print("\nKENNY_WENDY")

         if con_secure == 'y':
            pass_word = input("\nPassword(Must contain at least 1 special character and all must be 'UPPERCASE' letters and digits): ")
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if(regex.search(pass_word) == None):
              while (pass_word.isupper()) == False:
                   print("\nInvalid Pass Word")
                   pass_word = input("\nMust contain at least 1 special character and all must be 'UPPERCASE' letters and digits): ")
                 
            else:
                 if(pass_word.isupper()) == True:
                     print("\nTotal Payment: RM ", final)     
                     
                     con_pay1 = input("\nDo u want to proceed to the confirmation of payment (press 'y' for Yes or 'n' for No): ").lower()
                     while con_pay1 not in option_1:
                        print("\nInvalid input")
                        con_pay1 = input("\nDo u want to proceed to the confirmation of payment (press 'y' for Yes or 'n' for No): ").lower()
                     if con_pay1 == yes:
                           print("\nSecure TAC code has been sent to your mobile phone number via SMS...\n")
                           tac_code1 = int(input("Enter 6-digit secure TAC-Code: "))
                           count_tac1 = (len(str(abs(tac_code1))))
                           while count_tac1 != 6:
                                print("\nInvalid TAC Code, Please try again...")
                                tac_code1 = int(input("\nEnter 6-digit secure TAC-Code: "))
                                count_tac1 = (len(str(abs(tac_code1))))
                                
                           if count_tac1 == 6:
                               print("\nPayment Successful !!!\n")
                               print("We have notified the seller to ship out your order.\n\n")
                               reciept()
                               print("\nWould you help us to review our product?\nThank you! :) ")
                               review()
                               ratings()
                                                           
                     elif con_pay1 == no:
                           print("\nPayment Unsuccessful\n")
                           main()
         
         elif con_secure == 'n':
             pay_2()



#Calling the main function==============================================================================================================================================================    

main()

