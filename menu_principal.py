import questionary
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
