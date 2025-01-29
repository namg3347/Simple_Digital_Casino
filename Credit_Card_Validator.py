def input_card():
    #step-1:inputing the card_number
    card_number = input("Enter your valid credit card number: ")
    return card_number


def checker(card_number):
    #step -2 : checking  '-' and " " and digits in the credit card number
    if all(part.isdigit() for part in card_number.split(" ")) and " " in card_number:
        return (card_number)
    elif all(part.isdigit() for part in card_number.split("-")) and "-" in card_number:
        
        return (card_number)
    else:
        while True:
            if all(part.isdigit() for part in card_number.split(" ")) and " " in card_number:
                
                return (card_number)
            elif all(part.isdigit() for part in card_number.split("-")) and "-" in card_number:
        
                return (card_number)
            else:
                print("Enter a valid card number with digits separated by either spaces or dashes.")
                card_number = input_card()
            
def validator(card_number):
    sum_odd_digits =0
    sum_even_digits =0
    total=0
    #step removing seperators from card_numbers
    card_number=card_number.replace(" ","").replace("-","")
    #step-2 : getting sum of odd digits from right to left and getting double of sum of even digits from right to left
    #and getting the total sum.
    card_number = card_number[::-1] 
    #used to direcly reverse the string, '::' used goes through the string from start to end and 
    # '-1' represents index just after the len(card_number)
    # this easily reverse the string

    for i in card_number[::2]:
        sum_odd_digits+=int(i)
    
    for i in card_number[1::2]:
        i = int(i)*2
        if i>=10:
            sum_even_digits+= (1+(i%10))
        else:
            sum_even_digits += i
    #step-3:final checking if total is divisible is 10 or not
    total = sum_even_digits + sum_odd_digits

    return total%10==0

def main():
    card_number = input_card()
    #if the credit card is just in digits that we dont need to check and remove spaces or hyphen
    if card_number.isdigit():
        print(validator(card_number))
    else:
    #if the user adds anything else than just digits than we need checker 
        print(validator(checker(card_number)))
   
       


if __name__ == "__main__" :
    main()




