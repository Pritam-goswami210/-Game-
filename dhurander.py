#dhurandher 
def dhurandhar():
    i = True 
    while i == True :
        print("\nAvailable roles are:-\n'Hamza Ali Mazari' , 'Major Iqbal'")
        asking_user_char  = input("what dou you want to play as a --> ") .title().strip()
        
        if asking_user_char == "Hamza Ali Mazari":
            print("<----select your mission------>")
            mission1 = input("(LEVEL:-EASY)  \nFacing uzair baloch after his brother's death--> ")
            mission2 = input("(LEVEL:-- MEDIUM)\nFacing SP chaudihiry aslam after you betrayed him  ---> ")
            mission3 = input("(LEVEL:-- HARD)\nTaking over KARACHI-->")
            if mission1 == "yes":
                print("OK")
                print("your mission starts from now")
                print("your main target is to gain Uzair baloche's trust ")
                trust = 100   
                option_for_mainchar_mission_1= { 1 : "nothing will happen uzair ",
                                       2 : "i know who has killed him ",
                                       3 : "we will kill that chaudhiry!!!" }
                uzair = {  1 :"uzair:- 'we wll kill that person who has killed my brotheer!!!!'",
                         2 : "uzair:- 'so you know who killed my  brother'",
                         3:   "uzair:- 'how do you know the SP haz killed my brother,because no one was there'"}

                print("Uzair is crying because of his brothers death ")
                print("you have to maintain uzair's trust if the level reaches 25 he will catch you")
                
                # Print the options first to the screen
                print("\nOptions are:-")
                print(f"1: {option_for_mainchar_mission_1[1]}")
                print(f"2: {option_for_mainchar_mission_1[2]}")
                print(f"3: {option_for_mainchar_mission_1[3]}")
                
                # Take the input cleanly
                talk1 = input("\nWrite which option you want to take (1/2/3): ")
                if talk1 == "1" : 
                    print(uzair[1])
                    print("trust level:---",trust)
                    print("you have succeccfully maintained the  trust level")
                    print("________D__O__N__E________")
                elif talk1 == "2" :
                    print(uzair[2])
                    print("trust level :--",trust-50)
                    print("uzair is douting you now stay safe")
                    print("________D__O__N__E________")
                elif talk1 == "3":
                    print(uzair[3])
                    print("trust leval:--",trust-80)
                    print("uzair has killed you")
                    print("--------DEAD----------\n--G_A_M_E ---O_V_E_R--")
                else:
                    print("wrong option entered")
        elif mission2 == "yes":
            
            sp = {1:"why you have betrayed me",
                  2:"so you have another plan???",
                  3:"now what is your next plan",
                  4:" i will killll youuuuuuu 'Hamza'!!!!!",
                  5:"so you want to kill him on another place" }

            char_choice = {1:"it was not right time ",
                           2:"i have better plan ",
                           3:"i will kill  him in froest ",
                          }
            print("OK")
            print("your mission starts from now\nyou have to lower down his anger level ,if it reaches to 80 he willl kill you")
            anger_level = 50
            
            print(sp[1],anger_level)
            talk2 = input("your options are :--",char_choice[1],char_choice[2],char_choice[3])
            if talk2 == "1":
                print("it wasss",anger_level+30)
                print("--------DEAD----------\n--G_A_M_E ---O_V_E_R--")
            elif talk2 == "2":
                print("what was problem in that problem??",anger_level+10)
                print("saty alert because he  can kill you at any time because he is angry")
                print("________D__O__N__E________")
            elif talk2 == "3":
                print("you has waste my time",anger_level+80)
                print("--------DEAD----------\n--G_A_M_E ---O_V_E_R--")
        elif mission3 == "yes":
            print()


                

dhurandhar()