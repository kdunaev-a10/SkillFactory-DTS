class DepartmentReport():
    def __init__(self, company):  
        self.revenues = []  
        self.company = company 
        
    def add_revenue(self, amount):
        """
        Метод для добавления выручки отдела в список revenues.
        Если атрибута revenues ещё не существует, метод должен создавать пустой список перед добавлением выручки.
        """
#        if not hasattr(self, 'revenues'):  
#            self.revenues = []  
        # Добавим текущую сделку  
        self.revenues.append(amount)  
    
    def average_revenue(self):
        """
        Метод возвращает среднюю выручку по отделам.
        """
        average = round(sum(self.revenues)  / len(self.revenues))
        return 'Average department revenue for {}: {}'.format(self.company,average)
      
    def print_report(self):  
        """_summary_
        """
        print("Average department revenue for {}: {}".format(self.company, self.average_revenue())) 


report = DepartmentReport('test')
report.add_revenue(1_000_000)
report.add_revenue(400_000)
print(report.revenues)
print(report.average_revenue())

report1 = DepartmentReport("Danon")
report1.add_revenue(1_000_000)
report1.add_revenue(400_000)
print(report1.average_revenue())



class SalesReport():  
    def __init__(self, employee_name):  
        self.deals = []  
        self.employee_name = employee_name  
      
    def add_deal(self, company, amount):   
        self.deals.append({'company': company, 'amount': amount})  
          
    def total_amount(self):  
        #return sum([deal['amount'] for deal in self.deals])  
        return [deal['amount'] for deal in self.deals]
      
    def average_deal(self):  
        #return self.total_amount()/len(self.deals)  
        return 100
      
    def all_companies(self):  
        return list(set([deal['company'] for deal in self.deals]))  
      
    def print_report(self):  
        print("Employee: ", self.employee_name)  
        print("Total sales:", self.total_amount())  
        print("Average sales:", self.average_deal())  
        print("Companies:", self.all_companies())  

report = SalesReport("Ivan Semenov")  
  
report.add_deal("PepsiCo", 120_000)  
report.add_deal("SkyEng", 250_000)  
report.add_deal("PepsiCo", 20_000)  
  
report.print_report()  