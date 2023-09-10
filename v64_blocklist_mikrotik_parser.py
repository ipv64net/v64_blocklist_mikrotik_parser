import requests,json
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def api_abfrage(api_url, benutzername, passwort):
    try:
        # Eine GET-Anfrage an die API senden und Benutzername und Passwort übergeben
        response = requests.get(api_url, auth=HTTPBasicAuth(benutzername, passwort), verify=False)

        # Überprüfen, ob die Anfrage erfolgreich war (Statuscode 200)
        if response.status_code == 200:
            # Die JSON-Daten aus der Antwort extrahieren (falls die API JSON verwendet)
            daten = response.json()
            return daten
        else:
            print("Fehler bei der Anfrage. Statuscode:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Fehler bei der Anfrage:", e)
        return None

if __name__ == "__main__":
    v64_api_token="12345"
    v64_blocker_node_id="1234"
    mikrotik_router_ip = "1234"
    mikrotik_api_user = "api"
    mikrotik_api_pw = "api"
    api_url = f"https://{mikrotik_router_ip}/rest/ip/firewall/address-list?list=Block-SSH-Tarpit"  # Hier die URL deiner API eintragen
    daten = api_abfrage(api_url, mikrotik_api_user, mikrotik_api_pw)

    ip_list = []
    if daten:
        # Hier kannst du die Daten weiterverarbeiten, z.B. ausgeben
        print(json.dumps(daten, indent=4))  # Ausgabe der Daten als schön formatiertes JSON
        for eintrag in daten:
            if "address" in eintrag:
                ip_addr={"ip":eintrag["address"]}
                ip_list.append(ip_addr)
            else:
                print("Kein Address-Feld gefunden.")
    else:
        print("Fehler bei der API-Anfrage.")
    ip_list= {"ip_list": ip_list}
    ip_list=json.dumps(ip_list)
    print(ip_list)
    url = "https://ipv64.net/api.php"
    payload = {'blocker_id': v64_blocker_node_id,
        'report_ip_list': ip_list
    }
    headers = {
      'Authorization': f"Bearer {v64_api_token}"
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
