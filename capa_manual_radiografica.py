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
    