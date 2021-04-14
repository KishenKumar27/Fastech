###
#/***************************************************
#File Name: dataStoring.py
#Version/Date: v2 (2020-05-06)
#Programmer/ID: Sharveena Padmaraj (1191101614)
#Project Name: Fastech Online Shopping
#Teammates: Kishen , Hari ,Syaqeera
#Course/Term: PSP0201 Mini IT Project (2019/20 T3)
#***************************************************/
###

print("\nPress[1] if you are a Customer") #this site is only for the management
print("\nPress[2] if you are from the Management")


number = int(input("\nEnter Number: "))



    

if  number == 1: #displaying to the customer
    print("\n---------")
    print("WARNING")
    print("---------")
    print("*This page is not available for customers.\n")
    print("*This page is only for the management.\n")
    print("Thank You.")
    
elif number == 2 :  #displayng to the management
  employee_id = int(input("\nEMPLOYEE ID(***Must only contain 10 digits***): "))
  count_id = (len(str(abs(employee_id))))

  while count_id != 10:
      print("\nInvalid Employee ID")
      employee_id = int(input("\nEMPLOYEE ID(***Must only contain 10 digits***): "))
      count_id = (len(str(abs(employee_id))))

  if count_id == 10:
    password = (input("\nPASSWORD: "))
    print("\nLOGIN SUCCESSFULL")
    print("\nFOR A DAY")

    print("--------------------")
    print("ENTER THE NUMBER OF STOCK BOUGHT")
    print("--------------------")

    print("Printers")
    print("--------------------")


    NumberOfCanonimageCLASSLBP6030Bought = int(input(' Canon imageCLASS LBP6030 (Print Only) Mono Laser Printer :')) 
    counter = 0
    sum = 0

    while NumberOfCanonimageCLASSLBP6030Bought >= counter :
        PriceForEachStock = 300
        sum = sum + PriceForEachStock
        SUM1 =  round(sum,2)
        counter = counter + 1
     

        
    print("RM",SUM1)



    NumberOfEpsonEcoTankL3150InkTankPrinterBought = int(input(' Epson EcoTank L3150 Wi-Fi All-in-One Ink Tank Printer :')) 
    counter = 0
    sum = 0

    while NumberOfEpsonEcoTankL3150InkTankPrinterBought >= counter :
        PriceForEachStock = 510
        sum = sum + PriceForEachStock
        SUM2 =  round(sum,2)
        counter = counter + 1
     

        
    print("RM",SUM2)



    NumberOfBROTHERDCPT510WDCPT510WBought = int(input(' BROTHER DCP-T510W DCP T510W 3in1 :')) 
    counter = 0
    sum = 0

    while NumberOfBROTHERDCPT510WDCPT510WBought >= counter :
        PriceForEachStock = 550
        sum = sum + PriceForEachStock
        SUM3 =  round(sum,2)
        counter = counter + 1
     

        
    print("RM",SUM3)




    NumberOfCANONSELPHYCP1300Bought = int(input(' CANON SELPHY CP1300 :')) 
    counter = 0
    sum = 0

    while NumberOfCANONSELPHYCP1300Bought >= counter :
        PriceForEachStock = 500
        sum = sum + PriceForEachStock
        SUM4 =  round(sum,2)
        counter = counter + 1
     

        
    print("RM",SUM4)




    NumberOfHPSPROKETBought = int(input(' HP SPROKET 200 :')) 
    counter = 0
    sum = 0
    while NumberOfHPSPROKETBought >= counter :
        PriceForEachStock = 400
        sum = sum + PriceForEachStock
        SUM5=  round(sum,2)
        counter = counter + 1
     

        
    print("RM",SUM5)




    NumberOfEPSONLQIIBought = int(input(' EPSON LQ-590 II:')) 
    counter = 0
    sum = 0
    while NumberOfEPSONLQIIBought >= counter :
        PriceForEachStock = 1500
        sum = sum + PriceForEachStock
        SUM6=  round(sum,2)
        counter = counter + 1
     

        
    print("RM",SUM6)



    NumberOfHPPrinter2529DeskjetInkAdvantageHomeUsePrinter3in1K7W98ABought = int(input(' HP Printer 2529 Deskjet Ink Advantage Home Use Printer 3 in 1 (K7W98A) :')) 
    counter = 0
    sum = 0
    while NumberOfHPPrinter2529DeskjetInkAdvantageHomeUsePrinter3in1K7W98ABought >= counter :
        PriceForEachStock = 259
        sum = sum + PriceForEachStock
        SUM6i=  round(sum,2)
        counter = counter + 1
     

        
    print("RM",SUM6i)

    print("--------------------")
    print("KEYBOARD")
    print("--------------------")

    print("ENTER THE NUMBER OF STOCK BOUGHT")
    NumberOfRazerCynosaChromaGamingKeyboardBought = int(input('  Razer Cynosa Chroma Gaming Keyboard :')) 
    counter = 0
    sum = 0

    while NumberOfRazerCynosaChromaGamingKeyboardBought >= counter :
        PriceForEachStock = 200
        sum = sum + PriceForEachStock
        SUM7 =  round(sum,2)
        counter = counter + 1
     

        
    print("RM",SUM7)



    NumberOfAULAF2058F2088MechanicalGamingKeyboardBought = int(input('  AULA F2058/F2088 Mechanical Gaming Keyboard :')) 
    counter = 0
    sum = 0

    while NumberOfAULAF2058F2088MechanicalGamingKeyboardBought >= counter :
        PriceForEachStock = 200
        sum = sum + PriceForEachStock
        SUM8 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM8)



    NumberOfFANTECHWK893Bought = int(input('  FANTECH WK-893 :')) 
    counter = 0
    sum = 0

    while NumberOfFANTECHWK893Bought >= counter :
        PriceForEachStock = 80
        sum = sum + PriceForEachStock
        SUM9 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM9)


    NumberOfWireless24GkeyboardMouseSetBought = int(input('  Wireless 2.4G keyboard Mouse Set With Cover mini keypad Mice K-06 Computer Gaming Accessories :')) 
    counter = 0
    sum = 0

    while NumberOfWireless24GkeyboardMouseSetBought >= counter :
        PriceForEachStock = 25
        sum = sum + PriceForEachStock
        SUM9i =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM9i)

    print("--------------------")
    print("MONITOR")
    print("--------------------")

    NumberOfHP24y238FullHD60HzIPSMonitorBought = int(input('  HP 24y 23.8" Full HD 60Hz IPS Monitor :')) 
    counter = 0
    sum = 0

    while NumberOfHP24y238FullHD60HzIPSMonitorBought >= counter :
        PriceForEachStock = 420
        sum = sum + PriceForEachStock
        SUM10 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM10)



    NumberOfXiaomi34InchUltrawidemonitor2k144hzBought = int(input('  Xiaomi 34 Inch Ultrawide monitor 2k 144hz :')) 
    counter = 0
    sum = 0

    while NumberOfXiaomi34InchUltrawidemonitor2k144hzBought >= counter :
        PriceForEachStock = 2170
        sum = sum + PriceForEachStock
        SUM11 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM11)



    NumberOfBenQEW278027inchHDRiScreenBought = int(input(' BenQ EW2780 27 inch HDRi Screen :')) 
    counter = 0
    sum = 0

    while NumberOfBenQEW278027inchHDRiScreenBought >= counter :
        PriceForEachStock = 810
        sum = sum + PriceForEachStock
        SUM12 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM12)


    NumberOfCurved75HzFHDLEDMonitorultrathinHDHDMIBought = int(input(' Curved 75Hz FHD LED Monitor ultra-thin surface HD HDMI Super Slim And Sleek Design Filter bluray :')) 
    counter = 0
    sum = 0

    while NumberOfCurved75HzFHDLEDMonitorultrathinHDHDMIBought >= counter :
        PriceForEachStock = 370
        sum = sum + PriceForEachStock
        SUM12i =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM12i)


    print("--------------------")
    print("MOUSE")
    print("--------------------")

    NumberOfLogitechM330SilentMouseBought = int(input(' Logitech® M330 Silent Mouse :')) 
    counter = 0
    sum = 0

    while NumberOfLogitechM330SilentMouseBought >= counter :
        PriceForEachStock = 50
        sum = sum + PriceForEachStock
        SUM13 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM13)




    NumberOfAULAS20GamingMouseBought = int(input(' AULA S20 Gaming Mouse :')) 
    counter = 0
    sum = 0

    while NumberOfAULAS20GamingMouseBought >= counter :
        PriceForEachStock = 40
        sum = sum + PriceForEachStock
        SUM14 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM14)




    NumberOfRazerDeathAdderEliteGamingMouseBought = int(input(' Razer DeathAdder Elite Gaming Mouse :')) 
    counter = 0
    sum = 0

    while NumberOfRazerDeathAdderEliteGamingMouseBought >= counter :
        PriceForEachStock = 259
        sum = sum + PriceForEachStock
        SUM15 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM15)




    NumberOfHPX3000WIRELESSBought = int(input(' HP X3000 WIRELESS :')) 
    counter = 0
    sum = 0

    while NumberOfHPX3000WIRELESSBought >= counter :
        PriceForEachStock = 40
        sum = sum + PriceForEachStock
        SUM16 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM16)




    NumberOfGAMINGFREAKRGBBought = int(input('AVF GAMING FREAK RGB :')) 
    counter = 0
    sum = 0

    while NumberOfGAMINGFREAKRGBBought >= counter :
        PriceForEachStock = 70
        sum = sum + PriceForEachStock
        SUM17 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM17)




    NumberOfLOGITECHM590BTBought = int(input(' LOGITECH M590 B/T :')) 
    counter = 0
    sum = 0

    while NumberOfLOGITECHM590BTBought >= counter :
        PriceForEachStock = 100
        sum = sum + PriceForEachStock
        SUM18 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM18)


    NumberOfLogitechG103ProdigyGamingMouse910005481Bought = int(input(' Logitech G103 Prodigy Gaming Mouse 910-005481 :')) 
    counter = 0
    sum = 0

    while NumberOfLogitechG103ProdigyGamingMouse910005481Bought >= counter :
        PriceForEachStock = 30
        sum = sum + PriceForEachStock
        SUM18i =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM18i)

    print("--------------------")
    print("PROCESSOR")
    print("--------------------")

    NumberOfInteli53470320GhzProcessorBought = int(input(' Intel i5 3470 3.20 Ghz Processor  :')) 
    counter = 0
    sum = 0

    while NumberOfInteli53470320GhzProcessorBought >= counter :
        PriceForEachStock = 200
        sum = sum + PriceForEachStock
        SUM19 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM19)





    NumberOfInteli53470320GhzProcessorBought = int(input(' Intel Core i7 8700K  :')) 
    counter = 0
    sum = 0

    while NumberOfInteli53470320GhzProcessorBought >= counter :
        PriceForEachStock = 1470
        sum = sum + PriceForEachStock
        SUM20 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM20)




    NumberOfIntelCorei59600Bought = int(input('  Intel Core i5 9600  :')) 
    counter = 0
    sum = 0

    while NumberOfIntelCorei59600Bought >= counter :
        PriceForEachStock = 900
        sum = sum + PriceForEachStock
        SUM21 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM21)




    NumberOfAMDRyzen93900XBought = int(input('  AMD Ryzen™ 9 3900X :')) 
    counter = 0
    sum = 0

    while NumberOfAMDRyzen93900XBought >= counter :
        PriceForEachStock = 2000
        sum = sum + PriceForEachStock
        SUM22 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM22)




    NumberOfIntelCorei710700TProcessorBought = int(input(' Intel® Core™ i7-10700T Processor  :')) 
    counter = 0
    sum = 0

    while NumberOfIntelCorei710700TProcessorBought >= counter :
        PriceForEachStock = 910
        sum = sum + PriceForEachStock
        SUM23 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM23)




    NumberOfIntelXeonD1602ProcessorBought = int(input(' Intel® Xeon® D-1602 Processor :')) 
    counter = 0
    sum = 0

    while NumberOfIntelXeonD1602ProcessorBought >= counter :
        PriceForEachStock = 1900
        sum = sum + PriceForEachStock
        SUM24 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM24)



    NumberOfIntelCOREi59400FProcessorBought = int(input(' Intel CORE™ i5-9400F Processor (9M Cache, up to 4.10 GHz, LGA 1151, W/O GPU) :')) 
    counter = 0
    sum = 0

    while NumberOfIntelCOREi59400FProcessorBought >= counter :
        PriceForEachStock = 620
        sum = sum + PriceForEachStock
        SUM24i =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM24i)


    print("--------------------")
    print("SUPPLY UNIT")
    print("--------------------")

    NumberOfSupplyUnitPSUPB500Bought = int(input(' Supply Unit PSU (PB500) :')) 
    counter = 0
    sum = 0

    while NumberOfSupplyUnitPSUPB500Bought >= counter :
        PriceForEachStock = 150
        sum = sum + PriceForEachStock
        SUM25 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM25)



    NumberOfCoolerMasterMWATTLITEBought = int(input(' Cooler Master M.WATT LITE :')) 
    counter = 0
    sum = 0

    while NumberOfCoolerMasterMWATTLITEBought >= counter :
        PriceForEachStock = 230
        sum = sum + PriceForEachStock
        SUM26 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM26)



    NumberOfThermaltakeSMARTPRORGBBought = int(input(' Thermaltake SMART PRO RGB :')) 
    counter = 0
    sum = 0

    while NumberOfThermaltakeSMARTPRORGBBought >= counter :
        PriceForEachStock = 310
        sum = sum + PriceForEachStock
        SUM27 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM27)



    NumberOfArmaggeddonVoltronGold475RGBPowerSupplyUnitBought = int(input(' Armaggeddon Voltron Gold 475 RGB Power Supply Unit with RGB Silent Fan :')) 
    counter = 0
    sum = 0

    while NumberOfArmaggeddonVoltronGold475RGBPowerSupplyUnitBought >= counter :
        PriceForEachStock = 100
        sum = sum + PriceForEachStock
        SUM27i =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM27i)



    print("--------------------")
    print("RAM")
    print("--------------------")

    NumberOfKingstonValueRAM8GBramBought = int(input(' Kingston ValueRAM 8GB (ram) :')) 
    counter = 0
    sum = 0

    while NumberOfKingstonValueRAM8GBramBought >= counter :
        PriceForEachStock = 110
        sum = sum + PriceForEachStock
        SUM28 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM28)




    NumberOfKingstonD4Predator32002XRGB16GBBought = int(input(' Kingston D4 Predator 3200 2X RGB 16GB :')) 
    counter = 0
    sum = 0

    while NumberOfKingstonD4Predator32002XRGB16GBBought >= counter :
        PriceForEachStock = 370
        sum = sum + PriceForEachStock
        SUM29 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM29)




    NumberOfCorsairD4VG3200C16RGBPRO2X32BGBought = int(input(' Corsair D4 VG 3200 C16 RGB PRO 2X 32BG :')) 
    counter = 0
    sum = 0

    while NumberOfCorsairD4VG3200C16RGBPRO2X32BGBought >= counter :
        PriceForEachStock = 720
        sum = sum + PriceForEachStock
        SUM30 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM30)



    NumberOfKingstonHyperXFURY8GBDDR42400Mhz2666Mhz288PinPC4DIMMRAMBought = int(input(' Kingston HyperX FURY 8GB DDR4 2400Mhz/2666Mhz 288Pin PC4 DIMM RAM Desktop Memory :')) 
    counter = 0
    sum = 0

    while NumberOfKingstonHyperXFURY8GBDDR42400Mhz2666Mhz288PinPC4DIMMRAMBought >= counter :
        PriceForEachStock = 110
        sum = sum + PriceForEachStock
        SUM30i =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM30i)


    print("--------------------")
    print("SSD")
    print("--------------------")

    NumberOfIntel545sSeries128GBBought = int(input(' Intel 545s Series 128GB :')) 
    counter = 0
    sum = 0

    while NumberOfIntel545sSeries128GBBought >= counter :
        PriceForEachStock = 100
        sum = sum + PriceForEachStock
        SUM31 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM31)




    NumberOfKingstonHyperXSavage240GBBought = int(input(' Kingston HyperX Savage 240GB :')) 
    counter = 0
    sum = 0

    while NumberOfKingstonHyperXSavage240GBBought >= counter :
        PriceForEachStock = 350
        sum = sum + PriceForEachStock
        SUM32 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM32)





    NumberOfAdataAdataSX8200M2PCIENVME240GBBought = int(input(' Adata Adata SX-8200 M.2 PCIE NVME 240GB :')) 
    counter = 0
    sum = 0

    while NumberOfAdataAdataSX8200M2PCIENVME240GBBought >= counter :
        PriceForEachStock = 200
        sum = sum + PriceForEachStock
        SUM33 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM33)



    NumberOfA400SATASSDin25andM2FormFactorsBought = int(input(' A400 SATA SSD in 2.5" and M.2 Form Factors :')) 
    counter = 0
    sum = 0

    while NumberOfA400SATASSDin25andM2FormFactorsBought >= counter :
        PriceForEachStock = 100
        sum = sum + PriceForEachStock
        SUM33i =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM33i)




    NumberOfSAMSUNG970PRONVMeM2SSD1TBBought = int(input('  SAMSUNG 970 PRO NVMe M.2 SSD 1TB :')) 
    counter = 0
    sum = 0

    while NumberOfSAMSUNG970PRONVMeM2SSD1TBBought >= counter :
        PriceForEachStock = 720
        sum = sum + PriceForEachStock
        SUM34 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM34)



    NumberOfAPACERAS340PANTHERSATAIIISSDBought = int(input('  APACER AS340 PANTHER SATA III SSD :')) 
    counter = 0
    sum = 0

    while NumberOfAPACERAS340PANTHERSATAIIISSDBought >= counter :
        PriceForEachStock = 100
        sum = sum + PriceForEachStock
        SUM35 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM35)



    NumberOfSeagateFastExternalSSDFastSSDPortableSolidStateDriveBought = int(input('  Seagate Fast External SSD 2TB/1TB/500GB/250GB Fast SSD USB-C Portable Solid State Drive  :')) 
    counter = 0
    sum = 0

    while NumberOfSeagateFastExternalSSDFastSSDPortableSolidStateDriveBought >= counter :
        PriceForEachStock = 220
        sum = sum + PriceForEachStock
        SUM35i =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM35i)



    print("--------------------")
    print("COOLING FAN")
    print("--------------------")

    NumberOfThermaltakeRiingPlusTTPremiumEdition12RGB5packBought = int(input(' Thermaltake Riing Plus TT Premium Edition(12 RGB 5 pack) :')) 
    counter = 0
    sum = 0

    while NumberOfThermaltakeRiingPlusTTPremiumEdition12RGB5packBought >= counter :
        PriceForEachStock = 510
        sum = sum + PriceForEachStock
        SUM36 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM36)




    NumberOfCoolerMasterML360RRGBBought = int(input(' Cooler Master ML360R RGB :')) 
    counter = 0
    sum = 0

    while NumberOfCoolerMasterML360RRGBBought >= counter :
        PriceForEachStock = 440
        sum = sum + PriceForEachStock
        SUM37 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM37)



    NumberOfCorsairHYDROH100iPROPLTBought = int(input(' Corsair HYDRO H100i PRO PLT :')) 
    counter = 0
    sum = 0

    while NumberOfCorsairHYDROH100iPROPLTBought >= counter :
        PriceForEachStock = 550
        sum = sum + PriceForEachStock
        SUM38 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM38)

    print("--------------------")
    print("MOTHERBOARD")
    print("--------------------")


    NumberOfMicroATXMotherboardBought = int(input(' Micro-ATX Motherboard :')) 
    counter = 0
    sum = 0

    while NumberOfMicroATXMotherboardBought >= counter :
        PriceForEachStock = 210
        sum = sum + PriceForEachStock
        SUM39 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM39)



    NumberOfMSIB450MPROM2V2Bought = int(input(' MSI B450M PRO-M2 V2 :')) 
    counter = 0
    sum = 0

    while NumberOfMSIB450MPROM2V2Bought >= counter :
        PriceForEachStock = 280
        sum = sum + PriceForEachStock
        SUM40 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM40)




    NumberOfASUSPRIMEB450MKBought = int(input(' ASUS PRIME B450M-K :')) 
    counter = 0
    sum = 0

    while NumberOfASUSPRIMEB450MKBought >= counter :
        PriceForEachStock = 310
        sum = sum + PriceForEachStock
        SUM40i =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM40i)



    NumberOfGIGABYTEB450AORUSEliteGAMINGMOTHERBOARDAM4Bought = int(input(' GIGABYTE B450 AORUS Elite GAMING MOTHERBOARD (AM4) :')) 
    counter = 0
    sum = 0

    while NumberOfGIGABYTEB450AORUSEliteGAMINGMOTHERBOARDAM4Bought >= counter :
        PriceForEachStock = 400
        sum = sum + PriceForEachStock
        SUM41 =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM41)


    print("--------------------")
    print("CPU COOLERS")
    print("--------------------")

    NumberOfCoolerMasterMasterLiquidML120RML240RML360RRGBCPUBought = int(input(' Cooler Master MasterLiquid ML120R/ML240R/ML360R RGB All-in-One CPU Liquid Cooler :')) 
    counter = 0
    sum = 0

    while NumberOfCoolerMasterMasterLiquidML120RML240RML360RRGBCPUBought >= counter :
        PriceForEachStock = 380
        sum = sum + PriceForEachStock
        SUM41i =  round(sum,2)
        counter = counter + 1
        
        
    print("RM",SUM41i)




    print("---------------------------------------------------------------------")


    print("\n\n\n--------------------")
    print("ENTER THE NUMBER OF STOCK SOLD")
    print("--------------------")
    print("Printers")
    print("--------------------")

    NumberOfCanonimageCLASSLBP6030Sold = int(input(' Canon imageCLASS LBP6030 (Print Only) Mono Laser Printer :')) 
    counter = 0
    sum = 0

    while NumberOfCanonimageCLASSLBP6030Sold >= counter :
        PriceForEachStock = 312
        sum = sum + PriceForEachStock
        total1 =  round(sum,2)
        counter = counter + 1
     

        
    print("RM",total1)



    NumberOfEpsonEcoTankL3150InkTankPrinterSold = int(input(' Epson EcoTank L3150 Wi-Fi All-in-One Ink Tank Printer :')) 
    counter = 0
    sum = 0

    while NumberOfEpsonEcoTankL3150InkTankPrinterSold >= counter :
        PriceForEachStock = 569
        sum = sum + PriceForEachStock
        total2 =  round(sum,2)
        counter = counter + 1
     

        
    print("RM",total2)



    NumberOfBROTHERDCPT510WDCPT510WSold = int(input(' BROTHER DCP-T510W DCP T510W 3in1 :')) 
    counter = 0
    sum = 0

    while NumberOfBROTHERDCPT510WDCPT510WSold >= counter :
        PriceForEachStock = 589
        sum = sum + PriceForEachStock
        total3 =  round(sum,2)
        counter = counter + 1
     

        
    print("RM",total3)




    NumberOfCANONSELPHYCP1300Sold = int(input(' CANON SELPHY CP1300 :')) 
    counter = 0
    sum = 0

    while NumberOfCANONSELPHYCP1300Sold >= counter :
        PriceForEachStock = 540
        sum = sum + PriceForEachStock
        total4 = round(sum,2)
        counter = counter + 1
     

        
    print("RM",total4)




    NumberOfHPSPROKETSold = int(input(' HP SPROKET 200 :')) 
    counter = 0
    sum = 0
    while NumberOfHPSPROKETSold >= counter :
        PriceForEachStock = 439
        sum = sum + PriceForEachStock
        total5= round(sum,2)
        counter = counter + 1
     

        
    print("RM",total5)




    NumberOfEPSONLQIISold = int(input(' EPSON LQ-590 II:')) 
    counter = 0
    sum = 0
    while NumberOfEPSONLQIISold >= counter :
        PriceForEachStock = 1600
        sum = sum + PriceForEachStock
        total6= round(sum,2)
        counter = counter + 1
     

        
    print("RM",total6)



    NumberOfHPPrinter2529DeskjetInkAdvantageHomeUsePrinter3in1K7W98ASold = int(input(' HP Printer 2529 Deskjet Ink Advantage Home Use Printer 3 in 1 (K7W98A) :')) 
    counter = 0
    sum = 0
    while NumberOfHPPrinter2529DeskjetInkAdvantageHomeUsePrinter3in1K7W98ASold >= counter :
        PriceForEachStock = 299
        sum = sum + PriceForEachStock
        total6i= round(sum,2)
        counter = counter + 1
     

        
    print("RM",total6i)

    print("--------------------")
    print("KEYBOARD")
    print("--------------------")


    NumberOfRazerCynosaChromaGamingKeyboardSold = int(input('  Razer Cynosa Chroma Gaming Keyboard :')) 
    counter = 0
    sum = 0

    while NumberOfRazerCynosaChromaGamingKeyboardSold >= counter :
        PriceForEachStock = 239
        sum = sum + PriceForEachStock
        total7 = round(sum,2)
        counter = counter + 1
     

        
    print("RM",total7)



    NumberOfAULAF2058F2088MechanicalGamingKeyboardSold = int(input('  AULA F2058/F2088 Mechanical Gaming Keyboard :')) 
    counter = 0
    sum = 0

    while NumberOfAULAF2058F2088MechanicalGamingKeyboardSold >= counter :
        PriceForEachStock = 219
        sum = sum + PriceForEachStock
        total8 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total8)



    NumberOfFANTECHWK893Sold = int(input('  FANTECH WK-893 :')) 
    counter = 0
    sum = 0

    while NumberOfFANTECHWK893Sold >= counter :
        PriceForEachStock = 89
        sum = sum + PriceForEachStock
        total9 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total9)


    NumberOfWireless24GkeyboardMouseSetSold = int(input('  Wireless 2.4G keyboard Mouse Set With Cover mini keypad Mice K-06 Computer Gaming Accessories :')) 
    counter = 0
    sum = 0

    while NumberOfWireless24GkeyboardMouseSetSold >= counter :
        PriceForEachStock = 39.61
        sum = sum + PriceForEachStock
        total9i = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total9i)

    print("--------------------")
    print("MONITOR")
    print("--------------------")

    NumberOfHP24y238FullHD60HzIPSMonitorSold = int(input('  HP 24y 23.8" Full HD 60Hz IPS Monitor :')) 
    counter = 0
    sum = 0

    while NumberOfHP24y238FullHD60HzIPSMonitorSold >= counter :
        PriceForEachStock = 439
        sum = sum + PriceForEachStock
        total10 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total10)



    NumberOfXiaomi34InchUltrawidemonitor2k144hzSold = int(input('  Xiaomi 34 Inch Ultrawide monitor 2k 144hz :')) 
    counter = 0
    sum = 0

    while NumberOfXiaomi34InchUltrawidemonitor2k144hzSold >= counter :
        PriceForEachStock = 2199
        sum = sum + PriceForEachStock
        total11 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total11)



    NumberOfBenQEW278027inchHDRiScreenSold = int(input(' BenQ EW2780 27 inch HDRi Screen :')) 
    counter = 0
    sum = 0

    while NumberOfBenQEW278027inchHDRiScreenSold >= counter :
        PriceForEachStock = 829
        sum = sum + PriceForEachStock
        total12i = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total12i)


    NumberOfCurved75HzFHDLEDMonitorultrathinHDHDMISold = int(input(' Curved 75Hz FHD LED Monitor ultra-thin surface HD HDMI Super Slim And Sleek Design Filter bluray :')) 
    counter = 0
    sum = 0

    while NumberOfCurved75HzFHDLEDMonitorultrathinHDHDMISold >= counter :
        PriceForEachStock = 398
        sum = sum + PriceForEachStock
        total12 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total12)


    print("--------------------")
    print("MOUSE")
    print("--------------------")

    NumberOfLogitechM330SilentMouseSold = int(input(' Logitech® M330 Silent Mouse :')) 
    counter = 0
    sum = 0

    while NumberOfLogitechM330SilentMouseSold >= counter :
        PriceForEachStock = 71
        sum = sum + PriceForEachStock
        total13 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total13)




    NumberOfAULAS20GamingMouseSold = int(input(' AULA S20 Gaming Mouse :')) 
    counter = 0
    sum = 0

    while NumberOfAULAS20GamingMouseSold >= counter :
        PriceForEachStock = 51.90
        sum = sum + PriceForEachStock
        total14 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total14)




    NumberOfRazerDeathAdderEliteGamingMouseSold = int(input(' Razer DeathAdder Elite Gaming Mouse :')) 
    counter = 0
    sum = 0

    while NumberOfRazerDeathAdderEliteGamingMouseSold >= counter :
        PriceForEachStock = 279
        sum = sum + PriceForEachStock
        total15 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total15)




    NumberOfHPX3000WIRELESSSold = int(input(' HP X3000 WIRELESS :')) 
    counter = 0
    sum = 0

    while NumberOfHPX3000WIRELESSSold >= counter :
        PriceForEachStock = 70
        sum = sum + PriceForEachStock
        total16 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total16)




    NumberOfGAMINGFREAKRGBSold = int(input('AVF GAMING FREAK RGB :')) 
    counter = 0
    sum = 0

    while NumberOfGAMINGFREAKRGBSold >= counter :
        PriceForEachStock = 100
        sum = sum + PriceForEachStock
        total17 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total17)




    NumberOfLOGITECHM590BTSold = int(input(' LOGITECH M590 B/T :')) 
    counter = 0
    sum = 0

    while NumberOfLOGITECHM590BTSold >= counter :
        PriceForEachStock = 129
        sum = sum + PriceForEachStock
        total18 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total18)


    NumberOfLogitechG103ProdigyGamingMouse910005481Sold = int(input(' Logitech G103 Prodigy Gaming Mouse 910-005481 :')) 
    counter = 0
    sum = 0

    while NumberOfLogitechG103ProdigyGamingMouse910005481Sold >= counter :
        PriceForEachStock = 65.50
        sum = sum + PriceForEachStock
        total18i = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total18i)

    print("--------------------")
    print("PROCESSOR")
    print("--------------------")

    NumberOfInteli53470320GhzProcessorSold = int(input(' Intel i5 3470 3.20 Ghz Processor  :')) 
    counter = 0
    sum = 0

    while NumberOfInteli53470320GhzProcessorSold >= counter :
        PriceForEachStock = 229
        sum = sum + PriceForEachStock
        total19 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total19)





    NumberOfInteli53470320GhzProcessorSold = int(input(' Intel Core i7 8700K  :')) 
    counter = 0
    sum = 0

    while NumberOfInteli53470320GhzProcessorSold >= counter :
        PriceForEachStock = 1559
        sum = sum + PriceForEachStock
        total20 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total20)




    NumberOfIntelCorei59600Sold = int(input('  Intel Core i5 9600  :')) 
    counter = 0
    sum = 0

    while NumberOfIntelCorei59600Sold >= counter :
        PriceForEachStock = 659
        sum = sum + PriceForEachStock
        total21 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total21)




    NumberOfAMDRyzen93900XSold = int(input('  AMD Ryzen™ 9 3900X :')) 
    counter = 0
    sum = 0

    while NumberOfAMDRyzen93900XSold >= counter :
        PriceForEachStock = 2100
        sum = sum + PriceForEachStock
        total22 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total22)




    NumberOfIntelCorei710700TProcessorSold = int(input(' Intel® Core™ i7-10700T Processor  :')) 
    counter = 0
    sum = 0

    while NumberOfIntelCorei710700TProcessorSold >= counter :
        PriceForEachStock = 960
        sum = sum + PriceForEachStock
        total23 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total23)




    NumberOfIntelXeonD1602ProcessorSold = int(input(' Intel® Xeon® D-1602 Processor :')) 
    counter = 0
    sum = 0

    while NumberOfIntelXeonD1602ProcessorSold >= counter :
        PriceForEachStock = 2000
        sum = sum + PriceForEachStock
        total24 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total24)



    NumberOfIntelCOREi59400FProcessorSold = int(input(' Intel CORE™ i5-9400F Processor (9M Cache, up to 4.10 GHz, LGA 1151, W/O GPU) :')) 
    counter = 0
    sum = 0

    while NumberOfIntelCOREi59400FProcessorSold >= counter :
        PriceForEachStock = 669
        sum = sum + PriceForEachStock
        total24i = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total24i)


    print("--------------------")
    print("SUPPLY UNIT")
    print("--------------------")

    NumberOfSupplyUnitPSUPB500Sold = int(input(' Supply Unit PSU (PB500) :')) 
    counter = 0
    sum = 0

    while NumberOfSupplyUnitPSUPB500Sold >= counter :
        PriceForEachStock = 199
        sum = sum + PriceForEachStock
        total25 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total25)



    NumberOfCoolerMasterMWATTLITESold = int(input(' Cooler Master M.WATT LITE :')) 
    counter = 0
    sum = 0

    while NumberOfCoolerMasterMWATTLITESold >= counter :
        PriceForEachStock = 279
        sum = sum + PriceForEachStock
        total26 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total26)



    NumberOfThermaltakeSMARTPRORGBSold = int(input(' Thermaltake SMART PRO RGB :')) 
    counter = 0
    sum = 0

    while NumberOfThermaltakeSMARTPRORGBSold >= counter :
        PriceForEachStock = 349
        sum = sum + PriceForEachStock
        total27 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total27)



    NumberOfArmaggeddonVoltronGold475RGBPowerSupplyUnitSold = int(input(' Armaggeddon Voltron Gold 475 RGB Power Supply Unit with RGB Silent Fan :')) 
    counter = 0
    sum = 0

    while NumberOfArmaggeddonVoltronGold475RGBPowerSupplyUnitSold >= counter :
        PriceForEachStock = 129
        sum = sum + PriceForEachStock
        total27i = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total27i)



    print("--------------------")
    print("RAM")
    print("--------------------")

    NumberOfKingstonValueRAM8GBramSold = int(input(' Kingston ValueRAM 8GB (ram) :')) 
    counter = 0
    sum = 0

    while NumberOfKingstonValueRAM8GBramSold >= counter :
        PriceForEachStock = 167
        sum = sum + PriceForEachStock
        total28 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total28)




    NumberOfKingstonD4Predator32002XRGB16GBSold = int(input(' Kingston D4 Predator 3200 2X RGB 16GB :')) 
    counter = 0
    sum = 0

    while NumberOfKingstonD4Predator32002XRGB16GBSold >= counter :
        PriceForEachStock = 419
        sum = sum + PriceForEachStock
        total29 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total29)




    NumberOfCorsairD4VG3200C16RGBPRO2X32BGSold = int(input(' Corsair D4 VG 3200 C16 RGB PRO 2X 32BG :')) 
    counter = 0
    sum = 0

    while NumberOfCorsairD4VG3200C16RGBPRO2X32BGSold >= counter :
        PriceForEachStock = 759
        sum = sum + PriceForEachStock
        total30 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total30)



    NumberOfKingstonHyperXFURY8GBDDR42400Mhz2666Mhz288PinPC4DIMMRAMSold = int(input(' Kingston HyperX FURY 8GB DDR4 2400Mhz/2666Mhz 288Pin PC4 DIMM RAM Desktop Memory :')) 
    counter = 0
    sum = 0

    while NumberOfKingstonHyperXFURY8GBDDR42400Mhz2666Mhz288PinPC4DIMMRAMSold >= counter :
        PriceForEachStock = 110
        sum = sum + PriceForEachStock
        total30i = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total30i)


    print("--------------------")
    print("SSD")
    print("--------------------")

    NumberOfIntel545sSeries128GBSold = int(input(' Intel 545s Series 128GB :')) 
    counter = 0
    sum = 0

    while NumberOfIntel545sSeries128GBSold >= counter :
        PriceForEachStock = 149
        sum = sum + PriceForEachStock
        total31 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total31)




    NumberOfKingstonHyperXSavage240GBSold = int(input(' Kingston HyperX Savage 240GB :')) 
    counter = 0
    sum = 0

    while NumberOfKingstonHyperXSavage240GBSold >= counter :
        PriceForEachStock = 389
        sum = sum + PriceForEachStock
        total32 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total32)





    NumberOfAdataAdataSX8200M2PCIENVME240GBSold = int(input(' Adata Adata SX-8200 M.2 PCIE NVME 240GB :')) 
    counter = 0
    sum = 0

    while NumberOfAdataAdataSX8200M2PCIENVME240GBSold >= counter :
        PriceForEachStock = 230
        sum = sum + PriceForEachStock
        total33 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total33)



    NumberOfA400SATASSDin25andM2FormFactorsSold = int(input(' A400 SATA SSD in 2.5" and M.2 Form Factors :')) 
    counter = 0
    sum = 0

    while NumberOfA400SATASSDin25andM2FormFactorsSold >= counter :
        PriceForEachStock = 120
        sum = sum + PriceForEachStock
        total33i = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total33i)




    NumberOfSAMSUNG970PRONVMeM2SSD1TBSold = int(input('  SAMSUNG 970 PRO NVMe M.2 SSD 1TB :')) 
    counter = 0
    sum = 0

    while NumberOfSAMSUNG970PRONVMeM2SSD1TBSold >= counter :
        PriceForEachStock = 765
        sum = sum + PriceForEachStock
        total34 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total34)



    NumberOfAPACERAS340PANTHERSATAIIISSDSold = int(input('  APACER AS340 PANTHER SATA III SSD :')) 
    counter = 0
    sum = 0

    while NumberOfAPACERAS340PANTHERSATAIIISSDSold >= counter :
        PriceForEachStock = 120
        sum = sum + PriceForEachStock
        total35 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total35)



    NumberOfSeagateFastExternalSSDFastSSDPortableSolidStateDriveSold = int(input('  Seagate Fast External SSD 2TB/1TB/500GB/250GB Fast SSD USB-C Portable Solid State Drive  :')) 
    counter = 0
    sum = 0

    while NumberOfSeagateFastExternalSSDFastSSDPortableSolidStateDriveSold >= counter :
        PriceForEachStock = 255
        sum = sum + PriceForEachStock
        total35i = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total35i)



    print("--------------------")
    print("COOLING FAN")
    print("--------------------")

    NumberOfThermaltakeRiingPlusTTPremiumEdition12RGB5packSold = int(input(' Thermaltake Riing Plus TT Premium Edition(12 RGB 5 pack) :')) 
    counter = 0
    sum = 0

    while NumberOfThermaltakeRiingPlusTTPremiumEdition12RGB5packSold >= counter :
        PriceForEachStock = 539
        sum = sum + PriceForEachStock
        total36 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total36)




    NumberOfCoolerMasterML360RRGBSold = int(input(' Cooler Master ML360R RGB :')) 
    counter = 0
    sum = 0

    while NumberOfCoolerMasterML360RRGBSold >= counter :
        PriceForEachStock = 489
        sum = sum + PriceForEachStock
        total37 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total37)



    NumberOfCorsairHYDROH100iPROPLTSold = int(input(' Corsair HYDRO H100i PRO PLT :')) 
    counter = 0
    sum = 0

    while NumberOfCorsairHYDROH100iPROPLTSold >= counter :
        PriceForEachStock = 599
        sum = sum + PriceForEachStock
        total38 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total38)

    print("--------------------")
    print("MOTHERBOARD")
    print("--------------------")


    NumberOfMicroATXMotherboardSold = int(input(' Micro-ATX Motherboard :')) 
    counter = 0
    sum = 0

    while NumberOfMicroATXMotherboardSold >= counter :
        PriceForEachStock = 259
        sum = sum + PriceForEachStock
        total39 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total39)



    NumberOfMSIB450MPROM2V2Sold = int(input(' MSI B450M PRO-M2 V2 :')) 
    counter = 0
    sum = 0

    while NumberOfMSIB450MPROM2V2Sold >= counter :
        PriceForEachStock = 310
        sum = sum + PriceForEachStock
        total40 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total40)




    NumberOfASUSPRIMEB450MKSold = int(input(' ASUS PRIME B450M-K :')) 
    counter = 0
    sum = 0

    while NumberOfASUSPRIMEB450MKSold >= counter :
        PriceForEachStock = 359
        sum = sum + PriceForEachStock
        total40i = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total40i)



    NumberOfGIGABYTEB450AORUSEliteGAMINGMOTHERBOARDAM4Sold = int(input(' GIGABYTE B450 AORUS Elite GAMING MOTHERBOARD (AM4) :')) 
    counter = 0
    sum = 0

    while NumberOfGIGABYTEB450AORUSEliteGAMINGMOTHERBOARDAM4Sold >= counter :
        PriceForEachStock = 435
        sum = sum + PriceForEachStock
        total41 = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total41)


    print("--------------------")
    print("CPU COOLERS")
    print("--------------------")

    NumberOfCoolerMasterMasterLiquidML120RML240RML360RRGBCPUSold = int(input(' Cooler Master MasterLiquid ML120R/ML240R/ML360R RGB All-in-One CPU Liquid Cooler :')) 
    counter = 0
    sum = 0

    while NumberOfCoolerMasterMasterLiquidML120RML240RML360RRGBCPUSold >= counter :
        PriceForEachStock = 415
        sum = sum + PriceForEachStock
        total41i = round(sum,2)
        counter = counter + 1
        
        
    print("RM",total41i)







    print("\n\n\n--------------------")
    print("SUMMARY OF THE DAY")    
    print("--------------------")
    SUM = SUM1 + SUM2 + SUM3 + SUM4 + SUM5 + SUM6 + SUM6i + SUM7 + SUM8 + SUM9 + SUM9i + SUM10 + SUM11 + SUM12 + SUM12i + SUM13 + SUM14 + SUM15 + SUM16 + SUM17 + SUM18 + SUM18i + SUM19 +SUM20 + SUM21 + SUM22 + SUM23 + SUM24 + SUM24i + SUM25 + SUM26 + SUM27 + SUM27i + SUM28 +SUM29 + SUM30 + SUM30i + SUM31 + SUM32 + SUM33 + SUM33i + SUM34 + SUM35 + SUM35i + SUM36 + SUM37 + SUM38 + SUM39 +SUM40 + SUM40i + SUM41 + SUM41i
    total = total1 +  total2 +  total3 +  total4 +  total5 +  total6 +  total6i +  total7 +  total8 +  total9 +  total9i +  total10 +  total11 +  total12 +  total12i + total13 +  total14 + total15 +  total16 +  total17 +  total18 +  total18i +  total19 + total20 +  total21 +  total22 +  total23 +  total24 +  total24i +  total25 +  total26 +  total27 +  total27i +  total28 +  total29 +  total30 +  total31 +  total32 +  total33 +  total33i +  total34 + total35 +  total36 +  total37 +  total38  +  total39 +  total40 +  total40i +  total41 +  total41i         

    Sum = round(SUM,2)
    Total = round(total,2)

    print("\nTotal stock bought = RM",Sum)
    print("\nTotal stock sold to customrs = RM",Total)

    profit = (total) - (SUM) #total profit for the day
    profit1 = round(profit,2)
    print("\nProfit of the day = RM",profit1)

    if profit > 0:
        print("\nCompany Made Profit")
        
    else :
        print("\nCompany did not make profit")
