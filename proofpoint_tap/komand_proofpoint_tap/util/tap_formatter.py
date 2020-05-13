from email.utils import parseaddr
import re


class TAP:

    def __init__(self, data):
        self.data = self.clean_data(data)

    @staticmethod
    def clean_data(data):
        clean_data = {
            "threat": {
                "attachment_sha256": "",
                "category": "",
                "condemnation_time": "",
                "url": "",
                "threat_details_url": ""
            },
            "message": {
                "time_delivered": "",
                "recipients": "",
                "subject": "",
                "sender": "",
                "header_from": "",
                "header_replyto": "",
                "message_id": "",
                "sender_ip": "",
                "message_size": "",
                "message_guid": "",
                "threat_id" : ""
            },
            "browser": {
                "time": "",
                "source_ip": "",
                "user_agent": ""
            }

        }

        def normalize_key(key):
            """Normalize key data in collection"""
            return key.lower().replace(" ", "_").replace("-", "_").replace("=", "")

        def normalize_value(value):
            """Normalize value data in collection"""
            if isinstance(value, str):
                if value == "—":
                    return "-"
                return value.replace("<", "").replace(">", "").rstrip().replace("=", "")

        def walk_clean(collection):
            """Loops collection and walks clean to see if the key exists"""
            regex = '''(?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-zA-Z0-9-]*[a-zA-Z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''
            for item in collection:
                key = normalize_key(item)
                # Walk dict and set value
                for k, v in clean_data.items():
                    if isinstance(v, dict):
                        for kk, vv in v.items():
                            if key == kk:
                                # On match, set value
                                value = collection[collection.index(item) + 1]
                                # Handle replyto and from that contains a string of "<name> <email>"
                                if key in ["header_replyto", "header_from"]:
                                    if "@" in value:
                                        if key == "header_replyto":
                                            value = parseaddr(value)[1]
                                            clean_data["message"]["header_replyto"] = value
                                        if key == "header_from":
                                            value = value.replace('=', '')
                                            value = re.findall(regex, value)[0]
                                            clean_data["message"]["header_from"] = value
                                    elif len(clean_data[k][kk]) == 0:
                                        value = normalize_value(value)
                                        clean_data[k][kk] = value
                                else:
                                    value = normalize_value(value)
                                    clean_data[k][kk] = value
                            # handle recipient normalize
                            if key == "recipient":
                                value = collection[collection.index(item) + 1]
                                value = normalize_value(value)
                                clean_data["message"]["recipients"] = value

        # start of cleaning the data
        if isinstance(data, list):
            for collections in data:
                if isinstance(collections, list):
                    if len(collections) > 0:
                        for collection in collections:
                            walk_clean(collection)

        return clean_data
