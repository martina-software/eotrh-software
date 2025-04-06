import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import PolygonSelector
from matplotlib.path import Path as MplPath
from skimage.transform import resize
from skimage import exposure
from EntropyHub import DistEn2D


# ────────────────────────────────
# FUNCIONS AUXILIARS
# ────────────────────────────────

def carregar_i_preparar_imatge():
    nom_arxiu = input("📂 Escriu el nom del fitxer de la radiografia (ex: sana.jpg): ")
    imatge = cv2.imread(nom_arxiu)
    if imatge is None:
        print("❌ Error: no s'ha pogut carregar la imatge.")
        exit()

    imatge_gray = cv2.cvtColor(imatge, cv2.COLOR_BGR2GRAY)
    imatge_rescalada = exposure.rescale_intensity(imatge_gray, in_range='image', out_range=(0, 255))
    return imatge_rescalada


def seleccionar_roi_poligon(imatge, posicio):
    print(f"\n🖱️ Dibuixa la ROI poligonal sobre la dent ({posicio}) i tanca el contorn amb doble clic")
    coords = []

    def onselect(verts):
        coords.extend(verts)
        plt.close()

    fig, ax = plt.subplots()
    ax.imshow(imatge, cmap='gray')
    ax.set_title(f"Dibuixa la forma de la dent ({posicio})")
    selector = PolygonSelector(ax, onselect, useblit=True)
    plt.show()

    if not coords:
        print("❌ No s'ha seleccionat cap forma.")
        exit()

    return np.array(coords)


def extreure_roi_poligonal(imatge, vertices):
    mask = np.zeros_like(imatge, dtype=bool)
    path = MplPath(vertices)
    X, Y = np.meshgrid(np.arange(imatge.shape[1]), np.arange(imatge.shape[0]))
    points = np.vstack((X.flatten(), Y.flatten())).T
    mask_flat = path.contains_points(points)
    mask[Y, X] = mask_flat.reshape(imatge.shape)
    return imatge * mask, mask


def calcular_distEn2D(roi_masked):
    roi_vals = roi_masked[roi_masked > 0]
    if roi_vals.size == 0:
        print("❌ ROI buida.")
        return 0.0
    if np.std(roi_vals) < 1e-6:
        print("⚠️ ROI amb textura homogènia. STD ≈ 0.")
        return 0.0

    roi_resized = resize(roi_vals.reshape(-1, 1), (128, 128), anti_aliasing=True)
    roi_normalitzada = (roi_resized - np.mean(roi_resized)) / (np.std(roi_resized) + 1e-8)

    try:
        dist = DistEn2D(roi_normalitzada, m=2, tau=1, Logx=False)
        return round(dist, 4)
    except Exception as e:
        print(f"❌ Error en calcular DistEn2D: {e}")
        return 0.0


def mostrar_resultat(dent, posicio, valor):
    print(f"\n📘 Resultats per la dent {dent} (ROI {posicio}):")
    print(f"🧠 DistEn2D: {valor:.4f}")
    if valor < 0.70:
        print("✅ Compatible amb dent sana.")
    elif 0.70 <= valor <= 0.95:
        print("⚠️ Canvis compatibles amb EOTRH lleu o moderat.")
    else:
        print("❌ Alteracions marcades. Compatible amb EOTRH greu.")


# ────────────────────────────────
# FUNCIO PRINCIPAL
# ────────────────────────────────

def analisi_automatica():
    imatge = carregar_i_preparar_imatge()

    # Dent 101
    print("\n==============================")
    print("🦷 Anàlisi de la dent 101")
    verts1 = seleccionar_roi_poligon(imatge, "coronal (101)")
    roi1, _ = extreure_roi_poligonal(imatge, verts1)
    valor1 = calcular_distEn2D(roi1)
    mostrar_resultat(101, "coronal", valor1)

    verts2 = seleccionar_roi_poligon(imatge, "apical (101)")
    roi2, _ = extreure_roi_poligonal(imatge, verts2)
    valor2 = calcular_distEn2D(roi2)
    mostrar_resultat(101, "apical", valor2)

    # Dent 201
    print("\n==============================")
    print("🦷 Anàlisi de la dent 201")
    verts3 = seleccionar_roi_poligon(imatge, "coronal (201)")
    roi3, _ = extreure_roi_poligonal(imatge, verts3)
    valor3 = calcular_distEn2D(roi3)
    mostrar_resultat(201, "coronal", valor3)

    verts4 = seleccionar_roi_poligon(imatge, "apical (201)")
    roi4, _ = extreure_roi_poligonal(imatge, verts4)
    valor4 = calcular_distEn2D(roi4)
    mostrar_resultat(201, "apical", valor4)

    puntuacions = [valor1, valor2, valor3, valor4]
    puntuacio_total = 0

    for valor in puntuacions:
        if valor > 0.95:
            puntuacio_total += 10
        elif 0.70 <= valor <= 0.95:
            puntuacio_total += 5
        else:
            puntuacio_total += 0

    puntuacio_final = round((puntuacio_total / 40) * 10)

    print(f"\n📊 Puntuació total automàtica ajustada: {puntuacio_final}/10")

    return puntuacio_final
