import re

def extract_sap(config_content, partner_name):
    # Fonction pour extraire SAP à partir du fichier de configuration
    sap = None
    match_sap = re.search(fr'CFTPART\s+ID\s*=\s*\'{partner_name}\'.*?SAP\s*=\s*\(\s*\'(\d+)\'\)', config_content, re.DOTALL)
    if match_sap:
        sap = match_sap.group(1)
    return sap

def extract_host(config_content, partner_name):
    # Fonction pour extraire HOST à partir du fichier de configuration
    host = None
    match_ip = re.search(fr'CFTTCP\s+ID\s*=\s*\'{partner_name}\'.*?HOST\s*=\s*\(\s*\'([\d\.]+)\'\)', config_content, re.DOTALL)
    if match_ip:
        host = match_ip.group(1)
    return host

def read_config_file(config_file_path):
    # Fonction pour lire le contenu du fichier de configuration
    try:
        with open(config_file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Fichier de configuration '{config_file_path}' introuvable.")
        return None
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier de configuration : {e}")
        return None
