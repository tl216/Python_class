
#Homework 3 (Extra): Program to calculate ticket cost


#Function: calculateCost
#          This function calculates the cost of tickets based on the number of adults and child.
#          The cost of adult is $10 and child is $5.
#          if the student is buying the tickets, there will be 15% discount.
#Return:   cost of ticket
ADULT_PRICE = 10.00
CHILD_PRICE = 5.0
DISCOUNT = 0.85

def calculateCost(nAdultTickets, nChildTicket, studentIsBuying):

    cost = (nAdultTickets * ADULT_PRICE) + (nChildTicket * CHILD_PRICE)

    if (studentIsBuying):
        cost = (cost * DISCOUNT)      #15% if student is buying

    return cost

# Main program

#1
student = False
nAdults = 1
nChild = 1
totalCost = calculateCost(nAdults, nChild, student)
print("Cost of the show for " + str(nAdults) + " adults and " + str(nChild) + " child is: $" + str(totalCost))

#2
student = True
nAdults = 1
nChild = 1
totalCost = calculateCost(nAdults, nChild, student)
print("Cost of the show for " + str(nAdults) + " adults and " + str(nChild) + " child is: $" + str(totalCost))


#3
student = False
nAdults = 0
nChild = 8
totalCost = calculateCost(nAdults, nChild, student)
print("Cost of the show for " + str(nAdults) + " adults and " + str(nChild) + " child is: $" + str(totalCost))

#4
student = True
nAdults = 3
nChild = 3
totalCost = calculateCost(nAdults, nChild, student)
print("Cost of the show for " + str(nAdults) + " adults and " + str(nChild) + " child is: $" + str(totalCost))

#5
student = True
nAdults = 6
nChild = 0
totalCost = calculateCost(nAdults, nChild, student)
print("Cost of the show for " + str(nAdults) + " adults and " + str(nChild) + " child is: $" + str(totalCost))

#6
nAdults = raw_input("How many adult tickets: ")
nAdults = int(nAdults)
nChild = raw_input("How many nChild tickets: ")
nChild = int(nChild)
isStudent = raw_input("Are you a student (y or n)? ")
isStudent = str(isStudent)

if (isStudent == "y") or (isStudent == "n"):
    if (isStudent == "y"):
        student = True
    elif (isStudent == "n"):
        student = False

    totalCost = calculateCost(nAdults, nChild, student)
    print("Cost of the show for " + str(nAdults) + " adults and " + str(nChild) + " child is: $" + str(totalCost))

else:
    print(isStudent + " is an invalid input!")






