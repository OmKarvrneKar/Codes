from abc import ABC ,abstractmethod # ABC STAND FOR ABSTRACT BASE CLASS

class vehical(ABC): # VEHICAL IS ABSTRACT CLASS

    @abstractmethod # THIS IS AN ABSTRACT METHOD
    def start(self): # ABSTRACT METHOD IS A METHOD THAT IS DECLARED BUT CONTAINS NO IMPLEMENTATION
        pass # NULL STATEMENT IS USED AS A PLACEHOLDER FOR FUTURE CODE


    
class car (vehical):  # inheriting the abstract class vehical

    def start(self):
        print("car started")

c= car()

c.start()


#============================================

class rbi(ABC):

    @abstractmethod
    
    def interest_rate(self):
        pass
class sbi(rbi):
    def interest_rate(self):
        print("sbi interest rate is 6%")    

class icici(rbi):
    def interest_rate(self):
        print("icici interest rate is 7%")

class hdfc(rbi):
    def interest_rate(self):
        print("hdfc interest rate is 8%")   


#=========================================
# class ThroneInheritance:

#     def __init__(self, kingName: str):
#         self.king= kingName
#         self.children = defaultdict(list)
#         self.dead = set()


#     def birth(self, parentName: str, childName: str) -> None:
#         self.children[parentName].append(childName)

        

#     def death(self, name: str) -> None:
#         self.dead.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        order=[]

        def dfs(person):

            if person not in self.dead:

                order.append(person)

            for child in self.children[person]:
                dfs(child)
        dfs (self.king)
        return order
        


