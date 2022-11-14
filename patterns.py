''' * 
    * * 
    * * * 
    * * * * 
    * * * * * '''
n=int(input("Enter Number of Rows : "))
for i in range(0, n):
     for j in range(0, i+1):
          print("*",end= " ")
     print()
   
'''      * 
        * * 
       * * * 
      * * * * 
     * * * * * '''
n=int(input("Enter Number of Rows : "))
c = n - 1
for i in range(0, n):
     for t in range(0, c):
          print(end=" ")
     c = c - 1
     for t in range(0, i+1):
          print("* ", end="")
     print(" ")
    
''' 1 
    1 2 
    1 2 3 
    1 2 3 4 
    1 2 3 4 5 '''
num_input = int(input("Enter the Starting Number : "))
n=int(input("Enter Number of Rows : "))
for i in range(0, n):
     num=num_input
     for j in range(0, i+1):
          print(num, end=" ")
          num = num + 1
     print()
    
''' A 
    A B 
    A B C 
    A B C D 
    A B C D E '''
alph=input("Enter the Starting Letter : ")
num_user = ord(alph)
n=int(input("Enter Number of Rows : "))
for i in range(0, n):
     num=num_user
     for j in range(0, i+1):
          ch = chr(num)
          print(ch, end=" ")
          num = num + 1
     print()
  
''' 5 4 3 2 1 
    4 3 2 1 
    3 2 1 
    2 1 
    1        '''
n = int(input("Enter Number of Rows : "))
for i in range(0, n + 1):
    for j in range(n - i, 0, -1):
        print(j, end=' ')
    print()
    
''' 1 2 3 4 5 
    2 2 3 4 5 
    3 3 3 4 5 
    4 4 4 4 5 
    5 5 5 5 5  '''
n = int(input("Enter the Number of Columns/Rows : "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()
   
''' *****
    ****
    ***
    **
    *   '''
n=int(input("What number of '*' do you want to begin with ? "))
for i in range (n,0,-1):
    for a in range (1,i+1):
        print("*", end="")
    else :
        print()

'''
            *             
            *             
            *             
            *             
    * * * * * * * * * 
            *             
            *             
            *             
            *             
'''
rows = int(input("Enter Desired Number of Rows for the Pattern : "))
c = 1
while(c < rows*2):
    r = 1
    while(r < rows*2):
        if c == rows or r == rows:
            print('* ', end = '')
        else:
            print('  ', end = ' ')
        r = r + 1
    c = c + 1
    print("")

'''
 *  *  *  *  *  *  *  *  *  * 
 *                          * 
 *                          * 
 *                          * 
 *                          * 
 *                          * 
 *                          * 
 *                          * 
 *                          * 
 *  *  *  *  *  *  *  *  *  *
 '''
no_of_rows = int(input("Input the number of rows required for the pattern : "))
print()
for i in range(no_of_rows):
    for j in range(no_of_rows):
        if(i == 0 or i == no_of_rows - 1 or j==0 or j == no_of_rows -1):
            print(' * ', end = '')
        else:
            print('    ', end = '')
    print()

'''
  *    *    *    *    *  
  *    *         *    *  
  *         *         *  
  *    *         *    *  
  *    *    *    *    * 
'''
no_of_rows = int(input("Input the number of rows required for the pattern : "))
print()
for i in range(no_of_rows):
    for j in range(no_of_rows):
        if(i==j or i == 0 or i == no_of_rows - 1 or j == (no_of_rows - 1 - i) or j==0 or j == no_of_rows -1):
            print('  *  ', end = '')
        else:
            print('      ', end = '')
    print()

"""
*       *
 *     * 
  *   *  
   * *   
    *    
   * *   
  *   *  
 *     * 
*       *
"""
rows = int(input("Enter X Pattern Odd Rows = "))

print("X Star Pattern") 

for i in range(0, rows):
    for j in range(0, rows):
        if(i == j or j == rows - 1 - i):
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
