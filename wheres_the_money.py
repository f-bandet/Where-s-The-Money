### 
### Author: Faye Bandet
### Description: Welcome to Where's The Money! This is a program that helps a user 
###              visualize and understand how much money they spend of various categories of expenditures.
###
from os import _exit as exit

### Greeting statement

print ('-----------------------------')
print ("----- WHERE'S THE MONEY -----")
print ('-----------------------------')

### Checking for numbers
a_s = input ('What is your annual salary? \n')
if a_s.isnumeric() == False:
    print ('Must enter positive integer number.')
    exit (0)
a_s = float (a_s)
m_r = input ('How much is your monthly mortgage/rent? \n')
if m_r.isnumeric() == False:
    print ('Must enter positive integer number.')
    exit (0)
m_r = float (m_r)
b = input ('What do you spend on bills monthly? \n')
if b.isnumeric() == False:
    print ('Must enter positive integer number.')
    exit (0)
b = float (b)
f = input ('What are your weekly grocery/food expenses? \n')
if f.isnumeric() == False:
    print ('Must enter positive integer number.')
    exit (0)
f = float (f)
tr = input ('How much do you spend on travel annually? \n')
if tr.isnumeric() == False:
    print ('Must enter positive integer number.')
    exit (0)
tr = float (tr)
ta = input ('Tax percentage? \n')
if ta.isnumeric() == False:
    print ('Must enter positive integer number.')
    exit (0)
ta = float(ta)

### TAX STATEMENTS
### I added a lowercase x when I transitioned variables.

### Basic input functions
if(ta<100):
    print()
tax = (ta / 100.0) * a_s 
taxx = (tax / a_s) * 100
if ta <0 or ta >100:
    print ('Tax must be between 0% and 100%.')
    exit (0)
m_rx = ((m_r * 12) / a_s) * 100 
bx = ((b * 12) / a_s) * 100
fx = ((f * 52) / a_s) * 100
trx = ((tr) / a_s) * 100
e = (a_s) - (m_r * 12) - (b * 12) - (f * 52) - (tr) - (tax) 
ex = (e / a_s) * 100

### Print the financial break down statement
if m_rx >= bx and m_rx >= fx \
and m_rx >= trx and m_rx >= taxx and m_rx >= ex:
    print ('-' * 41 + '-' * int(m_rx))
if bx >= m_rx and bx >= fx \
and bx >= trx and bx >= taxx and bx >= ex:
    print ('-' * 41 + '-' * int(bx))
if fx >= bx and fx >= m_rx \
and fx >= trx and fx >= taxx and fx >= ex:
    print ('-' * 41 + '-' * int(fx))
if trx >= bx and trx >= fx \
and trx >= m_rx and trx >= taxx and trx >= ex:
    print ('-' * 41 + '-' * int(trx))
if taxx >= bx and taxx >= fx and taxx >= trx \
and taxx >= m_rx and taxx >= ex:
    print ('-' * 41 + '-' * int(taxx))
if ex >= bx and ex >= fx and ex >= trx \
and ex >= trx and ex >= taxx and ex >= m_rx:
    print ('-' * 41 + '-' * int(ex))
print ('See the financial breakdown below, based on a salary of', '$' + format(a_s, '.0f'))
if m_rx >= bx and m_rx >= fx \
and m_rx >= trx and m_rx >= taxx and m_rx >= ex:
    print ('-' * 41 + '-' * int(m_rx))
if bx >= m_rx and bx >= fx \
and bx >= trx and bx >= taxx and bx >= ex:
    print ('-' * 41 + '-' * int(bx))
if fx >= bx and fx >= m_rx \
and fx >= trx and fx >= taxx and fx >= ex:
    print ('-' * 41 + '-' * int(fx))
if trx >= bx and trx >= fx \
and trx >= m_rx and trx >= taxx and trx >= ex:
    print ('-' * 41 + '-' * int(trx))
if taxx >= bx and taxx >= fx and taxx >= trx \
and taxx >= m_rx and taxx >= ex:
    print ('-' * 41 + '-' * int(taxx))
if ex >= bx and ex >= fx and ex >= trx \
and ex >= trx and ex >= taxx and ex >= m_rx:
    print ('-' * 41 + '-' * int(ex))

###formatting
print('| mortgage/rent | $' + format (m_r * 12, '10,.0f'), '|' +
format (m_rx, '6,.1f') + '% |', '#' * int (m_rx))
print('|         bills | $' + format (b * 12, '10,.0f'), '|' +
format (bx, '6,.1f') + '% |', '#' * int (bx))
print('|          food | $' + format (f * 52, '10,.0f'), '|' +
format (fx, '6,.1f') + '% |', '#' * int (fx))
print('|        travel | $' + format (tr, '10,.0f'), '|' +
format (trx, '6,.1f') + '% |', '#' * int (trx))
print('|           tax | $' + format (tax, '10,.1f'), '|' +
format (taxx, '6,.1f') + '% |', '#' * int (taxx))
print('|         extra | $' + format (e, '10,.1f'), '|' +
format (ex, '6,.1f') + '% |', '#' * int (ex))

if m_rx >= bx and m_rx >= fx \
and m_rx >= trx and m_rx >= taxx and m_rx >= ex:
    print ('-' * 41 + '-' * int(m_rx))
if bx >= m_rx and bx >= fx \
and bx >= trx and bx >= taxx and bx >= ex:
    print ('-' * 41 + '-' * int(bx))
if fx >= bx and fx >= m_rx \
and fx >= trx and fx >= taxx and fx >= ex:
    print ('-' * 41 + '-' * int(fx))
if trx >= bx and trx >= fx \
and trx >= m_rx and trx >= taxx and trx >= ex:
    print ('-' * 41 + '-' * int(trx))
if taxx >= bx and taxx >= fx and taxx >= trx \
and taxx >= m_rx and taxx >= ex:
    print ('-' * 41 + '-' * int(taxx))
if ex >= bx and ex >= fx and ex >= trx \
and ex >= trx and ex >= taxx and ex >= m_rx:
    print ('-' * 41 + '-' * int(ex))
    
exit (0)