class Util:

    @staticmethod
    def update_properties(object_to_validate: dict, properties: list) -> dict:
        for checked_property in properties:
            value_of_property = object_to_validate.get(checked_property, [])
            if isinstance(value_of_property, dict):
                if value_of_property:
                    object_to_validate[checked_property] = [value_of_property]
                else:
                    object_to_validate[checked_property] = []
        return object_to_validate
