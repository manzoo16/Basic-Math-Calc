#!/usr/bin/env python
# coding: utf-8

# In[ ]:


number_one = input('Enter the first number: ')
number_two = input('Enter the second number: ')
number_one = int(number_one)
number_two = int(number_two)
print ('\033[1;31m---------------------------------------------\033[1;m\n')
print('''\033[1;34m##     ##     ##   ##    ##  #######  #####\033[1;m''')
print('''\033[1;34m#### ####   ## ##  ####  ##    ###   #     #\033[1;m''')
print('''\033[1;34m## ##  ##  ####### ##  ####  ###     #     #\033[1;m''')
print('''\033[1;34m##     ## ##    ## ##    ## #######   #####\033[1;m''')
print ('\033[1;31m---------------------------------------------\033[1;m\n')
print('The Manzoo program calculating Result.... ')
print('''\033[1;34mPlease Wait..........\033[1;m''')
print('###########################################')
result = number_one * number_two
print ('The Result is: ' + str(result))
    
number_three = input('Enter the third number: ')
number_four = input('Enter the fourth number: ')
number_three = int(number_three)
number_four = int(number_four)
print('The program calculationg, please wait...')
result = number_three * number_four
print('The Result is: ' + str(result))
