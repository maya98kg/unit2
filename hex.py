def to_hex(n):
    if(n<10):
        return n
    elif(n<16):
        return digit(n)
    else:
        result=digit(n//16)+digit(n%16)
        return result

def digit(x):
    if(x<10):
        return str(x)
    elif x==10:
        return 'a'
    elif x==11:
        return 'b'
    elif x==12:
        return 'c'
    elif x==13:
        return 'd'
    elif x==14:
        return 'e'
    else:
        return 'f'

def hex_color(red,green,blue):
    result="#"
    if(red<16):
        result=result+"0"+digit(red)
    else:
        result=result+digit(red//16)+digit(red%16)
    if(green<16):
        result=result+"0"+digit(green)
    else:
        result=result+digit(green//16)+digit(green%16)
    if(blue<16):
        result=result+"0"+digit(blue)
    else:
        result=result+digit(blue//16)+digit(blue%16)
    return result


#print(hex_color(10,32,255))
    