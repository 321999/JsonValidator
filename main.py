from pathlib import Path
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
       
        for field in schema.get("required",[]):
            if field not in json_data:
                print(f"{field} not in json")
                return False
        
        # logic atleast one of many fields to be present. Example: one of home phone or cell phone
        for group in schema.get("atleast_one_of_many"):
            if not any(item in json_data for item in group):
                # if not any of the field is present in the json data then return false
                return False

        # 3.  To check eihthe one field or another field 
        either_one_fields = schema.get('either_one', [])
        if not any(field in json_data for field in either_one_fields) or \
            not all(field not in json_data for field in set(schema) - set(either_one_fields)):
            print("44")
                return False
        
            print(group)
        return True
if __name__=="__main__":
    j=JsonValidator()
    print(j.validate_schema("/Users/apple/Desktop/Task3/json_file.json","/Users/apple/Desktop/Task3/schema.json"))