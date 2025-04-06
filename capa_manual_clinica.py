# Aquesta capa permet al veterinari introduir manualment els signes clínics observats en el pacient.
# S'avaluen signes clínics segons la taula de Tretow et al. (2025)

import questionary

def pregunta_signes_clinics():
    puntuacio_total = 0
    
    # Fístules
    resposta_fistules = questionary.select(
        "Fístules:",
        choices=[
            "1 purulenta i fins a 3 seroses (1 punt)",
            "2-3 purulentes o 4-6 seroses (2 punts)",
            ">3 purulentes o >6 seroses (3 punts)"
        ]).ask()
    puntuacio_total += int(resposta_fistules[resposta_fistules.find('(')+1])

    # Recessió gingival
    resposta_recessio = questionary.select(
        "Recessió gingival:",
        choices=[
            "<1/3 de l'arrel exposada (1 punt)",
            "<2/3 de l'arrel exposada (2 punts)",
            "Tota l'arrel exposada (3 punts)"
        ]).ask()
    puntuacio_total += int(resposta_recessio[resposta_recessio.find('(')+1])

    # Engrandiment bulbós visible de la regió alveolar
    resposta_bulbos = questionary.select(
        "Engrandiment bulbós visible de la regió alveolar:",
        choices=[
            "No (0 punts)",
            "Sí (1 punt)"
        ]).ask()
    puntuacio_total += int(resposta_bulbos[resposta_bulbos.find('(')+1])

    # Gingivitis
    resposta_gingivitis = questionary.select(
        "Gingivitis:",
        choices=[
            "Focal (1 punt)",
            "Difusa (2 punts)",
            "Coloració blavosa (3 punts)"
        ]).ask()
    puntuacio_total += int(resposta_gingivitis[resposta_gingivitis.find('(')+1])

    # Angle de mossegada
    resposta_mossegada = questionary.select(
        "Angle de mossegada no correlacionat amb l'edat:",
        choices=[
            "15 anys amb angle pincer (1 punt)",
            ">15 anys amb angle intermig (2 punts)",
            ">15 anys amb angle pincer (3 punts)"
        ]).ask()
    puntuacio_total += int(resposta_mossegada[resposta_mossegada.find('(')+1])

    # Classificació segons la puntuació total
    if puntuacio_total == 0:
        estadi, comentari = "0 - Cap troballa, sa", "Normalitat clínica. No es pot excloure afectació subclínica."
    elif 1 <= puntuacio_total <= 2:
        estadi, comentari = "1 - Sospitós", "Signes clínics mínims. Pot correspondre a estadis molt inicials."
    elif 3 <= puntuacio_total <= 5:
        estadi, comentari = "2 - Lleu", "Presència de signes clínics clars però localitzats."
    elif 6 <= puntuacio_total <= 9:
        estadi, comentari = "3 - Moderat", "Signes clínics múltiples i intensitat mitjana."
    else:
        estadi, comentari = "4 - Greu", "Afectació clínica generalitzada i severa."

    # Resultats finals
    print("\n--- Resultat del qüestionari clínic ---")
    print(f"Puntuació total: {puntuacio_total}")
    print(f"Estadi clínic: {estadi}")
    print(f"Interpretació: {comentari}")
    return puntuacio_total

if __name__ == "__main__":
    pregunta_signes_clinics()
   

