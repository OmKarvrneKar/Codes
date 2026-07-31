class rbi:
    def interest_rate(self):
        print("defIne interest rate")
class sbi(rbi):
    def deposit(self):
        print("deposit money in sbi")

    def interest_rate(self):
        print("sbi interest rate is 5%")

class sbihydrabad(sbi):
    def deposit(self):
        print("deposit money in sbi hydrabad")


# s=sbi()
# s.interest_rate()
# s.deposit()

sh=sbihydrabad()
sh.interest_rate()
# multilevel inheritance


