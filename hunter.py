from termcolor import colored
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import re

email_pattern = re.compile(r"[A-Za-z0-9.]+@[A-Za-z0-9.]+")
em_pattern = re.compile(r"[A-Za-z0-9.]+@<em>[A-Za-z0-9.]+<\/em>")

def select_chrome():
    import chromedriver_autoinstaller
    chromedriver_autoinstaller.install()

def select_firefox():
    import geckodriver_autoinstaller
    geckodriver_autoinstaller.install()

def initial_setup():
    choice = None
    while True:

        print(colored("1. Chrome", "blue"))
        print(colored("2. Mozilla Firefox", "blue"))
        
        choice = int(input("Choice: "))
        if choice == 1:
            print(colored("[+]Welcome to email hunter", "green"))
            print(colored("[*]Installing chrome driver...", "blue"))
            select_chrome()

        elif choice == 2:
            print(colored("[+]Welcome to email hunter", "green"))
            print(colored("[*]Installing geckodriver...", "blue"))
            select_firefox()

        else:
            print(colored("[-]The given choice doesn't exist yet.", "red"))
        
    
        return choice

def page_search(choice:int, domain = "gmail.com", site = "www.google.com", scroll_number = 6)-> list[str]:
    emails = []
    driver = webdriver.Firefox() if choice == 2 else webdriver.Chrome()
    try:
        driver.get("https://www.google.com")
        driver.maximize_window()
        sleep(3) 
        search_box = driver.find_elements(By.NAME, "q")[0]
        search_emails = f'site:{site} intext:"@{domain}"'
        search_box.send_keys(search_emails)
        sleep(1)
        search_box.send_keys(webdriver.Keys.RETURN)
        sleep(3)
        pageSource = driver.page_source
        for pattern in email_pattern.findall(pageSource):
            emails.append(pattern)
        for pattern in em_pattern.findall(pageSource):
            emails.append(pattern)
        sleep(3)
        for i in range(scroll_number):
            # print("Loop iter starts")
            html = driver.find_element(By.TAG_NAME, 'html') 
            html.send_keys(webdriver.Keys.END)
            sleep(4)
            pageSource = driver.page_source
            for pattern in email_pattern.findall(pageSource):
                emails.append(pattern)
            for pattern in em_pattern.findall(pageSource):
                emails.append(pattern)
            # print("Loop iter done")
        driver.quit()
        return emails

    except:
        print(colored("[-]An error occured", "red"))
        driver.quit()
        return []


def process_emails(emails_list) -> list:
    em_pattern = re.compile(r"[A-Za-z0-9.]+@<em>[A-Za-z0-9.]+<\/em>")
    for i in range(len(emails_list)):
        item = emails_list[i]
        if em_pattern.match(item):
            emails_list[i] = emails_list[i].replace("<em>", "")
            emails_list[i] = emails_list[i].replace("</em>", "")
    return emails_list

def write_to_file(emails_list, filepath):
    print(colored(rf"[*] Writing to emails to {filepath}", "blue"))
    with open(rf'{filepath}', mode='w') as file:
        emails_list = [emails_list[i] + '\n' for i in range(len(emails_list))]
        file.writelines(emails_list)
        print(colored(f"[\u2713] Emails successfully written to " + rf"{filepath}", "green"))

def main():
    banner = """
     ███╗   ███╗ █████╗ ██╗██╗         ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
     ████╗ ████║██╔══██╗██║██║         ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
     ██╔████╔██║███████║██║██║         ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
     ██║╚██╔╝██║██╔══██║██║██║         ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
     ██║ ╚═╝ ██║██║  ██║██║███████╗    ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
"""
    print(colored(banner, "yellow"))
    print(colored("\tExtract emails of a specific domain name from a website.\n\tEnsure that no one finds you ;)", "red"))
    print(colored("Press any key to continue...", "green"))
    input()

    domain = None
    website = None

    domain = input("Enter the email domain name (do not include @): ")
    website = input("Enter the website name: ")
    scroll_number = int(input("Number of scrolls per page: "))

    if not scroll_number:
        scroll_number = 6

    if not domain:
        domain =  "gmail.com"

    if not website:
        website = "www.google.com"

    choice = initial_setup()
    print(colored("[*] Finding emails...", "blue"))
    emails = set(process_emails(page_search(choice, domain=domain, site=website, scroll_number=scroll_number)))
    emails = [email for email in emails if domain in email]
    print(colored(f"[\u2713] Found {len(emails)} emails.", "yellow")) 
    print("Press any key to continue")

    for email in emails:
        print(colored(f"[+] {email}", "green"))

    print(colored("Press\n1. To write contents to a text file\n 2. Exit the program"))
    c = int(input("Choice: "))
    if c == 1:
        fp = input("Enter the filename: ")
        write_to_file(emails_list=emails, filepath=fp)  
    else:
        print(colored("Exiting the program. See you soon.", "cyan"))

    

if __name__ == "__main__":
    main()

#TODO: Include the cli and prettify the output. Add an option to put output into a text file.
