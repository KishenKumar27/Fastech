###
#/***************************************************
#File Name: customerServices.py
#Version/Date: V4 (2020/05/15)
#Programmer/ID: HARRI GANESH A/L G CHANDRA BOSE (1191100277)
#Project Name: Fastech Online Shopping
#Teammates: Kishen Kumar A/L Sivalingam , SHARVEENA A/P PADMARAJ , NURUL SYAQEERA BINTI ISMAIL 
#Course/Term: PSP0201 Mini IT Project (2019/20 T3)
#***************************************************/
###


def Communication():
    str = 'Customer Services'
    print (str.center(160,'='))
    print ('\nHere some of methods you can contact us\n')
    print ('If you prefer to contact us press   = 1\n')
    print ('If you prefer to Chat with us press = 2\n')
    Communication = int(input("Which method do you prefer to contact us ? =   "))

    if int(Communication) < 3:
        if  Communication  == 1:
            Contact()       
        elif Communication == 2:
            Chatbot()               
        else: 
            print('\nINVALID INPUT\n')
            Communication()
    else:
        Communication()

    
def Contact():
    print('\n|---------------------------------------------------------------------------|')
    print('|                        USE THIS METHODS TO CONTACT US                     |')
    print('|---------------------------------------------------------------------------|')
    print('|CALL    |Kindly call us on this number 0172859305 for further assistance   |')
    print('|---------------------------------------------------------------------------|')
    print('|MESSAGE |Kindly Message us on this number 0172859305 for further assistance|')
    print('|---------------------------------------------------------------------------|')
    print('|EMAIL   |Kindly Email us at denvormigo@gmail.com                           |')
    print('|---------------------------------------------------------------------------|\n')
    Continue = input("If you want to chat with us, then Enter 'Y' YES and 'N' for NO return to main menu = ").lower()
    if Continue == 'y':
        Chatbot()
    elif Continue == 'n':
        print()
        Communication()
    else:
        print('\nInvalid input')
        Contact()

    
    



def Chatbot():
        Chatbox = input('\nPlease Enter you name =  ')
        print(f'\n ** Hi {Chatbox} **\n')
        print(f'How may I help you today? I can answer these common questions for you MR/MRS.{Chatbox} \n')
        print('Order status and Tracking                                    =  1\n')
        print('About my refunds                                             =  2\n')
        print('Can I cancel my order ?                                      =  3\n')
        print('How to cancel my order ?                                     =  4\n')
        print('How to pay with credit card or debit card ?                  =  5\n')
        print('How do I place an order ?                                    =  6\n')
        print('Will I recieve receipt after done payment ?                  =  7\n')
        print('Where can I review or rates about this products or services? =  8\n')
        print('How much does it costs for shipping fees?                    =  9\n')
        Chatbot =  int(input(f"{Chatbox}, if you have any problems regarding this common problems, Please Enter a number according to your problem as mentioned above =  "))
        if Chatbot == 1:
            Status = input("\n WHERE IS MY ORDER ? If this is your problem, then Enter 'Y' YES and 'N' for NO return to main menu = ").lower()
            if Status == 'y':
                print('\n Please check you account for more details about your orders to get full details and current progress.')

            elif Status == 'n':
                Communication()
            else:
                print('\nInvalid input')
        elif Chatbot == 2:
            Refund = input("\n WHERE IS MY REFUND ? If this is your problem, then Enter Enter 'Y' YES and 'N' for NO return to main menu = ").lower()
            if Refund == 'y':
                print('\n There is no Returns yet. Please check for the updates.')
            elif Refund == 'n':
                Communication() 
            else:
                print('\nInvalid input')
        elif Chatbot == 3:
            order = input("\n Can I cancel my Order ? If this is your problem, then Enter 'Y' YES and 'N' for NO return to main menu = ").lower()
            if order == 'y':
                print('\n YES, you can.However, is only allowed if the appoinment had not been confirmed.')
            elif order == 'n':
                Communication()
            else:
                print('\nInvalid input')
        elif Chatbot == 4:
            Cancellation = input("\nHow to cancel my Order ? If this is your problem, then Enter 'Y' YES and 'N' for NO return to main menu = ").lower()
            if Cancellation == 'y':
                print('\nSelect the order you want to cancel in shopping cart and check your inbox for confirmation.')
            elif order == 'n':
                Communication()
            else:
                print('\nInvalid input')
        elif Chatbot == 5:
            card = input("\nHow to pay with credit card or debit card ? If this is your problem, then Enter 'Y' YES and 'N' for NO return to main menu = ").lower()
            if card == 'y':
                print('\nWhen making payment for your item, under "Payment Methods" choose credit card or debit to pay for your item.')
            elif card == 'n':
                Communication()
            else:
                print('\nInvalid input')
        elif Chatbot == 6:
            procedure = input("\nHow do I place an order ?  If this is your problem, then Enter 'Y' YES and 'N' for NO return to main menu = ").lower()
            if procedure == 'y':
                print('Step 1 Choose your products.\n')
                print('Step 2 Check prodcut information.\n')
                print('Step 3 Confirm your product and add into shopping cart.\n')
                print('Step 4 Provide your delivery information.\n')
                print('Step 5 Choose your paymnet method.\n')
                print('Step 6 Place your order.\n')
                print('Step 7 Receive order confirmation or receipt.\n')
                print('Step 8 Review and Rates our prodcuts and services.\n')
                print('Your Order will deliver to you soon as possible.\n')
            elif procedure == 'n':
                Communication()
            else:
                print('\nInvalid input')
        elif Chatbot == 7:
            receipt = input("\nWill I recieve receipt after done payment ?  If this is your problem, then Enter 'Y' YES and 'N' for NO return to main menu = ").lower()
            if receipt == 'y':
                print('\nYes. You will receive the receipt after you make the payment. It will be an E-Receipt.')
            elif receipt== 'n':
                Communication()
            else:
                print('\nInvalid input')
        elif Chatbot == 8:
            review = input("\nWhere can I review or rates about this products or services?  If this is your problem, then Enter 'Y' YES and 'N' for NO return to main menu = ").lower()
            if review == 'y':
                print('\nYou can rate or review once you finish shopping or after make the payment.')
            elif receipt == 'n':
                Communication()
            else:
                print('\nInvalid input')
        elif Chatbot == 9:
            shipping = input("\nHow much does it costs for shipping fees?  If this is your problem, then Enter 'Y' YES and 'N' for NO return to main menu = ").lower()
            if shipping == 'y':
                print('\nFastech providing free shipping and it is totaly free for the customers.')
            elif shipping == 'n':
                Communication()
            else:
                print('\nInvalid input')
        else:
            print('\nInvalid input')
            Communication()
            

                      
Communication()
