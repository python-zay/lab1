#!/usr/bin/env python
# coding: utf-8

# In[10]:


### ONE (A) This command will be initiated in Python progamming language
print ('Hello world')


# In[12]:


### ONE (B) The command will be initiated in Java progamming language
public class Main {
  public static void main(String[] args) {
    System.out.println("Hello, World!");
  }
}
### The results were "invalid syntax"


# In[13]:


### ONE (C) The command will be initiated in C# progamming language
using System;

namespace Program 
{
    public class Program
    { 
        public static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
    }
}
### The results were "invalid syntax"


# In[15]:


### ONE (D) The command will be initiated in C++ progamming language
#include <iostream>

int main()
{
  std::cout << "Hello, World!\n";
  return 0;
}
### The results were "invalid syntax"


# In[18]:


### TWO This command displays my name in Python progamming language
print('Isaiah Joseph Allen')


# In[22]:


### THREE This command will display my name with empty spaces
print('I s a i a h')
### Not sure if this was what step 3 implied


# In[23]:


### FOUR (A) Calculate the length of these strings:
string = "Python"
print(len(string))
### length calculated is 6


# In[24]:


### FOUR (B) Calculate the length of these strings:
string = "My favorite number is nine."
print(len(string))
### length calculated is 27


# In[27]:


### FOUR (C) Calculate the length of these strings:
string = "In 2022, Python 3.10.4 and 3.9.12 were expedited and so were older releases
including 3.8.13, and 3.7.13 because of many security issues in 2022. Python
3.9.13 is the latest 3.9 version, and from now on 3.9 (and older; 3.8 and 3.7) will
only get security updates."
print(len(string))
### Error while trying to calculate the length of the string


# In[30]:


### FIVE (A) Calculate the following operations without using math methods. Use the built-in
mathematical functions on Python.
9988870 * 303


# In[31]:


### FIVE (B)
34199820 / 2121.4


# In[32]:


### FIVE (C)
9988870 + 34199820 + 2121.4


# In[33]:


### FIVE (D)
9988870 + 34199820 + 2121.4 / 2


# In[34]:


### FIVE (E)
130 + 45 - 12 / 98 * 2


# In[35]:


### FIVE (F)
332403650 - 332524270


# In[36]:


### SIX (D) I am organizing a hackathon. I have 325 participants and want to create teams of 6
## students. How many complete teams do I have, and how many participants will
# work in a team with fewer participants?

325 / 6
### You can make a total of 54 whole teams


# In[38]:


### SEVEN (A)
import math
print(math.log(10))


# In[39]:


### SEVEN (B)
import math
print(math.sqrt(255))


# In[40]:


### SEVEN (C)
import math
math.gcd(200,25)


# In[42]:


### SEVEN (D)
import math
math.remainder(325,6)
### not sure if this is the correct method but it would be correct as one participant would be working alone


# In[43]:


### EIGHT Evaluate if these statements are true or false. Please # Write the result in a
## comment under the script.
89 == 7


# In[44]:


332433240365003633240365050 != 332433240365003633240365050


# In[45]:


332433240365003633240365050 == 332433240365003633240365050


# In[46]:


89 > 89


# In[47]:


89 > 89


# In[48]:


89 == 89


# In[49]:


89 != ‘89’
### Syntax error


# In[51]:


True == True


# In[53]:


True == ‘True’
### Syntax error


# In[54]:


‘Hello World!’ == ‘Hello World!’
### Syntax error


# In[61]:


### TEN Display a text by using string concatenation. Use at least one number in number
## format and convert it into a string.

string = "I have "
int = "2 "
string2 = "apples."

print(string + int  + string2)
### The result is "I have 2 apples"


# In[ ]:


# This progam says hello and asks for my name but its not really me 

print('Hello, world!')
print ('What us your name?')
myName = input()
print('It is not good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year ')


# In[ ]:




