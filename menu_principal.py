import questionary
<<<<<<< HEAD
from capa_manual_clinica import ask_clinical_signs
from capa_manual_radiografica import ask_radiographic_signs
from analisi_automatica import automatic_analysis

def integrated_score(clinical_score, radio_score, digital_score):
    # Apply specific weights for each layer (normalized over 41 points)
    normalized_clinical_score = clinical_score * (41 * 0.4 / 17)   # maximum 16.4
    normalized_radio_score = radio_score * (41 * 0.4 / 14)       # maximum 16.4
    normalized_digital_score = digital_score * (41 * 0.2 / 10)   # maximum 8.2

    total = normalized_clinical_score + normalized_radio_score + normalized_digital_score
    rounded_total = round(total)

    if rounded_total <= 12:
        classification = "Low suspicion of EOTRH"
        interpretation = "Insufficient clinical and radiographic evidence. Routine follow-up and examination recommended."
    elif 13 <= rounded_total <= 25:
        classification = "Moderate suspicion of EOTRH"
        interpretation = "Some signs compatible with EOTRH. Periodic clinical follow-up recommended to monitor progression."
    elif 26 <= rounded_total <= 34:
        classification = "High suspicion of EOTRH"
        interpretation = "Clear coincidence between clinical, radiographic and digital signs. Immediate evaluation required."
    else:
        classification = "Very high suspicion of severe EOTRH"
        interpretation = "Strong and consistent indicators. Urgent therapeutic action recommended."

    print("\n--- FINAL INTEGRATED RESULT ---")
    print(f"Total integrated score: {rounded_total}/41")
    print(f"Classification: {classification}")
    print(f"Interpretation: {interpretation}")


# Main menu
def main_menu():
    print("\nEarly EOTRH Diagnostic Software")
    print("Select the layers to perform:")

    clinical_score = radio_score = digital_score = 0

    # Ask for manual layers first
    if questionary.confirm("Do you want to perform the manual clinical signs layer?").ask():
        print("\n--- MANUAL CLINICAL LAYER ---")
        clinical_score = ask_clinical_signs()

    if questionary.confirm("Do you want to perform the manual radiographic signs layer?").ask():
        print("\n--- MANUAL RADIOGRAPHIC LAYER ---")
        radio_score = ask_radiographic_signs()

    # Ask for digital layer only at the end
    if questionary.confirm("Do you want to perform the automatic digital layer?").ask():
        print("\n--- AUTOMATIC DIGITAL LAYER ---")
        digital_score = automatic_analysis()

    integrated_score(clinical_score, radio_score, digital_score)

if __name__ == "__main__":
    main_menu()
=======
from capa_manual_clinica import pregunta_signes_clinics
from capa_manual_radiografica import pregunta_signes_radiografics
from analisi_automatica import analisi_automatica

def puntuacio_integrada(puntuacio_clinica, puntuacio_radio, puntuacio_digital):
    # Aplicar els pesos específics per a cada capa (normalitzat sobre 41 punts)
    puntuacio_clinica_normal = puntuacio_clinica * (41 * 0.4 / 17)   # màxim 16.4
    puntuacio_radio_normal = puntuacio_radio * (41 * 0.4 / 14)       # màxim 16.4
    puntuacio_digital_normal = puntuacio_digital * (41 * 0.2 / 10)   # màxim 8.2

    total = puntuacio_clinica_normal + puntuacio_radio_normal + puntuacio_digital_normal
    total_arrodonit = round(total)

    if total_arrodonit <= 12:
        classificacio = "Baixa sospita d’EOTRH"
        interpretacio = "No hi ha prou evidència clínica ni radiogràfica. Es recomana seguiment i exploració rutinària."
    elif 13 <= total_arrodonit <= 25:
        classificacio = "Sospita moderada d’EOTRH"
        interpretacio = "Alguns indicis compatibles amb EOTRH. Es recomana seguiment clínic periòdic per controlar l’evolució."
    elif 26 <= total_arrodonit <= 34:
        classificacio = "Alta sospita d’EOTRH"
        interpretacio = "Coincidència clara entre signes clínics, radiogràfics i digitals. Avaluació immediata."
    else:
        classificacio = "Molt alta sospita d’EOTRH greu"
        interpretacio = "Indicadors forts i coherents. Es recomana actuació terapèutica urgent."

    print("\n--- RESULTAT FINAL INTEGRAT ---")
    print(f"Puntuació total integrada: {total_arrodonit}/41")
    print(f"Classificació: {classificacio}")
    print(f"Interpretació: {interpretacio}")


# Menú principal
def menu_principal():
    print("\nSoftware diagnòstic precoç EOTRH")
    print("Selecciona les capes a realitzar:")

    puntuacio_clinica = puntuacio_radio = puntuacio_digital = 0

    # Demanar primer les capes manuals
    if questionary.confirm("Vols realitzar la capa manual de signes clínics?").ask():
        print("\n--- CAPA CLÍNICA MANUAL ---")
        puntuacio_clinica = pregunta_signes_clinics()

    if questionary.confirm("Vols realitzar la capa manual de signes radiogràfics?").ask():
        print("\n--- CAPA RADIOLÒGICA MANUAL ---")
        puntuacio_radio = pregunta_signes_radiografics()

    # Demanar la capa digital només al final
    if questionary.confirm("Vols realitzar la capa digital automàtica?").ask():
        print("\n--- CAPA DIGITAL AUTOMÀTICA ---")
        puntuacio_digital = analisi_automatica()

    puntuacio_integrada(puntuacio_clinica, puntuacio_radio, puntuacio_digital)

if __name__ == "__main__":
    menu_principal()
>>>>>>> 1736fc1f53b3ec1b8122c0cf47bda573e9848b82
