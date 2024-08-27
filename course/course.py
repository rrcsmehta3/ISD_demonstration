from department.department import Department
 
 
class Course():
    """
    Represents templetes for a course
      """
    def __init__(self , name:str, department:Department, credit_hours:int):
       
        if len(name.strip()) >0:
              self.__name = name
        else:
             raise ValueError("name cannot be blanck")
 
        if isinstance(department, Department):
             self.__department = department
        else:
              raise ValueError("Department must be one of the predefined department")
       
        if isinstance(credit_hours,int):
             self.__credit_hours = credit_hours
        else:
             raise ValueError("Credit hours must be a whole number")
        @property
        def name(self) -> str:
            return self.__name
        @property
        def department(self) -> Department:
            return self.__department
        @property
        def credit_hours(self) -> int:
            return self.__credit_hours
        @property
        def __str__(self) ->str:
             return(f"course: {self.__name} \nDepartment:{self.__department} \nCredit Hour: {credit_hours}")
       
        self.__name = name
 
        self.__department = department
 
        self.__credit_hours = credit_hours