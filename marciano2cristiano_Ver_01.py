print("\n"*3)
print("="*50)
print("From marcian to christian numeric system".center(50))
print("="*50)
print("\n")

marcian = input("input the marcian number: ")
print("you enter: ", marcian)

split_marcian = marcian.split(".")
print("split marcian: ", split_marcian)

# Validation, is a marcian number???
is_marcian_number = True
for part in split_marcian:
    for digit in part:
        if not (0<=int(digit)<3):  # remember type of digit is str
            print(marcian, """ is not a marcian number!!!
    I can't help you ...
    *note: marcian digits are only: 0,1,2""")
            is_marcian_number = False
            break
    if not is_marcian_number:
        break
        
if is_marcian_number:
    # display and compute numeric expansion, integer part
    print("Expansion in power series: ")
    integer_part = 0
    max_exponent = len(split_marcian[0]) - 1
    for i, d in enumerate(split_marcian[0]):
        integer_part += int(d) * (3**(max_exponent-i))

        if i < max_exponent:
            print("{0}*3^{1}".format( d, max_exponent-i ),end=" + ")
        else:
            print("{0}*3^{1}".format( d, max_exponent-i ),end="")

    # display and compute decimal part  
    decimal_part = 0
    if len(split_marcian) > 1:
        max_exponent = len(split_marcian[1]) - 1

        print(" + ",end="")
        for i, d in enumerate(split_marcian[1]):
            decimal_part += int(d) * (3**( -(i+1) ))
            print("{0}*3^-{1}".format(d,i+1),
                                end = " + " if i < max_exponent else "\n")

    print("marcian number ", marcian, " in christian is: ", integer_part + decimal_part)









