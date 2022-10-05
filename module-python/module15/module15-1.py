class DepartmentReport():
    def __init__(self):  
        self.revenues = []  
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
        return sum(self.revenues)  / len(self.revenues)
      
    def print_report(self):  
        """_summary_
        """
        print("Total sales:", self.average_revenue()) 


report = DepartmentReport()
report.add_revenue(1_000_000)
report.add_revenue(400_000)
print(report.revenues)
print(report.average_revenue())