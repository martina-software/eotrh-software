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
    