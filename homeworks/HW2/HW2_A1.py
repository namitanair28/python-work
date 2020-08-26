# CSCI 1133, Lab Section 007, HW 1, Problem A1
# Namita Nair, nair0025

def subtractWhile(total, num, times):
    while times >= 1:
        answer = total - num
        total = answer
        times -= 1
    return answer
        
def main():
    total = int(input("Please enter the current total:  "))
    num = int(input("What number will be subtracted?  "))
    times = int(input("How many times should we subtract?  "))
    print("Answer:  ", total, " - ( ", num, " * ", times, " ) = ", subtractWhile(total, num, times))
    
main()