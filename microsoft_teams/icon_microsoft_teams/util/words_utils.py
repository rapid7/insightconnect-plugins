from icon_microsoft_teams.util.strip_html import strip_html

def add_words_values_to_message(microsoft_message: dict) -> dict:
    message_content = microsoft_message.get("body", {}).get("content", "")
    if microsoft_message.get("body", {}).get("contentType", "").lower() == "html":
       message_content = strip_html(message_content)

    words = message_content.split(" ")
    try:
        first_word = words[0]
    except Exception:
        first_word = ""

    microsoft_message["first_word"] = first_word
    microsoft_message["words"] = words

    return microsoft_message
