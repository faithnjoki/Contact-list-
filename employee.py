class EmployeeRecord:
    # Class are blueprints
    
    """
    first_name
    last_name
    date_joined
    
    """
    
    def __init__(self,first_name,last_name,date_joined = '1st December',employee_number=1):
        # init is a constructor method used to instatiate instances of classes
        # date and employee number have defaults 
            # self.firstnaame and the rest is an atribute of the instance and what is after = sign is the value
        self.first_name = first_name
        self.last_name = last_name
        self.date_joined = date_joined 
        self.employee_number = employee_number