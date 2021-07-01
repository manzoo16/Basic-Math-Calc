def main(): 

    print ('\033[31m============================================\033[1;m\n')
    print('''\033[1;34m##     ##     ##   ##    ##  #######  #####\033[1;m''')
    print('''\033[1;34m#### ####   ## ##  ####  ##    ###   #     #\033[1;m''')
    print('''\033[1;34m## ##  ##  ####### ##  ####  ###     #     #\033[1;m''')
    print('''\033[1;34m##     ## ##    ## ##    ## #######   #####\033[1;m''')
    print ('\033[1;31m============================================\033[1;m\n')
    print("   Python Math Operator")
    print ('\033[1;31m  ======================\033[1;m\n')
    print('\033[2;31;43m   Author:   Technical Manzoo')
    print('\033[2;31;43m   Github:   Manzoo16')
    print('\033[1;31m   Telegram: @TechnicalManzoo\033[1;m')
    print('\033[1;31m   Youtube:  MLC Technical\033[1;m')
    print('\033[1;31m   Web:      jajabtech.tk\033[0;0m\n')
    print("\033[1;32m[1] ADDITION\033[1;32m");
    print("\033[1;32m[2] SUBTRACTION\033[1;32m");
    print("\033[1;32m[3] MULTIPLICATION\033[1;32m");
    print("\033[1;32m[4] DIVISION\033[1;32m");
    print("[5]\033[1;31m Exit\033[1;m\n");
   
    choice = int(input("\033[1;32mEnter your choice: \033[1;32m"));
    if (choice>=1 and choice<=4):
        print("\033[36mEnter two numbers: \033[36m");
        num1 = int(input());
        num2 = int(input());
        if choice == 1:
    	    res = num1 + num2;
    	    print('==================')
    	    print("Result = ", res);
    	    print('==================')  	
        elif choice == 2:
    	    res = num1 - num2;
    	    print('==================')
    	    print("Result = ", res);
    	    print('==================')
        elif choice == 3:
    	    res = num1 * num2;
    	    print('==================')
    	    print("Result = ", res);
    	    print('==================')
        else:
    	    res = num1 / num2;
    	    print('==================')
    	    print("Result = ", res);
    	    print('==================')
    elif choice == 5:
        print('==================')
        print("Thank you for using this program. Bye!");
    else:
        print("\033[1;31mWrong input..!!\033[1;m\n");
    
        restart = input("\033[36mDo you want to restart again? Type Yes and press enter\033[36m\n");
        if restart == "Yes":
        	main()
        else:
           print("Bye")
           exit();
       
main()
       
        
        