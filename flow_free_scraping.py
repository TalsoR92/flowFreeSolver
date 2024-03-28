import pyautogui
import time
import os
from pynput import keyboard
import numpy as np
from PIL import Image
import cv2
import pytesseract
from collections import Counter
import math

from colormath.color_conversions import convert_color
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_diff import delta_e_cie2000


def on_click_main():
    def on_click(x, y, button, pressed):
        if pressed and button == mouse.Button.left:  # Vérifie si le clic est le bouton gauche de la souris
            print(f"Position du clic : X = {x}, Y = {y}")

    # Crée une instance de détecteur de clic de souris
    listener = mouse.Listener(on_click=on_click)

    # Démarre le détecteur de clic de souris
    listener.start()

    # Garde le programme en cours d'exécution
    listener.join()


def on_key_press(key):
    if key == keyboard.Key.esc:
        # Arrêter le programme
        return False

def capture_et_cliquer(position, nb_levels, nb_taille):
    first = 2

    # Création du dossier pour les captures d'écran s'il n'existe pas déjà

    ##dossier_captures = f"screen_shot/board_{5}-{5}"

    os.makedirs(dossier_captures, exist_ok=True)

    # Capture de l'écran
    screenshot = pyautogui.screenshot()

    # Clique sur la position spécifiée
    pyautogui.click(position[0], position[1])

    # Enregistrement de la capture d'écran dans le dossier approprié
    nom_fichier = f"capture_{1}.png"
    chemin_fichier = os.path.join(dossier_captures, nom_fichier)
    screenshot.save(chemin_fichier)

    pyautogui.sleep(0.7)

    for taille in range(5, 5 + nb_taille + 1):
        # Création du dossier pour les captures d'écran s'il n'existe pas déjà
        dossier_captures = f"screen_shot/board_{taille}-{taille}"
        os.makedirs(dossier_captures, exist_ok=True)
        pyautogui.sleep(0.1)

        # Attente de la touche Échap pour arrêter le programme
        listener = keyboard.Listener(on_press=on_key_press)
        listener.start()

        # Boucle pour les captures d'écran suivantes
        for level in range(first, nb_levels+1):
            # Vérification si la touche Échap a été pressée
            if not listener.is_alive():
                return

            # Capture de l'écran
            screenshot = pyautogui.screenshot()

            # Enregistrement de la capture d'écran dans le dossier approprié
            nom_fichier = f"capture_{level}.png"
            chemin_fichier = os.path.join(dossier_captures, nom_fichier)
            screenshot.save(chemin_fichier)
            

            # Simulation de l'appui sur la touche Entrée
            pyautogui.press('enter')

            pyautogui.sleep(0.7)
           
        first = 1



def filter_board_contours(contours):
    board_contours = []
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)

        # Filtrer les contours avec 4 côtés (rectangles ou carrés)
        if len(approx) == 4:
            board_contours.append(approx)

    return board_contours


def iterate_files_in_folder(folder_path):
    # Vérifier si le chemin est un dossier
    if not os.path.isdir(folder_path):
        print(f"Erreur : '{folder_path}' n'est pas un dossier.")
        return
    
    # Parcourir les dossiers et les fichiers dans le dossier donné
    for root, dirs, files in os.walk(folder_path):
        # Parcourir les fichiers
        for file in files:
            file_path = os.path.join(root, file)
            
            # Obtenir le chemin complet avec le nom des deux dossiers
            folder_path_with_file = os.path.abspath(file_path)
            
            crop_screenshot(folder_path_with_file)

            print(folder_path_with_file)

def afficher_point(image_path, coordinates):
    # Charger l'image
    image = cv2.imread(image_path)

    # Dessiner un point vert sur l'image à l'emplacement spécifié
    cv2.circle(image, coordinates, 5, (0, 255, 0), -1)

    # Afficher l'image avec le point vert
    cv2.imshow("Image avec point vert", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def detect_horizontal_lines(image_path, output_path):
    # Chargement de l'image
    image = cv2.imread(image_path)

    # Conversion en niveaux de gris
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Application du filtre de Canny pour détecter les contours
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Détection des lignes avec la transformée de Hough
    lines = cv2.HoughLinesP(edges, 1, math.pi/180, threshold=100, minLineLength=100, maxLineGap=10)

    # Affichage du nombre de lignes détectées avant le triage
    print("Nombre de lignes détectées avant le triage :", len(lines) if lines is not None else 0)

    # Stockage des traits et de leurs tailles
    stored_lines = []
    stored_lengths = []

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            angle = math.atan2(y2 - y1, x2 - x1) * 180 / math.pi
            if abs(angle) < 10 or abs(angle - 180) < 10:
                stored_lines.append((x1, y1, x2, y2))
                length = abs(x2 - x1)  # Utiliser la longueur horizontale
                stored_lengths.append(length)

    # print("Tailles des traits sélectionnés :")
    # for length in stored_lengths:
    #     print(length)

    # Affichage des tailles des traits stockés avant la sélection
    # print("Tailles des traits stockés avant la sélection :", stored_lengths)

    # Comptage des tailles des traits
    length_counts = Counter(stored_lengths)

    # Recherche de la taille de trait la plus fréquente
    most_common_length = length_counts.most_common(1)[0][0]

    # Sélection des traits ayant une taille similaire à la taille la plus fréquente +/- 6
    selected_lines = []
    for line in stored_lines:
        line_length = abs(line[2] - line[0])
        similar_lines = [l for l in stored_lines if abs(abs(l[2] - l[0]) - line_length) <= 6]
        if len(similar_lines) >= len(selected_lines):
            selected_lines = similar_lines

    # Calcul des médianes des coordonnées x des extrémités gauche et droite
    median_left = np.median([line[0] for line in selected_lines])
    median_right = np.median([line[2] for line in selected_lines])

    # Sélection finale des traits en vérifiant la différence par rapport aux médianes
    final_selected_lines = []
    for line in selected_lines:
        diff_left = abs(line[0] - median_left)
        diff_right = abs(line[2] - median_right)
        if diff_left <= 10 and diff_right <= 10:
            final_selected_lines.append(line)

    # print(f"\n\n final_selected_lines : {final_selected_lines} \n et nb = {len(final_selected_lines)}  \n\n")

    # Suppression des lignes proches
    final_selected_lines = remove_close_lines_horizontal(final_selected_lines)

    # Affichage du nombre de lignes détectées après le triage final
    print(f"\n\nlast nb of lines : {len(final_selected_lines)} \n \n\n")

    # Traçage des lignes horizontales sélectionnées sur l'image
    for line in final_selected_lines:
        x1, y1, x2, y2 = line
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Enregistrement de l'image avec les lignes tracées
    cv2.imwrite(output_path, image)
    # print(f"\n\n {final_selected_lines}")

    # Récupération des coordonnées du trait le plus haut et le plus bas
    top_line = min(final_selected_lines, key=lambda line: line[1])
    bottom_line = max(final_selected_lines, key=lambda line: line[3])

    # Renvoi des coordonnées sous forme de tuples (x, y)
    return (
        len(final_selected_lines) - 1,
        (top_line[0], top_line[1]),
        (top_line[2], top_line[3]),
        (bottom_line[0], bottom_line[1]),
        (bottom_line[2], bottom_line[3])
    )

def detect_vertical_lines(image_path, output_path):
    # Chargement de l'image
    image = cv2.imread(image_path)

    # Conversion en niveaux de gris
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Application du filtre de Canny pour détecter les contours
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Détection des lignes avec la transformée de Hough
    lines = cv2.HoughLinesP(edges, 1, math.pi/180, threshold=100, minLineLength=100, maxLineGap=10)

    # Affichage du nombre de lignes détectées avant le triage
    # print("Nombre de lignes détectées avant le triage :", len(lines) if lines is not None else 0)

    # Stockage des traits et de leurs tailles
    stored_lines = []
    stored_lengths = []

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            angle = math.atan2(y2 - y1, x2 - x1) * 180 / math.pi
            if abs(angle) > 80 and abs(angle) < 100:
                stored_lines.append((x1, y1, x2, y2))
                length = abs(y2 - y1)  # Utiliser la longueur horizontale
                stored_lengths.append(length)
                    
    # print("stored_lines:", len(stored_lines))
    # print("stored_lengths:", len(stored_lengths))

    # Affichage des tailles des traits stockés avant la sélection
    # print("Tailles des traits stockés avant la sélection :", stored_lengths)

    # Comptage des tailles des traits
    length_counts = Counter(stored_lengths)

    # Recherche de la taille de trait la plus fréquente
    most_common_length = length_counts.most_common(1)[0][0]
    # print(f"most_common_lenght = {most_common_length}")
    # Sélection des traits ayant une taille similaire à la taille la plus fréquente +/- 6
    selected_lines = []
    for line in stored_lines:
        line_length = abs(line[3] - line[1])
        similar_lines = [l for l in stored_lines if abs(abs(l[3] - l[1]) - line_length) <= 6]
        if len(similar_lines) >= len(selected_lines):
            selected_lines = similar_lines

    # Affichage des tailles des traits sélectionnés
    selected_lengths = [abs(line[3] - line[1]) for line in selected_lines]

    

    # Calcul des médianes des coordonnées y des extrémités supérieure et inférieure
    median_top = np.median([line[1] for line in selected_lines])
    median_bottom = np.median([line[3] for line in selected_lines])

    # Sélection finale des traits en vérifiant la différence par rapport aux médianes
    final_selected_lines = []
    for line in selected_lines:
        diff_top = abs(line[1] - median_top)
        diff_bottom = abs(line[3] - median_bottom)
        if diff_top <= 10 and diff_bottom <= 10:
            final_selected_lines.append(line)

    # print(f"\n\n list of lines : {final_selected_lines} \n and nb : {len(final_selected_lines)}")

    # Suppression des lignes proches
    final_selected_lines = remove_close_lines_vertical(final_selected_lines)
    
    # Affichage du nombre de lignes détectées après le triage final
    print("Nombre de lignes détectées après le triage final :", len(final_selected_lines))
    
    # final_selected_lines = final_selected_lines[]

    # Traçage des lignes verticales sélectionnées sur l'image
    for line in final_selected_lines:
        x1, y1, x2, y2 = line
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Enregistrement de l'image avec les lignes tracées
    cv2.imwrite(output_path, image)

    # Récupération des coordonnées de la ligne la plus à gauche et la plus à droite
    left_line = min(final_selected_lines, key=lambda line: line[0])
    right_line = max(final_selected_lines, key=lambda line: line[2])

    # Renvoi des coordonnées sous forme de tuples (x, y)
    return (len(final_selected_lines) - 1, (left_line[0], left_line[1]), (left_line[2], left_line[3]), (right_line[0], right_line[1]), (right_line[2], right_line[3]))

# detect_horizontal_lines("capture_26.png", "lines_26.png")


# remove duplicates horizontal ligne 
def remove_close_lines_horizontal(lines):
    # Suppression des lignes proches
    final_selected_lines = []
    tolerance = 6
    for line in lines:
        x1, y1, x2, y2 = line
        close_line = False
        for other_line in final_selected_lines:
            if abs(other_line[1] - y1) <= tolerance:
                # print(f"other_ligne y : {other_line[1]} || y1 : {y1}")
                close_line = True
                break
        if not close_line:
            final_selected_lines.append(line)
    return final_selected_lines

# remove duplicates vertical ligne 
def remove_close_lines_vertical(lines):
    # Suppression des lignes proches
    final_selected_lines = []
    tolerance = 6
    for line in lines:
        x1, y1, x2, y2 = line
        close_line = False
        for other_line in final_selected_lines:
            if abs(other_line[0] - x1) <= tolerance:
                # print(f"other_ligne y : {other_line[1]} || y1 : {x1}")
                close_line = True
                break
        if not close_line:
            final_selected_lines.append(line)
    return final_selected_lines


# create image with vertical and horitontal lignes
def draw_lines(image_path, output_path):
    (nb_y,top_left1, top_right1, bottom_left1, bottom_right1) = detect_horizontal_lines(image_path, output_path)
    print(f"nb vertical square in board= {nb_y}")
    
    (nb_x,bottom_left2, top_left2, bottom_right2, top_right2) = detect_vertical_lines(output_path, output_path)
    print(f"nb horizontal square in board= {nb_x}")

    distance_margin = 7  # Marge de distance acceptée

    # afficher_point(image_path, top_right1)

    # print((nb_y,top_left1, top_right1, bottom_left1, bottom_right1))
    # print((nb_x,top_left2, top_right2, bottom_left2, bottom_right2))
    # print()
    # exit(0)

    if (
        math.dist(top_left1, top_left2) > distance_margin
        or math.dist(top_right1, top_right2) > distance_margin
        or math.dist(bottom_left1, bottom_left2) > distance_margin
        or math.dist(bottom_right1, bottom_right2) > distance_margin
    ):
        print(math.dist(top_left1, top_left2))
        print(math.dist(top_right1, top_right2))
        print(math.dist(bottom_left1, bottom_left2))
        print(math.dist(bottom_right1, bottom_right2))
        print()

        print("Les traits horizontaux et verticaux ne concordent pas.")
        sys.exit(0)

    return [nb_x, nb_y, (top_left1, top_right1, bottom_left1, bottom_right1)]
    

def crop_image(image_path, output_path, top_left, top_right, bottom_left, bottom_right):
    # Chargement de l'image
    image = cv2.imread(image_path)

    # Conversion des coordonnées en np.ndarray
    top_left = np.array(top_left)
    top_right = np.array(top_right)
    bottom_left = np.array(bottom_left)
    bottom_right = np.array(bottom_right)

    # Définition des dimensions du carré de sortie
    width = max(np.linalg.norm(top_left - top_right), np.linalg.norm(bottom_left - bottom_right))
    height = max(np.linalg.norm(top_left - bottom_left), np.linalg.norm(top_right - bottom_right))

    # Définition des coordonnées des coins du carré de sortie
    dst_points = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

    # Calcul de la matrice de transformation affine
    src_points = np.float32([top_left, top_right, bottom_left, bottom_right])
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)

    # Application de la transformation affine pour recadrer l'image
    cropped_image = cv2.warpPerspective(image, matrix, (int(width), int(height)))

    # Enregistrement de l'image recadrée
    cv2.imwrite(output_path, cropped_image)


def all_crop_image_in_folder(input_path, output_path, output_path_final):
    # Vérification et création du répertoire de sortie
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    if not os.path.exists(output_path_final):
        os.makedirs(output_path_final)

    # Parcours de tous les fichiers dans le répertoire d'entrée
    for filename in os.listdir(input_path):
        if filename.endswith(".png"):
            # Chemin complet du fichier d'entrée
            image_path = os.path.join(input_path, filename)

            # Nom de fichier de sortie pour l'étape de détection des lignes
            lines_output_path = os.path.join(output_path, f"lines_{filename}")

            # Nom de fichier de sortie final pour le recadrage
            final_output_path = os.path.join(output_path_final, f"final_{filename}")

            # Détection des lignes horizontales et récupération des coordonnées
            top_left, top_right, bottom_left, bottom_right = detect_horizontal_lines(image_path, lines_output_path)

            # Recadrage de l'image selon les coordonnées obtenues
            crop_image(image_path, final_output_path, top_left, top_right, bottom_left, bottom_right)


def display_images_in_folder(folder_path, time_delay_sec):
    # Liste des fichiers d'images dans le dossier
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if len(image_files) == 0:
        print("Aucune image trouvée dans le dossier.")
        return

    # Parcours des fichiers d'images
    for image_file in image_files:
        # Chemin complet de l'image
        image_path = os.path.join(folder_path, image_file)

        # Lecture de l'image
        image = cv2.imread(image_path)

        # Affichage de l'image
        cv2.imshow("Image", image)
        cv2.waitKey(int(time_delay_sec * 1000))  # Conversion du délai en millisecondes

    # Fermeture de la fenêtre d'affichage
    cv2.destroyAllWindows()

# make flow matrice with board cut image
def generate_flow_matrix(image_path, dimension):
    # Chargement de l'image
    image = cv2.imread(image_path)

    # Calcul des dimensions de chaque case et du carré de pixels
    rows, cols, _ = image.shape
    case_width = cols // dimension[0]
    case_height = rows // dimension[1]
    pixel_square_size = case_width // 2
    print(dimension)
    # Définition de la matrice de flow avec le type de données "object"
    flow_matrix = np.empty((dimension[1], dimension[0]), dtype=object)

    for i in range(dimension[1]):
        for j in range(dimension[0]):
            # Coordonnées du centre de la case
            center_x = (j * case_width) + (case_width // 2)
            center_y = (i * case_height) + (case_height // 2)

            # Coordonnées du carré de pixels au centre de la case
            square_x_start = center_x - (pixel_square_size // 2)
            square_x_end = square_x_start + pixel_square_size
            square_y_start = center_y - (pixel_square_size // 2)
            square_y_end = square_y_start + pixel_square_size

            # Récupération des couleurs des pixels dans le carré
            colors = image[square_y_start:square_y_end, square_x_start:square_x_end]
            colors = colors.reshape(-1, 3)  # Reshape pour obtenir une liste de pixels

            # Comptage des couleurs dans le carré
            color_counts = Counter(tuple(pixel) for pixel in colors)
            most_common_color = color_counts.most_common(1)[0][0]
            b, g, r = most_common_color
            
            # print(f"i = {i} and j = {j}")

            # Conversion de la couleur en chaîne de caractères
            color_string = find_closest_color(r, g, b)
            # print(color_string)
            # Assignation de la couleur à la case correspondante dans la matrice de flow
            flow_matrix[i, j] = color_string

            # Affichage de la couleur de chaque pixel au centre de la case
            # print(f"Case ({i}, {j}) : R={r}, G={g}, B={b} ({color_string})")
    print(len(flow_matrix))
    print(len(flow_matrix[0]))
    # Affichage de la matrice de flow
    for row in flow_matrix:
        print(*[elem if elem else "-" for elem in row])
    
    return flow_matrix

# find color of a screen shot of board
def get_color_name(r, g, b):
    # Liste de noms de couleurs et leurs plages de valeurs RGB
    colors = {
        ((180, 255), (0, 50), (0, 50)): "Red",
        ((0, 50), (120, 140), (0, 50)): "Green",
        ((0, 10), (0, 10), (180, 255)): "Blue",
        ((180, 255), (180, 255), (0, 50)): "Yellow",
        ((0, 50), (180, 255), (180, 255)): "Cyan",
        ((180, 255), (0, 50), (180, 255)): "Magenta",
        ((200, 255), (100, 180), (0, 50)): "Orange",
        ((128, 128), (0, 10), (128, 128)): "Purple",
        ((180, 255), (180, 255), (180, 255)): "White",
        ((160, 170), (40, 50), (40, 50)): "Brown"
    }

    # Parcourir les couleurs et vérifier si la couleur donnée correspond à une couleur de référence
    for ranges, color_name in colors.items():
        in_range = all([r_range[0] <= r <= r_range[1] for r, r_range in zip((r, g, b), ranges)])
        if in_range:
            return color_name

    # Retourner une chaîne vide si aucune couleur correspondante n'est trouvée
    return ""

# find closest color of a picture of board
def find_closest_color(r, g, b):
    colors = {
        "Red": (255, 0, 0),
        "Green": (0, 255, 0),
        "Blue": (0, 0, 255),
        "Yellow": (255, 255, 0),
        "Cyan": (0, 255, 255),
        "Magenta": (255, 0, 255),
        "Orange": (255, 165, 0),
        "Purple": (128, 0, 128),
        "White": (255, 255, 255),
        "Brown": (165, 42, 42)
    }

    closest_color = ""
    closest_distance = float('inf')

    for color, rgb in colors.items():
        distance = ((r - rgb[0]) ** 2) + ((g - rgb[1]) ** 2) + ((b - rgb[2]) ** 2)
        if distance < closest_distance:
            closest_distance = distance
            closest_color = color
    
    if closest_color == "" or (closest_color == "Brown" and closest_distance > 450):  # Couleur très sombre ou aucune correspondance
        # print(closest_color)
        # print(closest_distance)
        # print(f"r = {r}, g = {g}, b = {b} ")
        # print()
        return ""

    # print(closest_color)
    # print(f"r = {r}, g = {g}, b = {b} ")
    # print()
    return closest_color

def create_green_points(image_path, dimension, output_path):
    # Chargement de l'image
    image = cv2.imread(image_path)

    # Calcul des dimensions de chaque case
    rows, cols, _ = image.shape
    case_width = cols // dimension
    case_height = rows // dimension

    # Parcourir chaque case et créer un point vert au milieu
    for i in range(dimension):
        for j in range(dimension):
            # Coordonnées du centre de la case
            center_x = (j * case_width) + (case_width // 2)
            center_y = (i * case_height) + (case_height // 2)

            # Dessiner un point vert sur l'image à l'emplacement spécifié
            cv2.circle(image, (center_x, center_y), 5, (0, 255, 0), -1)

    # Enregistrer l'image avec les points verts
    cv2.imwrite(output_path, image)

def image_to_flow_matrice(image_path, output_path):
    similarity_margin = 4  # Définir la marge de similarité
    res = draw_lines(image_path, output_path)
    

    nb_x = res[0]
    nb_y = res[1]
    # print("res = ")
    # print(res)
    (top_left, top_right, bottom_left, bottom_right) = res[2]

    
    crop_image(output_path, output_path, top_left, top_right, bottom_left, bottom_right)

    
    return (generate_flow_matrix(output_path, (nb_x,nb_y)),nb_x,nb_y)


# detect_horizontal_lines("capture_1.png", "test_with_lines_horizontal.png")

# image_to_flow_matrice("IMG_5168.png", "test.png")

# draw_lines("capture_1.png", "test_with_all_lignes.png")
# detect_vertical_lines("capture_1.png", "test_with_lines_vertical.png")


# Exemple d'utilisation

# image_path = "screen_shot_v3/board_9-9/final_capture_1.png"


# # create_green_points(image_path, 5, "test.png")


# # display_images_in_folder("screen_shot_v3/board_9-9", 0.4)

# generate_flow_matrix(image_path,9)

# all_crop_image_in_folder("screen_shot_v2/board_9-9", "screen_shot_v3/intermediare_board_9-9","screen_shot_v3/board_9-9")



# top_left, top_right, bottom_left, bottom_right = detect_horizontal_lines(image_path, "final_image.png")


# crop_image(image_path, "final_image_v2.png", top_left, top_right, bottom_left, bottom_right)



# afficher_point("final_image.png", bottom_right)


# recadrer_image(image_path, top_left, top_right, bottom_left, bottom_right, "image_rogne.png")
# top_corners, bottom_corners = find_plateau_corners(image_path)

# print("Sommet supérieur gauche :", top_corners[0])
# print("Sommet supérieur droit :", top_corners[1])
# print("Sommet inférieur gauche :", bottom_corners[0])
# print("Sommet inférieur droit :", bottom_corners[1])

# crop_image(image_path, top_corners[0], top_corners[1], bottom_corners[0], bottom_corners[1], "final_image.png")



images_folder = "screen_shot_v2"

