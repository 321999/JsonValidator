from pathlib import Path
import json


class JsonValidator:
    def __init__(self) -> None:
        pass

    def validate_schema(self, json_file: Path, schema_file: Path) -> bool:
        """
        Validate a JSON against a given schema file.

        :param json_file: Path to the JSON file to be validated.
        :type json_file: Path
        :param schema_file: Path to the schema file.
        :type schema_file: Path
        :return: True if validation succeeds, False otherwise.
        :rtype: bool
        """
        try:
            with open(json_file, 'r') as json_data_file:
                json_data = json.load(json_data_file)
                print([i for i in json_data])

            with open(schema_file, 'r') as schema_json_file:
                schema = json.load(schema_json_file)
                print(f"schema is", schema)

            print("printing schema file ", schema.get("required"))

            for field in schema.get("required", []):
                if field not in json_data:
                    print("*" * 24)
                    print(f"{field} not in json")
                    return False

            schema_data = schema.get("atleast_one_of_many")

            for group in schema_data:
                print(any(it in json_data for it in group))
                if not any(item in json_data for item in group):
                    return False

            mutual_exclusive = schema.get("mutual_exclusive")

            for group in mutual_exclusive:
                if all(field in json_data for field in group):
                    return False

            enum_day = schema.get("enum", [])
            if sum(day in json_data for day in enum_day) > 1:
                return False

            return True
        except (json.JSONDecodeError, FileNotFoundError):
            return False


if __name__ == "__main__":
    j = JsonValidator()
    if j.validate_schema("/Users/apple/Desktop/Task3/json_file.json", "/Users/apple/Desktop/Task3/schema.json"):
        print("Validation succeeded")
    else:
        print("Validation failed")
