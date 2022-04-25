def calculation(cal_out,x,y):
    
    if cal_out == 'A':
        return x + y
    
    elif cal_out  == 'S':
        return x - y
    
    elif cal_out  == 'M':
        return x * y
    
    elif cal_out  == 'D':
        return x / y
    
cal_out = input('Select : ')
two_Input = input("x, y Input Data: ").split(' ')

print("Result: ", calculation(cal_out, x, y ))