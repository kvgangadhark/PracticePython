import webbrowser

chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"

def change_address(str1):
    str2 = str1.replace("emulex.com","lvn.broadcom.net")
    webbrowser.get(chrome_path).open(str2)
    
    return str2

str1 = "http://srcserver.emulex.com/projects/be2_sw/changeset/368509"
change_address(str1)
