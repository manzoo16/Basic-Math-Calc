#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print ('\033[1;31m============================================\033[1;m\n')
print('''\033[1;34m##     ##     ##   ##    ##  #######  #####\033[1;m''')
print('''\033[1;34m#### ####   ## ##  ####  ##    ###   #     #\033[1;m''')
print('''\033[1;34m## ##  ##  ####### ##  ####  ###     #     #\033[1;m''')
print('''\033[1;34m##     ## ##    ## ##    ## #######   #####\033[1;m''')
print ('\033[1;31m============================================\033[1;m\n')
print("   Python Math Operator")
print ('\033[1;31m  ======================\033[1;m\n')
print('\033[1;31m   Author:   Technical Manzoo\033[1;m\n')
print('\033[1;31m   Github:   Manzoo16\033[1;m\n')
print('\033[1;31m   Telegram: @TechnicalManzoo\033[1;m\n')
print('\033[1;31m   Web:      jajabtech.tk\033[1;m\n')
print("\033[1;32m[1] Addition\033[1;32m");
print("\033[1;32m[2] Subtraction\033[1;32m");
print("\033[1;32m[3] Multiplication\033[1;32m");
print("\033[1;32m[4] Division\033[1;32m");
print("[5] Exit");
choice = int(input("Enter your choice: "));
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
    print("See You Soon, Bye")
    print('==================')
else:
    print("Wrong input..!!");
