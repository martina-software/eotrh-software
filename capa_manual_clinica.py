<<<<<<< HEAD
# This layer allows the veterinarian to manually enter the clinical signs observed in the patient.
# Clinical signs are evaluated according to the Tretow et al. (2025) table

import questionary

def ask_clinical_signs():
    total_score = 0
    
    # Fistulas
    fistula_response = questionary.select(
        "Fistulae:",
        choices=[
            "1 purulent or up to 3 serous (1 point)",
            "2-3 purulent or 4-6 serous (2 points)",
            ">3 purulent or >6 serous (3 points)"
        ]).ask()
    total_score += int(fistula_response[fistula_response.find('(')+1])

    # Gingival recession
    recession_response = questionary.select(
        "Gingival recession:",
        choices=[
            "<1/3 of the root exposed (1 point)",
            "<2/3 of root exposed (2 points)",
            "Whole root exposed (3 points)"
        ]).ask()
    total_score += int(recession_response[recession_response.find('(')+1])

    # Bulbous enlargement of the alveolar region
    bulbous_response = questionary.select(
        "Subgingval bulbous enlargement:",
        choices=[
            "No (0 points)",
            "Yes (1 point)"
        ]).ask()
    total_score += int(bulbous_response[bulbous_response.find('(')+1])

    # Gingivitis
    gingivitis_response = questionary.select(
        "Gingivitis:",
        choices=[
            "Focal (1 point)",
            "Widespread (2 points)",
            "Blueish colour (3 points)"
        ]).ask()
    total_score += int(gingivitis_response[gingivitis_response.find('(')+1])

    # Bite angle
    bite_response = questionary.select(
        "Bite angle not correlated with age:",
        choices=[
            "15 years old and pincer-like (1 point)",
            "Over 15 years old and bisection angle (2 points)",
            "Over 15 years old and pincer-like (3 points)"
        ]).ask()
    total_score += int(bite_response[bite_response.find('(')+1])

    # Classification according to total score
    if total_score == 0:
        stage, comment = "0 - No clinical findings/healthy", "Clinical normality. Subclinical involvement cannot be excluded."
    elif 1 <= total_score <= 2:
        stage, comment = "1 - Suspicious", "Minimal clinical signs. May correspond to very early stages."
    elif 3 <= total_score <= 5:
        stage, comment = "2 - Mild", "Presence of clear but localized clinical signs."
    elif 6 <= total_score <= 9:
        stage, comment = "3 - Moderate", "Multiple clinical signs and medium intensity."
    else:
        stage, comment = "4 - Severe", "Generalized and severe clinical involvement."

    # Final results
    print("\n--- Clinical questionnaire result ---")
    print(f"Total score: {total_score}")
    print(f"Clinical stage: {stage}")
    print(f"Interpretation: {comment}")
    return total_score

if __name__ == "__main__":
    ask_clinical_signs()
=======
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
>>>>>>> 1736fc1f53b3ec1b8122c0cf47bda573e9848b82
   

