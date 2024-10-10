import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id']== 101, ['name', 'age']]
    #student1 = (students['student_id']==101)
    #return student1.loc[student1,['name','age']]
    #return students.query("student_id == 101")[["name", "age"]]
    #return students[["name", "age"]][students["student_id"] == 101]