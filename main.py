from os import system
system("clear")
xnum = 0
ynum = 0
coal = 5
coin = 10
food = 12
coord = "0:0"
locations = {"1:0":"solitude","-2:1":"coal mine"}
currentloc = "nowhere"
#print("  -> Input Test")
#print("you wake up in a folding cot. you find the ashes of a recent campfire lying on the ground. it is the start of another great day as an adventurer. you think to yourself that you should probably start planning for today's adventure. you are still in bed. try to 'get up' now.")
#while True:
#  print()
#  act = input(" -")
#  if act == "help":
#    print("you need to 'get up' now.")
#  elif act == "get up":
#    print("you get up out of bed. you are ready to start your day.")
#    break
#  elif act == "sleep":
#    print("you let your eyes shut, and you sleep.")
#    print()
#    print("that was a rather bold response, by the way. you needed to 'get up'.")
#    exit()

while True:
  print()
  act = input(" -")

  if act == "help":
    print("commands are as following:")
    print(" move: sets which direction you are going for the day.")
    print(" map: use your map to find certain locations like settlements, mines, and lakes.")
    print(" sextant: use your sextant to determine your location.")
    print(" inventory: check your inventory")
    print(" help: lists off commands you can use")
    print("coordinates are shown as X:Y.")
    
    if currentloc == "solitude":
      print(" use move and coordinates 0,0 to stay in solitude.")
  
  elif act == "move":
    x = input("X: ")
    y = input("Y: ")
    try:
      if not( int(x)==1 or int(x)==-1 or int(x)==0 ):
        print("bad x coordinate")
        continue
      if not( int(y)==1 or int(y)==-1 or int(y)==0 ):
        print("bad y coordinate")
        continue

      xnum = xnum + int(x)
      ynum = ynum + int(y)

      if coord == str(xnum) + ":" + str(ynum):
        
        if currentloc == "solitude":
          print("you return to the inn for the night. you can pay for a night in the inn, which would cost 2 coins. do you want to rent a room?")
          
          while True:
            print()
            act = input(" y/n:")
            if act == "y":
              
              if coin < 2:
                print("you do not have enough money. you decide to set up camp outside the village for the night.")
              
              else:
                print("you purchase a room for the night.")
                print("your room comes with a free meal, so you order and sit at a table.")
                print("your food arrives not long after. you eat your meal, and join the rest of the people at the bar.")
                print("the menu has the following options:")
                print("  -water: free!")
                print("  -lemonade: free! (suggested for your kids)")
                print("  -beer: 2 coins")
                print()
                print(" other options include 'leave' and 'talk'")
                print()
                drinks_per_session = 0

                while True:
                  if drinks_per_session > 2:
                    print("you are feeling tipsy. you need to stop drinking beer.")

                  act = input(" -")
                  
                  if act == "water":
                    print("you order up a glass of water. you drink it.")
                  
                  elif act == "lemonade":
                    print("you order up a glass of lemonade. it is a rather sweet lemonade, with a bit of sour. you drink it.")
                  
                  elif act == "beer":
                    
                    if drinks_per_session < 4:
                      print("you ask the bartender to get you a beer.")
                    
                      if coin > 2:
                        print("you pay 2 coins, and drink the beer.")
                        coin = coin - 2
                        drinks_per_session = drinks_per_session + 1

                      else:
                        print("you do not have enough money.")

                    else:
                      print("you have had enough beer for tonight...")
                  elif act == "leave":
                    print("you decide to leave the bar.")
                    break
                  
                  else:
                    print("the menu has the following options:")
                    print("  -water: free!")
                    print("  -lemonade: free! (suggested for your kids)")
                    print("  -beer: 1 coin")
                    print()
                    print(" other options include 'leave' and 'talk'")
                    print()
                break
            
            elif act == "n":
              print("you decide to just set up camp outside the village.")
              print("you set up your cot.")
              print("you sleep.")
            
            else:
              print("answer as 'y' or 'n'")
          
          else:
            print("you go homeless for the night.")
        
        else:
          print("you stay at the camp for the night.")
          print("you set up your cot and sleep.")
          continue
      
      coord = str(xnum) + ":" + str(ynum)
      if coord in locations:
        print("location " + coord + " found")
        print("location name is " + locations[coord])
        currentloc = locations[coord]
      
      else:
        print("location " + coord + " is empty.")
        currentloc = "nowhere"
      
      print("you pack your things. you head for " + locations[coord] + " and get there by sunset.")
      
      if locations[coord] == "solitude":
        print("you are welcomed into solitude by the villagers, who lead you to an inn, where they give you food and a bed for the night.")
        print("you sleep.")
        print()
        print("you wake up. you head into the streets after packing your stuff. ")
      
      else:
        print("you set up camp when you get there.")
        print("")
    
    except:
      print("bad input")
      continue
  
  elif act == "map":
    print("your map tells you ")
    for i in locations:
      print(i + " ( " + locations[i] + " )")
  
  elif act == "sextant":
    print("you are at " + coord)
    print("you are in " + currentloc)
  
  elif act == "inventory":
    print("you have " + str(coal) + " lumps of coal")
    print("you have " + str(coin) + " coins")
    print("you have " + str(food) + " meals")
