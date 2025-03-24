# Print all numbers from 1 to 100 using a  for  loop.
for i in range(1,101):
    print(i);

#write a program to display the multiplication table of a given number. First 20 
number=int(input('enter a number'));
for i in range(1,21):
    you=number*i;
    print(you);

#print all even numbers between 1 and 50 using a  while loop.
i=1;
while(i<50):
    if(i%2==0):
        print(i);
    i+=1;

#write a program to print the sum of the first  n  natural numbers. (n*n+1/ 2) 
naturalnumbers=0;
for i in range(1,101):
    naturalnumbers+=i;
print(naturalnumbers);


#reverse a number using a  while  loop. 1.  Also can we get the sum of all the digits. 
reverse_number = input('Enter a number: ');
new_number = "";
newest_number = 0;
i = 0;
while i < len(reverse_number):
    new_number = reverse_number[i] + new_number;
    newest_number += int(reverse_number[i]);
    i += 1;
print(new_number);
print(newest_number);

#write a program to count the number of digits in a given number using a  while  loop. 
digit=input('enter a number');
i=1;
while(i==1):
 print(len(digit));
 i+=1;

#write a program that keeps asking the user to enter numbers until they enter a negative number. Use a  while  loop. 
while(True):
    
        user=int(input('enter a number'));
        if(user<0):
          break;
    