""" Write a function called sumRange that given two integers returns the sum
of all the integers between the two given integers inclusive. For instance,
sumRange(3,6) would return 18. Use a second function in the definition of
sum-Range to show that you can employ some top-down design to
decompose this problem into a simpler problem and then use that simpler
solution to solve this problem. """

def sumRange(n1,n2):
    soma = 0
    for sum in range(n1,n2+1):
        soma += sum
        print(soma)

def main():
    n1 = int(input('Please enter a integer to sum: '))
    n2 = int(input('Please enter the last integer to sum: '))
    sumRange(n1,n2)

main()