import re

def extract_ssl_info(config_content, partner_name):
    ssl_info = {}
    match_ssl = re.search(fr'CFTSSL\s+ID\s*=\s*\'DSSL{partner_name}.*?USERCID\s*=\s*\'([^\']+)\'', config_content, re.DOTALL)
    if match_ssl:
        ssl_info['USERCID'] = match_ssl.group(1)
    return ssl_info

def extract_root_cid(config_content):
    root_cid = []
    root_cid_matches = re.search(fr'ROOTCID\s*=\s*\((.*?)\)', config_content, re.DOTALL)
    if root_cid_matches:
        root_cid_items = re.findall(r"'([^']+)'", root_cid_matches.group(1))
        root_cid = [item.strip() for item in root_cid_items]
    return root_cid


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
