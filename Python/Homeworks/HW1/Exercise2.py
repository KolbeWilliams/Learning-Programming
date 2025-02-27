count = 0 #used to record term number
pi = 0.0 #used as the vaule of pi in the current term
sign = 1 #used to determine wether to add or subtract in the sequence
denominator = 1 #used as the denominator of each term
control = 1 #used as the value of pi in each term carried out to 4 decimal places
while(control != 3.1415):
    print("Term", count, end = '') 
    print(':', pi)
    if(sign % 2 == 1):
        pi += (4 / denominator)
    else:
        pi -= (4 / denominator)
    denominator += 2
    sign += 1
    count += 1
    control = int(pi * 10000)
    control /= 10000
print("Term", count, end = '') 
print(':', pi)
print(count, 'terms in the series must be used to get 3.1415')
#It takes 10794 terms in the series to get to 3.1415