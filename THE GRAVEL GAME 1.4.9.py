import random
from tkinter import *
import time

master = Tk()

print("Welcome to THE GRAVEL GAME (version 1.4.9)")
print("")
print("To see all of your options, you might need to expand your button control area a bit. ;]")
print("")
time.sleep(1.5)


def uiPrint():
    info()
    print("")
    print("your gravel amount is", gravel)
    print("your multiplier is gravel times", mult)
    print("your kindness levels are", kindness)
    blankLine()

def info():
    print("Stock investments: need 10 Gravel! {Warning! May backfire!}")
    print("Gravel press lvl.up purchases: need 15 Gravel!")
    print("ByeBye Money purchases: need 50 Gravel!!")
    #print("Gravel-worker purchases: need 75 Gravel!")
    print("Traveling Salesman hires: need 5 Gravel and 50 kindness.")

info()

gravel = 0
mult = 1
kindness = 0
dcp1 = 0
tonga_time = 0
shrug_counter = 0
tick_tock = 'no'
CFO = "off"
safety_inspector = 250
##5trill_10mill_progress = 0
##worst_progress = 0
##boom_progress = 0
##galactic_progress = 0
    

def blankLine():
    for i in range(20):
        print("")

#if kindness < -999999999999999999999999999999999999999999999999999999999999999999999999999998:
 #   print("You certaninly are mean, huh.")
  #  time.sleep(0.5)
   # print("to just...")
    #print("dump that all onto charity...")
#    time.sleep(5)
 #   while mult == mult:
  #      print("YOU'RE THE WORST!!!!!!!!!!")

#GravelUp
def purchaseGravelUpCommand():
    global gravel
    global mult
    if gravel < 15:
        print("PURCHASE DENIED")
        print("REASONING:")
        print("!!!Not enough Gravel!!!")
        blankLine()
    elif gravel >= 15:
        mult = mult + 2
        gravel = gravel - 15
        print("Gravel press lvl.up Purchased!")
        blankLine()

#Traveling Salesman
def purchaseTravelingSalesCommand():
    global gravel
    global mult
    global kindness
    if gravel < 10:
        print("HIRE DENIED")
        print("REASONING:")
        print("!!!Not enough Gravel!!!")
        blankLine()
    elif gravel >= 5:
        if kindness < 50:
            print("HIRE FAILED")
            print("REASONING:")
            print("!!!Not enough Kindness!!!")
            blankLine()
        elif kindness >= 50:
            mult = mult*1.5
            gravel = gravel - 5
            kindness = kindness - 50
            print("Traveling salesman Hired!")
            blankLine()

#Telemarketer
def purchaseTelemarketerCommand():
    global mult
    global kindness
    if kindness >= 55:
        mult = mult*1.25
        kindness = kindness - 55
        print("Telemarketer Hired!")
        blankLine()

#Charity
def purchaseCharityCommand():
    global gravel
    global mult
    global kindness
    gravel_to_zero = 0
    kindness_Add = gravel / 5
    kindness = kindness + kindness_Add
    if gravel > 0:
        print("Thank you for your donation!!")
        print("your kindness levels are ", kindness,"!")
        gravel = gravel_to_zero
        blankLine()
    elif gravel <= 0:
        if tick_tock == 'no':
            print("Thank you for your donation!!")
            print("...")
            time.sleep(0.5)
            print("ya fithly animal...")
            time.sleep(1.5)
            print("your kindness levels are ", kindness,"...")
            gravel = gravel_to_zero
            blankLine()
        elif tick_tock == 'yes':
            print("YOU CAN'T DO THAT!")
            time.sleep(1)
            print("REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            while tick_tock == 'yes':
                print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")

#Codes
def CodesCommand():
    global gravel
    global mult
    global kindness
    global tonga_time
    global tick_tock
    blankLine()
    code = input("Okay, so, do ya know any codes???")
    if code == "Liam":
        print("congradulations! You typed in the LIAM code!")
        print("You get 129113 Gravel!!!")
        gravel = gravel + 129113
        blankLine()
    elif code == "Simon":
        print("congradulations! You typed in the SIMON code!")
        print("You get 219131514 Gravel!!!")
        gravel = gravel + 219131514
        blankLine()
    elif code == "yes":
        print("boom")
        tonga_time = 1
        blankLine()
    elif code == "Elliot":
        print("congradulations! You typed in the ELLIOT code!")
        print("You get 5121291522 Gravel!!!")
        gravel = gravel + 5121291522
        blankLine()
    elif code == "Stonks":
        print("congradulations! You typed in the STONKS code!")
        print("You get 10 Million Gravel!!!")
        gravel = 10000000
        blankLine()
    elif code == "Universal Paperclips":
        print("congradulations! You typed in the PAPERCLIPS code!")
        print("You get 25 more multipliers!!!")
        mult = mult + 25
        blankLine()
    elif code == "Excel Class":
        print("congradulations! You typed in the EXCEL CLASS code!")
        print("You get 10 more multipliers; 10 more kindness; and 100 more Gravel!!!")
        gravel = gravel + 100
        mult = mult + 10
        kindness = kindness + 10
        blankLine()
    elif code == "Stay in school, kids!":
        print("STAY IN SCHOOL!!!!")
        mult = mult * 2.5
        kindness = kindness * 7.5
    elif code == "tic toc":
        print("no")
        time.sleep(0.5)
        print("no")
        time.sleep(0.5)
        print("no")
        time.sleep(0.5)
        print("no")
        time.sleep(0.5)
        print("no")
        time.sleep(1.5)
        gravel = -99999999999999999999999999999999999999999999999999999999999999999999
        print("Your Gravel is now at", gravel,". How do ya feel.")
        tick_tock = 'yes'
        blankLine()
    elif code == "PAPAYA":
        print("uh-oh...")
        time.sleep(1.25)
        print("OH NO")
        time.sleep(1)
        while gravel == gravel:
            print("P")
            time.sleep(0.25)
            blankLine()
            print("A")
            time.sleep(0.25)
            blankLine()
            print("P")
            time.sleep(0.25)
            blankLine()
            print("A")
            time.sleep(0.25)
            blankLine()
            print("Y")
            time.sleep(0.25)
            blankLine()
            print("A")
            time.sleep(0.25)
            blankLine()
            time.sleep(1)
            print("P")
            time.sleep(0.25)
            print("A")
            time.sleep(0.25)
            print("P")
            time.sleep(0.25)
            print("A")
            time.sleep(0.25)
            print("Y")
            time.sleep(0.25)
            print("A")
            time.sleep(2.125)
            print("PAPAYA")
            time.sleep(0.01)
            print("PAPAYA")
            time.sleep(0.01)
            print("PAPAYA")
            time.sleep(0.01)
            print("PAPAYA")
            time.sleep(0.01)
            print("PAPAYA")
            time.sleep(0.01)
            print("PAPAYA")
            time.sleep(0.01)
            print("PAPAYA")
            time.sleep(0.01)
            print("PAPAYA")
            time.sleep(0.01)
            print("PAPAYA")
            time.sleep(0.01)
            print("PAPAYA")
            time.sleep(0.01)
            print("PAPAYA")
            time.sleep(0.01)
            print("PAPAYA")
            time.sleep(2.5)
            print("   P  A   ")
            print("  A    P  ")
            print("   Y  A   ")
            time.sleep(1)
            blankLine()
    elif code == "Mr.Rayson":
        print("This is a list of codes:")
        print("Mr.Rayson : Shows a list of codes.")
        print("Stonks : Changes gravel to 10000000.")
        print("tic toc : Changes gravel to -99999999999999999999999999999999999999999999999999999999999999999999")
        print("Liam : Gives you 129113 Gravel")
        print("Simon : Gives you 219131514 Gravel")
        print("Elliot : Gives you 5121291522 Gravel")
        print("Universal Paperclips : Adds 25 multipliers.")
        print("Excel Class : Adds 10 multipliers; 10 kindness; and 100 Gravel.")
        print("PAPAYA : i do not dare enter that plane of reality...")
        print("Stay in school, kids! : gives multipliers are multiplied by 2.5; kindness is multiplied by 7.5")
    elif code == "Mr. Rayson":
        print("This is a list of codes:")
        print("Mr.Rayson : Shows a list of codes.")
        print("Stonks : Changes gravel to 10000000.")
        print("tic toc : Changes gravel to -99999999999999999999999999999999999999999999999999999999999999999999")
        print("Liam : Gives you 129113 Gravel")
        print("Simon : Gives you 219131514 Gravel")
        print("Elliot : Gives you 5121291522 Gravel")
        print("Universal Paperclips : Adds 25 multipliers.")
        print("Excel Class : Adds 10 multipliers; 10 kindness; and 100 Gravel.")
        print("PAPAYA : i do not dare enter that plane of reality...")
        print("Stay in school, kids! : gives multipliers are multiplied by 2.5; kindness is multiplied by 7.5")
    else:
        print("OOOOOO, mmmmm, no. You don't get any.")
        print("*throws pop can onto head*")
        time.sleep(1.125)
        blankLine()
            
#shrug
def purchaseShrugCommand():
    global gravel
    global mult
    global kindness
    global shrug_counter
    gravel_to_zero = 0
    print("   __           __")
    print("     \_(' _ ')_/")
    shrug_counter = shrug_counter + 1
    gravel = gravel_to_zero
    tick_tock == 'no'
    time.sleep(0.5)
    blankLine()

#all endings
def purchaseEndingsCommand():
    blankLine()
    global gravel
    global mult
    global kindness
    global shrug_counter
    global tick_tock
    print("Stonks ending:", ((gravel / 10000000) * 100),"% complete.")
    time.sleep(2.5)
    #print("")
    #print("You're the worst ending:", ((kindness / -99999999999999999999999999999999999999999999999999999999999999) * 100),"% complete.")
    #time.sleep(2.5)
    print("")
    print("The big boom ending:", ((gravel / 1300) * 100),"% complete.")
    time.sleep(2.5)
    print("")
    #print("Galactic gravel ending:", ((gravel / 100000000000000) * 100),"% complete.")
    #time.sleep(2.5)
    #26660502140000000000000000000000
    print("Galactic gravel ending:", ((gravel / 26660502140000000000000000000000) * 100),"% complete.")
    time.sleep(2.5)
    print("")
    print("Shrug overload:", ((shrug_counter / 500) * 100),"% complete.")
    time.sleep(2.9)
    print("")
    if tick_tock == 'no':
        print("Lousey donation ending: 0% complete.")
    elif tick_tock == 'yes':
        print("Lousey donation ending: 50% complete.")
    time.sleep(5)
    blankLine()

#ByeByeMoney
def purchaseByeByeMoneyCommand():
    global gravel
    global mult
    if gravel < 50:
        print("PURCHASE DENIED")
        print("REASONING:")
        print("!!!Not enough Gravel!!!")
        blankLine()
    elif gravel >= 50:
        gravel = gravel - 150
        print("ByeBye Money Purchased!")
        blankLine()

#Cheif Financial Officer
def purchaseCFOCommand():
    global gravel
    global CFO
    if CFO == "off":
        if gravel > 271166:
            print("I'm your Cheif Financial Officer:")
            time.sleep(1.25)
            print("Pete!")
            print("Click the button again for a little help when you have some debt!")
            time.sleep(2.5)
            gravel = gravel - 27116
            CFO = "on"
            blankLine()
        else:
            print("HIRE DENIED")
            print("REASONING:")
            print("!!!Not enough Gravel!!!")
            blankLine()
    else:
        if gravel <= -1000:
            print("I'll fix your little debt problem!")
            gravel = 0
            print("Pete: out!")
        else:
            print("You'll be fine; come back when you have more debt!")


#Boom
def purchaseBoomCommand():
    global gravel
    global mult
    if gravel < 1300:
        print("PURCHASE DENIED")
        print("REASONING:")
        print("!!!Not enough Gravel!!!")
        blankLine()
    elif gravel >= 1300:
        gravel = gravel - 1300
        print("your gravel is now at")
        print(gravel)
        time.sleep(1.5)
        print("also, you have a bomb now.")
        explode = input("do you wanna blow it up? (y or n)")
        if explode == "y":
            print("Okay...")
            time.sleep(1.5)
            print("!!!COUNTDOWN_ACTIVATED!!!")
            time.sleep(1.5)
            print("           10 ")
            time.sleep(1)
            print("           9 ")
            time.sleep(1)
            print("           8 ")
            time.sleep(1)
            print("           7 ")
            time.sleep(1)
            print("           6 ")
            time.sleep(1)
            print("          !5!")
            time.sleep(1)
            print("          !4!")
            time.sleep(1)
            print("          !3!")
            time.sleep(1)
            print("          !2!")
            time.sleep(1)
            print("          !1!")
            time.sleep(1.5)
            while explode == "y":
                time.sleep(0.0025)
                print("BOOOOOOOOOM")
        else:
            print("oh, ok")
            blankLine()

#Gravel -5 -to- 5
def purchaseGravel5Command():
    global gravel
    global mult
    if gravel < 500:
        print("PURCHASE ES FALSO")
        print("Razonamiento:")
        print("!!!No Hay Suficiente Grava!!!")
        blankLine()
    elif gravel >= 500:
        print("Complete!")
        gravel = gravel + random.randint(-5,5)
        blankLine()
        
#Safety Inspector
safety_inspector = random.randint(1,500)
if safety_inspector == 1:
    print("Hi, I'm the safety inspector.")
    print("You're all good.")
    time.sleep(1.25)
    mult = mult * 2
    gravel = gravel * 2

#Investments
def purchaseStocksCommand():
    global gravel
    global mult
    if gravel < 10:
        print("INVESTMENT DENIED")
        print("REASONING:")
        print("!!!Not enough Gravel!!!")
        blankLine()
    elif gravel >= 10:
        gravel = gravel + random.randint(-10000,5000)
        print("Stocks Invested!")
        blankLine()
    elif gravel >= 5000:
        gravel = gravel + random.randint(-50000,10000)
        print("Stocks Invested!")
        blankLine()
    elif gravel >= 10000:
        gravel = gravel + random.randint(-100000,50000)
        print("Stocks Invested!")
        blankLine()
    elif gravel >= 50000:
        gravel = gravel + random.randint(-500000,100000)
        print("Stocks Invested!")
        blankLine()
        
#This chunk is for the failed auto clicker button; double '#' section is a seperate option of usage.
#############################################################################################################################################################
##gravel_workers=0 # start workers at 0

##def purchaseGravelWorkerCommand():
 ##   global gravel
  ##  global gravel_workers # declare global
   ## if gravel < 75:
    ##    print("PURCHASE DENIED")
     ##   print("REASONING:")
      ##  print("!!!Not enough Gravel!!!")
       ## blankLine()
    ##else:
     ##   gravel -= 75 # pay for a worker
      ##  print("Gravel-worker purchased!")
       ## gravel_worker += 1 # receive an employee

##def gravel_workers():
 ##   global master
  ##  global gravel
   ## global gravel_workers
    ##gravel += gravel_workers # get clicks from autoclickers
    ##master.after(1000, autoclick) # do this again 1 second later

##gravel_workers() # start benefiting from all existing autoclickers

#def purchaseGravelWorkerCommand():
 #   global gravel
  #  if gravel < 75:
        #print("PURCHASE DENIED")
       # print("REASONING:")
      #  print("!!!Not enough Gravel!!!")
     #   blankLine()
    #elif gravel >= 75:
        #gravel = gravel - 75
        #print("Gravel-worker purchased!")
        #while gravel == gravel:
            #gravel = gravel + 1
            #time.sleep(1)
##################################################################################################################################################################


if gravel > 26660502140000000000000000000000:
    print("...")
    time.sleep(0.1)
    print("")
    print("...")
    time.sleep(0.1)
    print("")
    print("...")
    time.sleep(1.5)
    print("")
    print("How did you even make that much gravel!?")
    time.sleep(0.25)
    print("")
    print("1 piece of gravel is only 0.5 of a centimeter!")
    time.sleep(0.125)
    print("")
    print("The volume of Earth is 1.07BILLION CENTEMETERS!!!!")
    time.sleep(0.5)
    print("")
    print("THE EARTH'S VOLUME IS ONLY 4 BILLION PIECES OF GRAVEL!!!")
    time.sleep(0.5)
    print("")
    print("YOU MADE A FULL SIZED REPLICA OF THE UNIVERSE!")
    time.sleep(0.5)
    print("")
    print("THE UNIVERSE!!!!!!!!")
    time.sleep(1.875)
    while gravel > -99999999999999.9:
        print("WHAT DID YOU DO")

#Get5T for 10M
def purchase5t_10mCommand():
    global gravel
    global mult
    if gravel < 10000000:
        print("PURCHASE DENIED")
        print("REASONING:")
        print("!!!Not enough Gravel!!!")
        blankLine()
    elif gravel >= 10000000:
        gravel =gravel - 10000000
        gravel = gravel + 5000000000000
        print("You have purchaced 5 Trillion gravel for 10 Million!")
        time.sleep(0.25)
        print("Your gravel is now", gravel)
        time.sleep(0.5)
        print("You know what that means...")
        time.sleep(0.25)
        print("...")
        time.sleep(0.25)
        print("...")
        time.sleep(0.25)
        print("...")
        time.sleep(0.25)
        print("...")
        time.sleep(2.5)
        while gravel >= -98765676543456765345676545654345643456543456787654567887654456787634567654345678654345678765434876543456765434567876543456765456787654:
            print("S  T  O  N  K  S")
        blankLine()

def buttonCommand():
    global gravel
    global mult
    gravel += 1*(mult)
    uiPrint()

    if gravel == 252000:
        print('''Rank Unlocked: Gravel Intern!
        BONUS 100 gravel!''')
        gravel += 100
        print("")

    elif gravel == 630000:
        print ('''Rank Unlocked: Professional Gravel maker!
        BONUS 200!''')
        gravel += 300
        print("")

    elif gravel == 1620000:
        print ('''Rank Unlocked: Vice President of GRAVEL co.!
        4x Gravel!''')
        mult = mult * 4
        print("")

    elif gravel == 2520000:
        print ('''Rank Unlocked:  C.E.O of GRAVEL.co!!
        8x GRAVEL!''')
        mult = mult * 8
        print("")

mainGravelButton = Button(master, text="Make Gravel", command = buttonCommand)
mainGravelButton.pack()

purchaseGravelUpButton = Button(master, text="Purchase Gravel press lvl.up", command = purchaseGravelUpCommand)
purchaseGravelUpButton.pack()

#worker
#purchaseGravelWorkerButton = Button(master, text="Purchase Gravel-worker", command = purchaseGravelWorkerCommand)
#purchaseGravelWorkerButton.pack()

purchaseCharityButton = Button(master, text="Donate to Charity!", command = purchaseCharityCommand)
purchaseCharityButton.pack()

purchaseTravelingSales = Button(master, text="Hire a traveling salesman", command = purchaseTravelingSalesCommand)
purchaseTravelingSales.pack()

#purchaseKindGravelButton = Button(master, text="Exchange Kindness for gravel!", command = purchaseKindGravelCommand)
#purchaseKindGravel.pack()

purchaseByeByeMoneyButton = Button(master, text="Purchase ByeBye Money", command = purchaseByeByeMoneyCommand)
purchaseByeByeMoneyButton.pack()

purchaseStocks = Button(master, text="Invest In Stocks", command = purchaseStocksCommand)
purchaseStocks.pack()

purchaseGravel5 = Button(master, text="Make -5 to 5 gravel", command = purchaseGravel5Command)
purchaseGravel5.pack()

#I've been trying to make this thing work for a while now.
#   __            __
#     \_(' _ ')_/

purchaseShrugButton = Button(master, text="shrug", command = purchaseShrugCommand)
purchaseShrugButton.pack()

purchaseBoomButton = Button(master, text="Purchase boom", command = purchaseBoomCommand)
purchaseBoomButton.pack()

purchaseCFOButton = Button(master, text="Hire the Chief Financial Officer", command = purchaseCFOCommand)
purchaseCFOButton.pack()

purchase5t_10mButton = Button(master, text="Purchase 5trillion for 10million!(!!!WARNING: STONKS!!!)", command = purchase5t_10mCommand)
purchase5t_10mButton.pack()

purchaseEndingsButton = Button(master, text="See all endings", command = purchaseEndingsCommand)
purchaseEndingsButton.pack()

#this one should be last
CodesButton = Button(master, text="codes", command = CodesCommand)
CodesButton.pack()

master.title("GRAVEL GAME!")
master.geometry("%sx%s+%s+%s" % (512,512,512,512))
mainloop()
#200,70,512,512
