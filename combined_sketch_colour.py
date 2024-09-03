import cv2
import pygame
import sys

# Function to capture the sketch from the webcam
def capture_sketch():
    # Initialize webcam
    cap = cv2.VideoCapture(0)

    # Function to convert captured frame to a sketch
    def sketch(image):
        # Convert image to grayscale
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Apply Gaussian Blur
        img_gray_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
        # Extract edges
        canny_edges = cv2.Canny(img_gray_blur, 10, 70)
        # Invert the binary image
        ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
        return mask

    while True:
        ret, frame = cap.read()
        # Display live sketch
        cv2.imshow('Our Live Sketcher', sketch(frame))
        # Press Enter key to capture and save the sketch
        if cv2.waitKey(1) == 13:  # 13 is the Enter Key
            sketch_image = sketch(frame)
            cv2.imwrite('sketch.png', sketch_image)
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Sketch saved as 'sketch.png'. Opening coloring window...")

# Function to color the saved sketch
def open_coloring_app(image_path):
    # Initialize Pygame
    pygame.init()

    # Load the saved sketch
    sketch = pygame.image.load(image_path)

    # Set up display
    window_size = (sketch.get_width(), sketch.get_height())
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Color Your Sketch")

    # Convert sketch to a format suitable for drawing with alpha (transparency) channel
    sketch = sketch.convert_alpha()

    # Main loop variables
    drawing = False
    brush_size = 5

    # Color dictionary with keys mapped to colors
    colors = {
        'r': (255, 0, 0, 255),   # Red
        'g': (0, 255, 0, 255),   # Green
        'b': (0, 0, 255, 255),   # Blue
        'y': (255, 255, 0, 255), # Yellow
        'c': (0, 255, 255, 255), # Cyan
        'm': (255, 0, 255, 255), # Magenta
        'o': (255, 165, 0, 255), # Orange
        'p': (128, 0, 128, 255), # Purple
        'k': (0, 0, 0, 255),     # Black
        'w': (255, 255, 255, 255) # White
    }

    # Default color
    color = colors['r']  # Red

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Save the colored sketch
                pygame.image.save(sketch, 'colored_sketch.png')
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
            elif event.type == pygame.KEYDOWN:
                # Change color based on the key pressed
                key = event.unicode.lower()
                if key in colors:
                    color = colors[key]

        # Get mouse position and draw if drawing
        if drawing:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            pygame.draw.circle(sketch, color, (mouse_x, mouse_y), brush_size)

        # Display the sketch on screen
        screen.blit(sketch, (0, 0))
        pygame.display.update()

# First capture the sketch, then automatically open it in the coloring app
capture_sketch()
open_coloring_app('sketch.png')