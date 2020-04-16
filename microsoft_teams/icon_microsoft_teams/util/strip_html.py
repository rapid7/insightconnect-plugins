from bs4 import BeautifulSoup

def strip_html(in_text):
    if in_text:  # BeautifulSoup will bomb on null text
        soup = BeautifulSoup(in_text, features='html.parser')
        for script in soup(["script", "style"]):  # remove all javascript and stylesheet code
            script.extract()
        text = soup.get_text()
        text = text.strip("\n")
        return text
    else:
        return in_text
