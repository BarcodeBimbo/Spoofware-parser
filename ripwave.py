import requests, json
from bs4 import BeautifulSoup

#################################################################################
#                                   RIP                                         #
#                                                                               #
# ███████ ██████   ██████   ██████  ███████ ██     ██  █████  ██    ██ ███████  #
# ██      ██   ██ ██    ██ ██    ██ ██      ██     ██ ██   ██ ██    ██ ██       #
# ███████ ██████  ██    ██ ██    ██ █████   ██  █  ██ ███████ ██    ██ █████    #
#      ██ ██      ██    ██ ██    ██ ██      ██ ███ ██ ██   ██  ██  ██  ██       #
# ███████ ██       ██████   ██████  ██       ███ ███  ██   ██   ████   ███████  #                                                                                                                                                   
#                                                                               #
#  Reversed & developed by Joshua With Love                                     #
#  Contact: @UrFingPoor - Version: 1.0.0 - Last Updated: 11/14/2024             #
#################################################################################

#region Request_INFO
url = ""
base_url = "https://spoofwave.com/"
menuitems = """ 
        Search Type Menu Options: 
        - 1. E-Mail - Leak Check
        - 2. Phone - Carrier Check
        - 3. Username - Leak Check
        - 4. Seon - Registration Check: Email/Phone
"""
#endregion

def get_search_type_value(index: str):
    global url 
    match(index):
        case "1":
            url = f"{base_url}leakcheck"  
            print(url)  
            return "value"
        case "2":
            url = f"{base_url}carrier"
            return "number"
        case "3":
            url = f"{base_url}username" 
            return "username"
        case "4":
            url = f"{base_url}seon"
            return "searchvalue"


def spoofwave_api(search_type: str, search_value: str):
    try:
        
        data = { search_type: search_value, "submit": "" }
        
        response = requests.post(url, data=data)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table")
        if not table:
            print("No table found in the response.")
            exit()

        parsed_data = {}
        rows = table.find_all("tr")

        if len(rows) < 2:
            print("Table does not contain enough rows to parse.")
            exit()

        for row in rows[1:]:  
            cols = row.find_all("td")
            
            if len(cols) < 2:
                continue 
            
            field = cols[0].get_text(strip=True)
            value = cols[1].get_text(strip=True)
            parsed_data[field] = value

        return json.dumps(parsed_data, indent=2)

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}") 
    except Exception as err:
        print(f"An error occurred: {err}")       

def main():
    search_type = input(f"{menuitems}\nEnter A Search Type: ")
    search_value = input("Enter A Search Value: ")

    #example spoofwave_api(username | Email | Phone, Swag | swag@gmail.com | 5105680778)
    print(spoofwave_api(search_type=get_search_type_value(search_type), search_value=search_value)) 

if __name__ == "__main__":
	main()
