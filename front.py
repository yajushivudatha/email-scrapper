import eel
from hunter import page_search, process_emails
# eel -> change its __init__.py import bottle.ext.websocket -> import bottle_websocket to avoid errors

eel.init("web")

# GUI is intended for use with google chrome only.

@eel.expose
def search_emails(domain_name, site):
    emails = list(set(process_emails(page_search(choice = 1, domain=domain_name, site = site))))
    print("Found emails")
    return emails

eel.start("index.html")

