import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    #employees['bonus'] = employees['salary']*2
    #employees['bonus'] = employees['salary'].apply(lambda x: x*2)
    #return employees.assign(bonus=2 * employees['salary']
    employees["bonus"]=2*employees["salary"]
    return employees
    