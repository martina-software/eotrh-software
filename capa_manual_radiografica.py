<<<<<<< HEAD
# This layer allows the veterinarian to manually enter the radiographic signs observed in the patient.
# It is based on a standardized scale specific for radiographic signs (according to Tretow et al., 2025).

# Manual radiographic layer according to Tretow et al. (2025)
import questionary

def ask_radiographic_signs():
    total_score = 0

    # Number of affected teeth
    affected_teeth_response = questionary.select(
        "Quantity: Teeth Affected:",
        choices=[
            "0 (0 points)",
            "1-4 (1 point)",
            "5-8 (2 points)",
            "≥9 (3 points)"
        ]).ask()
    total_score += int(affected_teeth_response[affected_teeth_response.find('(')+1])

    # Absent teeth/extractions
    absent_response = questionary.select(
        "Quantity: Missing/Extracted teeth:",
        choices=[
            "None (0 points)",
            "One or more incisors already missing/extracted (1 point)"
        ]).ask()
    total_score += int(absent_response[absent_response.find('(')+1])

    # Dental shape
    shape_response = questionary.select(
        "Tooth shape:",
        choices=[
            "Regular (0 points)",
            "Preserved: slightly blunted root tip, enlargement of the periodontal space (1 point)",
            "Largely preserved: circumferential increase of the root tip or the more occlusal part of the tooth, intra-alveolar tooth part < clinical crown (2 points)",
            "Largely lost: intra-alveolar tooth part = clinical crown (3 points)",
            "Lost: intra-alveolar tooth part > clinical crown (4 points)"
        ]).ask()
    total_score += int(shape_response[shape_response.find('(')+1])

    # Dental structure
    structure_response = questionary.select(
        "Tooth structure:",
        choices=[
            "No radiological findings (0 points)",
            "Mild: single area of increased radiolucency (up to max. 1/3 of the root width)(1 point)",
            "Moderate: multiple areas of increased radiolucency (up to max. 1/3) or two (up to 2/3) (2 points)",
            "Severe: large areas of increased radiolucency (3 points)"
        ]).ask()
    total_score += int(structure_response[structure_response.find('(')+1])

    # Dental surface
    surface_response = questionary.select(
        "Tooth surface:",
        choices=[
            "No radiological findings (0 points)",
            "1 1 irregularity (up to max 1/3 root length) (1 point)",
            "2 irregularities / rough surface (2 points)",
            "Obviously irregular (surface slumps)/ rough (3 points)"
        ]).ask()
    total_score += int(surface_response[surface_response.find('(')+1])

    # Classification according to total score
    if total_score == 0:
        stage = "0 - Normal"
        interpretation = "No abnormal radiological findings. Does not exclude mild EOTRH."
    elif 1 <= total_score <= 2:
        stage = "1 - Suspicious"
        interpretation = "Tooth shape preserved but sporadic deviations: slightly blunted root tip, surface irregular/rough, slightly altered tooth structure"
    elif 3 <= total_score <= 5:
        stage = "2 - Mild"
        interpretation = "Tooth shape preserved, slightly blunted root tip, surface irregular/rough, slightly altered tooth structure"
    elif 6 <= total_score <= 9:
        stage = "3 - Moderate"
        interpretation = "Tooth shape largely preserved, intra-alveolar tooth part is not wider than the clinical crown, obviously blunted root tip, surface irregular/rough, moderately altered tooth structure"
    else:
        stage = "4 - Severe"
        interpretation = "Loss of tooth shape, intra-alveolar tooth part is wider than the clinical crown, surface obviously irregular/rough, severely altered tooth structure. Coincides with severe clinical signs."

    # Final results
    print("\n--- Radiographic questionnaire result ---")
    print(f"Total radiographic score: {total_score}")
    print(f"Radiographic stage: {stage}")
    print(f"Interpretation: {interpretation}")
    return total_score

if __name__ == "__main__":
    ask_radiographic_signs()
=======
# Aquesta capa permet al veterinari introduir manualment els signes radiogràfics observats en el pacient.
# Es basarà en una escala estandarditzada específica per a signes radiogràfics (segons Tretow et al., 2025).

# Capa manual radiogràfica segons Tretow et al. (2025)
import questionary

def pregunta_signes_radiografics():
    puntuacio_total = 0

    # Nombre de dents afectades
    resposta_dents_afectades = questionary.select(
        "Nombre de dents afectades:",
        choices=[
            "0 (0 punts)",
            "1-4 (1 punt)",
            "5-8 (2 punts)",
            "≥9 (3 punts)"
        ]).ask()
    puntuacio_total += int(resposta_dents_afectades[resposta_dents_afectades.find('(')+1])

    # Dents absents/extraccions
    resposta_absents = questionary.select(
        "Dents absents o extraccions:",
        choices=[
            "Cap (0 punts)",
            "≥1 incisiu perdut (1 punt)"
        ]).ask()
    puntuacio_total += int(resposta_absents[resposta_absents.find('(')+1])

    # Forma dental
    resposta_forma = questionary.select(
        "Forma dental:",
        choices=[
            "Regular (0 punts)",
            "Conservació parcial (1 punt)",
            "Conservació majoritària (2 punts)",
            "Pèrdua majoritària (3 punts)",
            "Pèrdua completa (4 punts)"
        ]).ask()
    puntuacio_total += int(resposta_forma[resposta_forma.find('(')+1])

    # Estructura dental
    resposta_estructura = questionary.select(
        "Estructura dental:",
        choices=[
            "Cap troballa radiològica (0 punts)",
            "Lleu (1 punt)",
            "Moderada (2 punts)",
            "Greu (3 punts)"
        ]).ask()
    puntuacio_total += int(resposta_estructura[resposta_estructura.find('(')+1])

    # Superfície dental
    resposta_superficie = questionary.select(
        "Superfície dental:",
        choices=[
            "Cap troballa radiològica (0 punts)",
            "1 zona irregular (1 punt)",
            "2 irregularitats / superfície rugosa (2 punts)",
            "Irregularitat marcada / col·lapse (3 punts)"
        ]).ask()
    puntuacio_total += int(resposta_superficie[resposta_superficie.find('(')+1])

    # Classificació segons la puntuació total
    if puntuacio_total == 0:
        estadi = "0 - Normal"
        interpretacio = "Sense alteracions radiogràfiques anormals. No exclou EOTRH lleu."
    elif 1 <= puntuacio_total <= 2:
        estadi = "1 - Sospitós"
        interpretacio = "La forma dental es conserva però hi ha desviacions puntuals. Difícil diferenciar de grau 0. Confirmar amb signes clínics."
    elif 3 <= puntuacio_total <= 5:
        estadi = "2 - Lleu"
        interpretacio = "Signes inicials compatibles amb EOTRH."
    elif 6 <= puntuacio_total <= 9:
        estadi = "3 - Moderat"
        interpretacio = "Indicadors radiogràfics clars."
    else:
        estadi = "4 - Greu"
        interpretacio = "Coincideix amb signes clínics greus."

    # Resultats finals
    print("\n--- Resultat del qüestionari radiogràfic ---")
    print(f"Puntuació total radiogràfica: {puntuacio_total}")
    print(f"Estadi radiogràfic: {estadi}")
    print(f"Interpretació: {interpretacio}")
    return puntuacio_total

if __name__ == "__main__":
    pregunta_signes_radiografics()
>>>>>>> 1736fc1f53b3ec1b8122c0cf47bda573e9848b82
    