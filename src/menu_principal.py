import questionary
from src.capa_manual_clinica import ask_clinical_signs
from src.capa_manual_radiografica import ask_radiographic_signs
from src.analisi_automatica import automatic_analysis

def integrated_score(clinical_score, radio_score, digital_score):
    # Apply specific weights for each layer (normalized over 41 points)
    clinical_score_normal = clinical_score * (41 * 0.4 / 17)   # maximum 16.4
    radio_score_normal = radio_score * (41 * 0.4 / 14)       # maximum 16.4
    digital_score_normal = digital_score * (41 * 0.2 / 10)   # maximum 8.2

    total = clinical_score_normal + radio_score_normal + digital_score_normal
    total_rounded = round(total)

    if total_rounded <= 12:
        classification = "Low suspicion of EOTRH"
        interpretation = "Insufficient clinical and radiographic evidence. Routine follow-up and examination recommended."
    elif 13 <= total_rounded <= 25:
        classification = "Moderate suspicion of EOTRH"
        interpretation = "Some signs compatible with EOTRH. Regular clinical follow-up recommended to monitor progression."
    elif 26 <= total_rounded <= 34:
        classification = "High suspicion of EOTRH"
        interpretation = "Clear coincidence between clinical, radiographic and digital signs. Immediate evaluation required."
    else:
        classification = "Very high suspicion of severe EOTRH"
        interpretation = "Strong and consistent indicators. Urgent therapeutic action recommended."

    print("\n--- FINAL INTEGRATED RESULT ---")
    print(f"Total integrated score: {total_rounded}/41")
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
    if questionary.confirm("Do you want to perform the automatic digital analysis?").ask():
        print("\n--- AUTOMATIC DIGITAL LAYER ---")
        digital_score = automatic_analysis()

    integrated_score(clinical_score, radio_score, digital_score)

if __name__ == "__main__":
    main_menu()
