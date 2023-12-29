### to validate a json against a given schema file

### First we have to creating the schema file

### mutual exclusive 
if one is value is present other should not present 

#### \
"\" symbol is used to continue to the next line

```
if 6<10.   \
:
  print("correct")
```
understanding the 
```
 # Validating  either one field or another field
            either_one_fields = schema.get('either_one', [])
            if not any(field in json_data for field in either_one_fields) or \
               not all(field not in json_data for field in set(schema) - set(either_one_fields)):
                print("44")
                return False

```
* condition 1:
```
if not any(field in json_data for field in either_one_fields) 
```
This will check  any one should be present 
* condition 2:
```
set_difference = set(schema) - set(either_one_fields)
<!-- to consider only the element from schema -->
condition2 = all(field not in json_data for field in set_difference)
```
Check if all fields from the set difference between schema and either_one_fields are not present in json_data 

* after that we have to check the 
```
not of condition1 or not of condition2 then we return false

```
