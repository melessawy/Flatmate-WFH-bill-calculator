from bill import Bill
from flatmate import Flatmate
from controller import Controller

def main():
    no_of_flatmates = int(input('enter the number of flatmates: '))
    flatmates = []

    print("***************************************")
    print("Flatmate details")
    print("***************************************")


    for i in range(no_of_flatmates):
        name = input("enter flatmate name: ")
        days = int(input("enter the number of days {} works from the office this month: ".format(name)))
        hours = float(input("enter the number of hours {} spends at work per day (including commute time): ".format(name)))
        person = Flatmate(name, days, hours)
        flatmates.append(person)

    print("***************************************")
    print("Bill details")
    print("***************************************")

    bill_amount = float(input("enter the bill's amount: "))
    bill = Bill(bill_amount)

    print("***************************************")
    print("Computing hours spent at the house")
    print("***************************************")

    for flatmate in flatmates:
        flatmate.compute_hours_in_house(bill)
        print("{} will spend a total of {} hours in the house this month".format(flatmate.name, flatmate.hours_in_house))

    print("***************************************")
    print("Computing the bill shares per flatmate")
    print("***************************************")

    cont = Controller()
    cont.compute_total_hours_occupancy(flatmates)

    for flatmate in flatmates:
        flatmate.compute_weight(cont.total_hours_occupancy)
        print("{}'s share of the bill: ${}.".format(flatmate.name, round(flatmate.weight * bill.amount, 2)))

if __name__ == "__main__":
    main()
