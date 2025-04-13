import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import PolygonSelector
from matplotlib.path import Path as MplPath
from skimage.transform import resize
from skimage import exposure
from EntropyHub import DistEn2D

# ────────────────────────────────
# AUXILIARY FUNCTIONS
# ────────────────────────────────

def distEn2D_screening_classification(dist_en_val):
    if dist_en_val < 0.81:
        category = "No digital alterations"
        interpretation = "No clear texture changes detected. Mild EOTRH cannot be ruled out. Clinical examination recommended."
        points = 0
    elif dist_en_val <= 0.87:
        category = "Digital suspicion"
        interpretation = "Alterations compatible with EOTRH detected. Severity undetermined. Manual confirmation required."
        points = 5
    else:
        category = "Strong suspicion of EOTRH"
        interpretation = "Marked digital changes. Compatible with moderate or severe EOTRH. Immediate evaluation recommended."
        points = 10

    return category, interpretation, points

def load_and_prepare_image():
    filename = input("📂 Enter the radiograph file name (e.g., sana.jpg): ")
    image = cv2.imread(filename)
    if image is None:
        print("❌ Error: could not load the image.")
        exit()

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rescaled_image = exposure.rescale_intensity(gray_image, in_range='image', out_range=(0, 255))
    return rescaled_image

def select_polygon_roi(image, tooth):
    print(f"\n🖱️ Draw the polygonal ROI over tooth {tooth} and close the contour with double click")
    coords = []

    def onselect(verts):
        coords.extend(verts)
        plt.close()

    fig, ax = plt.subplots()
    ax.imshow(image, cmap='gray')
    ax.set_title(f"Draw the shape of tooth {tooth}")
    selector = PolygonSelector(ax, onselect, useblit=True)
    plt.show()

    if not coords:
        print("❌ No shape was selected.")
        exit()

    return np.array(coords)

def extract_polygonal_roi(image, vertices):
    mask = np.zeros_like(image, dtype=bool)
    path = MplPath(vertices)
    X, Y = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0]))
    points = np.vstack((X.flatten(), Y.flatten())).T
    mask[Y, X] = path.contains_points(points).reshape(image.shape)
    return image * mask, mask

def calculate_distEn2D(roi_masked):
    roi_vals = roi_masked[roi_masked > 0]
    if roi_vals.size == 0:
        print("❌ Empty ROI.")
        return 0.0
    if np.std(roi_vals) < 1e-6:
        print("⚠️ ROI with homogeneous texture. STD ≈ 0.")
        return 0.0

    roi_resized = resize(roi_vals.reshape(-1, 1), (128, 128), anti_aliasing=True)
    roi_normalized = (roi_resized - np.mean(roi_resized)) / (np.std(roi_resized) + 1e-8)

    try:
        dist = DistEn2D(roi_normalized, m=2, tau=1, Logx=False)
        return round(dist, 4)
    except Exception as e:
        print(f"❌ Error calculating DistEn2D: {e}")
        return 0.0

def show_result(tooth, value):
    category, interpretation, points = distEn2D_screening_classification(value)
    print(f"\n📘 Results for tooth {tooth}:")
    print(f"🧠 DistEn2D: {value:.4f}")
    print(f"📊 Category: {category}")
    print(f"💬 Interpretation: {interpretation}")
    print(f"⭐ Automatic points: {points}/10")

# ────────────────────────────────
# MAIN FUNCTION
# ────────────────────────────────

def automatic_analysis():
    image = load_and_prepare_image()

    print("\n==============================")
    print("🦷 Analysis of tooth 101")
    verts1 = select_polygon_roi(image, "101")
    roi1, _ = extract_polygonal_roi(image, verts1)
    value1 = calculate_distEn2D(roi1)
    show_result("101", value1)

    print("\n==============================")
    print("🦷 Analysis of tooth 201")
    verts2 = select_polygon_roi(image, "201")
    roi2, _ = extract_polygonal_roi(image, verts2)
    value2 = calculate_distEn2D(roi2)
    show_result("201", value2)

if __name__ == "__main__":
    automatic_analysis()
