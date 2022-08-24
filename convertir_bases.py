
digit2Value = { "0":0, "1":1, "2": 2, "3":3, "4":4,
                "5":5, "6":6, "7":7, "8":8, "9":9, 
                "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

def is_number_base_x( number, base ):
    split_number = number.split(".")

    # Validation, is a number in base X???
    result = True
    for part in split_number:
        for digit in part:
            if not ( 0<= digit2Value[digit] < base ):
                result = False
                break
        if not result:
            break

        return result

def baseX_to_base10( number , base ):
    split_number = number.split(".")
    # display and compute numeric expansion
    print("\nExpansion in power series: \n\t",end="")

    # integer part
    integer_part = 0
    max_exponent = len(split_number[0]) - 1
    for i, d in enumerate(split_number[0]):
        integer_part += digit2Value[d] * (base**(max_exponent-i))

        if i < max_exponent:
            print("{0}*{1}^{2}".format( d,base, max_exponent-i ),end=" + ")
        else:
            print("{0}*{1}^{2}".format( d,base, max_exponent-i ),end="")

    # decimal part  
    decimal_part = 0
    if len(split_number) > 1:
        max_exponent = len(split_number[1]) - 1

        print(" + ",end="")
        for i, d in enumerate(split_number[1]):
            decimal_part += digit2Value[d] * (base**( -(i+1) ))

            print("{0}*{1}^-{2}".format(d,base,i+1),
                                end = " + " if i < max_exponent else "\n")

    return integer_part + decimal_part

def main():
    print("\n"*3)
    print("="*50)
    print("From base X to decimal numeric system".center(50))
    print("="*50)
    print("\n")
    
    print(" 0) Binary base \n 1) Octal base \n 2) Hexadecimal base \n 3) Other ")
    option = input("Choose your base: ")
    
    base = 0
    
    if option == '0':
        base = 2
    elif option == '1':
        base = 8
    elif option == '2':
        base = 16
    else:
        pass # TODO: Lo que usted tiene que completar

    print("\n")
    numberX = input("input the number to convert from base "+ str(base) + " : " )
    print("you enter: ", numberX)

    if is_number_base_x( numberX, base ):
        print("-"*50)
        value_base10 = baseX_to_base10( numberX , base )
        
        print("\n")
        print("-"*50)
        print("\n number ", numberX , "in base ", base)
        print("  converted to decimal is: ", value_base10)
        print("-"*50)

    else:
        print(numberX, """\t is not a number in base X!!!
    I can't help you ...""")

    print("\n")
if __name__ ==  "__main__":
    main()








