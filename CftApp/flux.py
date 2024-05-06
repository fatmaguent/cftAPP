import re

def get_idf_type_by_partner(config_content, partner_name):
    # Définir le modèle regex pour rechercher les lignes contenant le nom du partenaire et le type IDF
    regex_pattern = r"CFTIDF\s+ID\s*=\s*('[^']*')\s*,\s*NIDF\s*=\s*('[^']*')\s*,\s*PART\s*=\s*('[^']*')\s*,\s*TYPE\s*=\s*('SEND'|'RECV')"

    # Rechercher toutes les correspondances dans le contenu de la configuration
    matches = re.findall(regex_pattern, config_content)

    # Filtrer les correspondances pour le partenaire spécifié
    partner_matches = [match for match in matches if match[2] == f"'{partner_name}'"]

    # Compter les occurrences de 'SEND' et 'RECV'
    send_count = sum(1 for match in partner_matches if match[3] == "'SEND'")
    recv_count = sum(1 for match in partner_matches if match[3] == "'RECV'")

    # Construire la chaîne de type de flux
    type_str = ""
    if send_count > 0:
        type_str += f"{send_count} SEND"
    if recv_count > 0:
        if type_str:
            type_str += ", "
        type_str += f"{recv_count} RECEIVE"

    return type_str

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
