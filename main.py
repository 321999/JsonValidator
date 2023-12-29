from pathlib import Path
from typing import Any
import json


# creating a class called JsonValidator
class JsonValidator:

# creating a constructor of the class
    def __init__(self) -> None:
        pass
    # creating the methodto  Validate a Json against a given schema file
    def validate_schema(self,json_file:Path, schema_file:Path)->bool:
        '''
        param: json_file This is the file which is going to be validated 
        type: Path As We are going to take the json path as input 
        param schema_file This is the file which is going to be validate the json file 
        type :Path As We are going to take the json path as input
        return bool if validation succeeded then return true else false
        '''

        # loading the json data form json file 
        with open(json_file,'r') as json_data_file:
            json_data=json.load(json_data_file)
            print([i for i in json_data])
        
        # similarly loading the external schema file  
        with open(schema_file,'r') as schema_json_file:
            schema=json.load(schema_json_file)
            print(f"shcema is",schema)

        # print(json_file)
        # first of all validating the required field
        print("printing schema file ",schema.get("required"))
        #  id, name field to be declared as they are mandatory
        # print(schema.get("required",[]))
        for field in schema.get("required",[]):
            if field not in json_data:
                print("*"*24)
                print(f"{field} not in json")
                return False
        # print(schema.get("atleast_one_of_many"))
        # logic atleast one of many fields to be present. Example: one of home phone or cell phone
        schema_data=schema.get("atleast_one_of_many")
        for group in schema_data:
            print(any(it in json_data for it in group))
            if not any(item in json_data for item in group):
                # if not any of the field is present in the json data then return false
                return False

        # 4. mutually exclusive fields (if one is present, the other should not be present)
        # In this we perform mutually exclusive on dob and uid
        mutual_exclusive=schema.get("mutual_exclusive")  
        for group in mutual_exclusive:  
           if all(field in json_data for field in group):
                return False
        
        # 5. field value to be one of a set of values. Example: field day can have only one of
# SU,MO,TU,WE,TH,FR,SA (enum)
        enum_day=schema.get("enum",[])
        if sum(day in json_data for day in enum_day)>1:
             return False

        return True
if __name__=="__main__":
    j=JsonValidator()
    print(j.validate_schema("/Users/apple/Desktop/Task3/json_file.json","/Users/apple/Desktop/Task3/schema.json"))