import cv2
import numpy as np

def detect_and_crop_flow_free_board(image_path, output_path):
    # Charger l'image
    image = cv2.imread(image_path)
    
    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Appliquer un flou gaussien pour réduire le bruit
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Détection des contours avec l'algorithme de Canny
    edges = cv2.Canny(blurred, 50, 150)
    
    # Trouver les contours dans l'image
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Trouver le plus grand contour (la grille)
    largest_contour = max(contours, key=cv2.contourArea)
    
    # Calculer les coordonnées de la boîte englobante de la grille
    x, y, w, h = cv2.boundingRect(largest_contour)
    
    # Découper l'image autour de la grille
    cropped_image = image[y:y+h, x:x+w]
    
    # Sauvegarder l'image découpée
    cv2.imwrite(output_path, cropped_image)
    print(f"Image découpée enregistrée sous : {output_path}")

# Exemple d'utilisation de la fonction
image_path = 'screen_examples/capture_1.png'
output_path = 'screen_examples/cropped_image.png'
# cropped_image = detect_and_crop_flow_free_board(image_path, output_path)


# reconnait tout les carrés de la board !!!
def colorize_detected_squares(image_path, output_path):
    # Charger l'image
    image = cv2.imread(image_path)
    
    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Appliquer un flou gaussien pour réduire le bruit
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Détection des contours avec l'algorithme de Canny
    edges = cv2.Canny(blurred, 50, 150)
    
    # Détecter les lignes droites dans l'image à l'aide de la transformation de Hough
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)
    
    # Dessiner les lignes détectées sur l'image
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    # Enregistrer l'image avec les lignes détectées
    cv2.imwrite(output_path, image)
    print(f"Image avec les lignes détectées enregistrée sous : {output_path}")

# Appeler la fonction avec le chemin de l'image d'entrée et le chemin de sortie pour l'image avec les lignes détectées
image_path = 'screen_examples/screen_iphone_11-14.png'
output_path = 'screen_examples/image_with_detected_lines_9-9.png'


# decoupe bien la board pour les 3/4
def crop_table(image_path, output_path):
    # Charger l'image
    image = cv2.imread(image_path)
    
    # Convertir l'image en HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Définir les bornes pour la couleur verte dans l'espace HSV
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([70, 255, 255])

    # Masquer l'image pour obtenir uniquement les pixels verts
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Trouver les contours des carrés verts
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sélectionner le plus grand contour (le contour extérieur du tableau)
    max_contour = max(contours, key=cv2.contourArea)

    # Approximer le contour pour obtenir un polygone
    perimeter = cv2.arcLength(max_contour, True)
    approx = cv2.approxPolyDP(max_contour, 0.04 * perimeter, True)

    # Récupérer les coordonnées du polygone
    x, y, w, h = cv2.boundingRect(approx)

    # Découper l'image pour extraire le tableau
    cropped_table = image[y:y+h, x:x+w]

    # Enregistrer l'image découpée
    cv2.imwrite(output_path, cropped_table)
    print(f"Image du tableau découpée enregistrée sous : {output_path}")

def filter_contours_with_close_neighbors(contours, threshold=50):
    filtered_contours = []
    for contour in contours:
        # Calculer la bounding box du contour
        x, y, w, h = cv2.boundingRect(contour)
        # Définir les limites de la zone de recherche pour les contours voisins
        search_area = np.array([x - threshold, y - threshold, x + w + threshold, y + h + threshold])
        # Rechercher les contours voisins dans la zone de recherche
        neighbor_contours = [c for c in contours if cv2.boundingRect(c) != (x, y, w, h) and
                             cv2.pointPolygonTest(c, (x + w // 2, y + h // 2), False) >= 0 and
                             cv2.pointPolygonTest(c, (x, y), False) >= 0 and
                             cv2.pointPolygonTest(c, (x + w, y), False) >= 0 and
                             cv2.pointPolygonTest(c, (x, y + h), False) >= 0 and
                             cv2.pointPolygonTest(c, (x + w, y + h), False) >= 0 and
                             cv2.contourArea(c) >= cv2.contourArea(contour)]
        # Si au moins un contour voisin a une taille similaire, ajouter le contour
        if len(neighbor_contours) > 0:
            filtered_contours.append(contour)
    return filtered_contours

def crop_table_v2(image_path, output_path):
    # Charger l'image
    image = cv2.imread(image_path)
    
    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Appliquer un filtre morphologique pour nettoyer l'image
    kernel = np.ones((5,5), np.uint8)
    morph_image = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    
    # Trouver les contours dans l'image nettoyée
    contours, _ = cv2.findContours(morph_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filtrer les contours pour ne garder que ceux avec des voisins de taille similaire
    filtered_contours = filter_contours_with_close_neighbors(contours)
    
    # Sélectionner le plus grand contour (le contour extérieur du tableau)
    max_contour = max(filtered_contours, key=cv2.contourArea)

    # Approximer le contour pour obtenir un polygone
    perimeter = cv2.arcLength(max_contour, True)
    approx = cv2.approxPolyDP(max_contour, 0.04 * perimeter, True)

    # Récupérer les coordonnées du polygone
    x, y, w, h = cv2.boundingRect(approx)

    # Découper l'image pour extraire le tableau
    cropped_table = image[y:y+h, x:x+w]

    # Enregistrer l'image découpée
    cv2.imwrite(output_path, cropped_table)
    print(f"Image du tableau découpée enregistrée sous : {output_path}")


image_path = 'screen_examples/capture_1.png'
output_path = 'screen_examples/image_with_detected_lines_9-9.png'
colorize_detected_squares(image_path, output_path)

# Appeler la fonction avec le chemin de l'image d'entrée et le chemin de sortie pour l'image modifiée
image_path = 'screen_examples/image_with_detected_lines_9-9.png'
output_path = 'screen_examples/image_with_squares.png'
crop_table_v2(image_path, output_path)