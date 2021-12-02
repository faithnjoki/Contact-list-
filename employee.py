class EmployeeRecord:
    """
    first_name
    last_name
    date_joined
    
    """
    def __init__(self,first_name,last_name,date_joined = '1st December',employee_number=1):
        # date and employee number have defaults 
        self.first_name = first_name
        self.last_name = last_name
        self.date_joined = date_joined 
        self.employee_number = employee_number