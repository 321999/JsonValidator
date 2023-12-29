import json
'''
1. required fields. Example: id, name field to be declared as they are mandatory
1. required fields. Example: id, name field to be declared as they are mandatory
2. atleast one of many fields to be present. Example: one of home phone or cell phone
or work phone fields
3. either one field or another field Either birth date or govt id number
4. mutually exclusive fields (if one is present, the other should not be present)
5. field value to be one of a set of values. Example: field day can have only one of
SU,MO,TU,WE,TH,FR,SA (enum)
'''
Schema={
    "required":["id","name"],
    "atleast_one_of_many":[
        ["home phone","cell phone","work phone"]
    ],
    "either_one":["DOB","govt_id"],
    "mutual_exclusive":[["DOB","govt_id"]],
    "enum":["SU","MO","TU","WE","TH","FR","SA"]
}

json_stirng=json.dumps(Schema)
# creating the file of json
with(open("schema.json","w") as file):
    file.write(json_stirng)