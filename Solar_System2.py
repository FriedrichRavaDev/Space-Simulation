import pygame, sys, math
from PIL import Image

# Initialize Pygame
windowWidth = 1900
windowHeight = 1200
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("path/One Hour of Soviet Music - Space Program.mp3")
pygame.mixer.music.play()
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Советская космическая программа')

# Colors
black = (0, 0, 0)
light_blue = (0, 119, 182)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

image = Image.open("path/Solar System/Earth.png")
image = image.convert('RGBA')
mode = image.mode
size = image.size
data = image.tobytes()

image_surface = pygame.image.fromstring(data, size, mode)

image1 = Image.open("path/Sun.gif")
image1 = image1.convert('RGBA')
mode1 = image1.mode
size1 = image1.size
data1 = image1.tobytes()

image_surface1 = pygame.image.fromstring(data1, size1, mode1)

image2 = Image.open("path/Moon.png")
image2 = image2.convert('RGBA')
mode2 = image2.mode
size2 = image2.size
data2 = image2.tobytes()

image_surface2 = pygame.image.fromstring(data2, size2, mode2)

image3 = Image.open("path/Mars.png")
image3 = image3.convert('RGBA')
mode3 = image3.mode
size3 = image3.size
data3 = image3.tobytes()

image_surface3 = pygame.image.fromstring(data3, size3, mode3)

image4 = Image.open("path/Sputnik1.png")
image4 = image4.convert('RGBA')
mode4 = image4.mode
size4 = image4.size
data4 = image4.tobytes()

image_surface4 = pygame.image.fromstring(data4, size4, mode4)

imageSoviet_mars = Image.open("path/Mars-1.png")
imageSoviet_mars = imageSoviet_mars.convert('RGBA')
modeSoviet_mars = imageSoviet_mars.mode
sizeSoviet_mars = imageSoviet_mars.size
dataSoviet_mars = imageSoviet_mars.tobytes()

image_surfaceSoviet_mars = pygame.image.fromstring(dataSoviet_mars, sizeSoviet_mars, modeSoviet_mars)


# Initial positions and masses
Moon_x = 400
Moon_y = 687
Moon_mass = 50

Earth_x = 500
Earth_y = 687
Earth_mass = 200

Sputnik_x = 0
Sputnik_y = 0

Mars_x = 250
Mars_y = 687
Mars_mass = 100

Solar_x = 950
Solar_y = 600
Solar_mass = 1000

class Planet:
    def __init__(self, name, x, y, mass):
        self.name = name
        self.x = x
        self.y = y
        self.mass = mass

Planets = [
    Planet("Earth", 500, 687, 200),
    Planet("Moon", 400, 687, 50),
    Planet("Mars", 250, 687, 100),
    Planet("Sun", 950, 600, 1000)
]

def calculate_gravity(planet_x, planet_y, planet_mass, sputnik_x, sputnik_y):
    # Calculate distance between Sputnik and planet
    distance_x = planet_x - sputnik_x
    distance_y = planet_y - sputnik_y
    distance = math.hypot(distance_x, distance_y)

    if distance != 0:
        # Normalized direction of the gravitational force
        nDirection = (distance_x / distance, distance_y / distance)
        
        # Calculate the magnitude of the gravitational force
        gravity = planet_mass / (distance * distance)
        
        # Return force components
        sputnik_force = (nDirection[0] * gravity, nDirection[1] * gravity)
    
        # Calculate the perpendicular direction to the gravitational force
        sputnik_direction = (-nDirection[1], nDirection[0])
        sputnik_forward_force = (sputnik_direction[0] * Sputnik_forward_magnitude, sputnik_direction[1] * Sputnik_forward_magnitude)

        return (sputnik_forward_force[0], sputnik_forward_force[1])
    return (0, 0)

# Force scaling factors
forward_force_magnitude = 2.35
Moon_forward_magnitude = 2.7
Mars_forward_magnitude = 2.4
Sputnik_forward_magnitude = 2

# Orbit path
orbit_path = []
earth_orbit_path = []
solar_orbit_path = []
mars_orbit_path = []
max_path_length = 1800  # Maximum number of points to keep in the orbit path

def draw_orbit_path(surface, path, color):
    if len(path) > 1:
        # Draw continuous lines between each pair of points in the path
        pygame.draw.lines(surface, color, False, path, 1)


running = True
Sputnik = False
clicked = False
Mars_Touched = False
angle = 0
angle1 = 0
angle2 = 0
clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            print(f'Mouse moved to ({x}, {y})')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            Sputnik = True
            x_Direction = x
            y_Direction = y

            Sputnik_x = Earth_x
            Sputnik_y = Earth_y

            Mouse_Position = (x_Direction, y_Direction)

            Sputnik_direction_x = Mouse_Position[0] - Sputnik_x
            Sputnik_direction_y = Mouse_Position[1] - Sputnik_y 

            Sputnik_magnitude = math.hypot(Sputnik_direction_x, Sputnik_direction_y)
            Sputnik_NormalisedDirection_x = (Sputnik_direction_x / Sputnik_magnitude)
            Sputnik_NormalisedDirection_y = (Sputnik_direction_y / Sputnik_magnitude)

            Sputnik_Resultant_Force_x = Sputnik_NormalisedDirection_x * Sputnik_forward_magnitude 
            Sputnik_Resultant_Force_y = Sputnik_NormalisedDirection_y * Sputnik_forward_magnitude

 #MOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOON            

    # Calculate distance between Earth and Moon
    distance_x1 = Earth_x - Moon_x
    distance_y1 = Earth_y - Moon_y
    Moon_magnitude = math.hypot(distance_x1, distance_y1)

    if Moon_magnitude != 0:
        # Normalized direction of the gravitational force
        Moon_nDirection = (distance_x1 / Moon_magnitude, distance_y1 / Moon_magnitude)
        Moon_Gravity = Earth_mass / (Moon_magnitude * Moon_magnitude) *2
        Moon_Force = (Moon_nDirection[0] * Moon_Gravity, Moon_nDirection[1] * Moon_Gravity)

        # Calculate the perpendicular direction to the gravitational force
        Moon_perpendicular_direction = (-Moon_nDirection[1], Moon_nDirection[0])
        Moon_forward_force = (Moon_perpendicular_direction[0] * Moon_forward_magnitude, Moon_perpendicular_direction[1] * Moon_forward_magnitude)

        # Update Earth's position with gravitational and forward forces
        Moon_x += Moon_Force[0] + Moon_forward_force[0]
        Moon_y += Moon_Force[1] + Moon_forward_force[1]

    # ORBIT AROUND THE SUN

    # Calculate distance between Earth and Moon
    distance_x2 = Solar_x - Moon_x
    distance_y2 = Solar_y - Moon_y
    Moon_magnitude_Solar = math.hypot(distance_x2, distance_y2)

    if Moon_magnitude_Solar != 0:
        # Normalized direction of the gravitational force
        Moon_nDirection_Solar = (distance_x2 / Moon_magnitude_Solar, distance_y2 / Moon_magnitude_Solar)
        Moon_Gravity_Solar = Solar_mass / (Moon_magnitude_Solar * Moon_magnitude_Solar)
        Moon_Force_Solar = (Moon_nDirection_Solar[0] * Moon_Gravity_Solar, Moon_nDirection_Solar[1] * Moon_Gravity_Solar)

        # Calculate the perpendicular direction to the gravitational force
        Moon_Solar_perpendicular_direction = (-Moon_nDirection_Solar[1], Moon_nDirection_Solar[0])
        Moon_forward_force_Solar = (Moon_Solar_perpendicular_direction[0] * Moon_forward_magnitude, Moon_Solar_perpendicular_direction[1] * Moon_forward_magnitude)

        # Update Earth's position with gravitational and forward forces
        Moon_x += Moon_Force_Solar[0] + Moon_forward_force_Solar[0]
        Moon_y += Moon_Force_Solar[1] + Moon_forward_force_Solar[1]

    # ORBIT AROUND THE SUN

 #MOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOON    

 #MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARS

    # Calculate distance between Earth and Moon
    distance_xMars = Solar_x - Mars_x
    distance_yMars = Solar_y - Mars_y
    Mars_magnitude = math.hypot(distance_xMars, distance_yMars)

    if Mars_magnitude != 0:
        # Normalized direction of the gravitational force
        Mars_nDirection = (distance_xMars / Mars_magnitude, distance_yMars / Mars_magnitude)
        Mars_Gravity = Solar_mass / (Mars_magnitude * Mars_magnitude)
        Mars_Force = (Mars_nDirection[0] * Mars_Gravity, Mars_nDirection[1] * Mars_Gravity)

        # Calculate the perpendicular direction to the gravitational force
        Mars_perpendicular_direction = (-Mars_nDirection[1], Mars_nDirection[0])
        Mars_forward_force = (Mars_perpendicular_direction[0] * Mars_forward_magnitude, Mars_perpendicular_direction[1] * Mars_forward_magnitude)

        # Update Earth's position with gravitational and forward forces
        Mars_x += Mars_Force[0] + Mars_forward_force[0]
        Mars_y += Mars_Force[1] + Mars_forward_force[1]

 #MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARS


    # Calculate distance between Earth and Sun
    distance_x = Solar_x - Earth_x
    distance_y = Solar_y - Earth_y
    magnitude = math.hypot(distance_x, distance_y)

    if magnitude != 0:
        # Normalized direction of the gravitational force
        nDirection = (distance_x / magnitude, distance_y / magnitude)
        Gravity = Solar_mass / (magnitude * magnitude)
        Force = (nDirection[0] * Gravity, nDirection[1] * Gravity)

        # Calculate the perpendicular direction to the gravitational force
        perpendicular_direction = (-nDirection[1], nDirection[0])
        forward_force = (perpendicular_direction[0] * forward_force_magnitude, perpendicular_direction[1] * forward_force_magnitude)

        # Update Earth's position with gravitational and forward forces
        Earth_x += Force[0] + forward_force[0]
        Earth_y += Force[1] + forward_force[1]

    # Redraw the screen
    surface.fill(black)

    # Update orbit path for Earth
    current_position = (Earth_x + 12.5, Earth_y + 11)
    if len(orbit_path) > 0:
        pygame.draw.line(surface, white, orbit_path[-1], current_position, 1)
    orbit_path.append(current_position)
    if len(orbit_path) > max_path_length:
        orbit_path.pop(0)

    # Update orbit paths for Moon
    current_position_solar = (Moon_x + 7.5, Moon_y + 7.5)

    if len(earth_orbit_path) > 0:
        pygame.draw.line(surface, gray, earth_orbit_path[-1], current_position, 1)
    earth_orbit_path.append(current_position)
    if len(earth_orbit_path) > max_path_length:
        earth_orbit_path.pop(0)

    if len(solar_orbit_path) > 0:
        pygame.draw.line(surface, white, solar_orbit_path[-1], current_position_solar, 1)
    solar_orbit_path.append(current_position_solar)
    if len(solar_orbit_path) > max_path_length:
        solar_orbit_path.pop(0)

    # Draw orbit paths
    draw_orbit_path(surface, earth_orbit_path, gray)   # Moon's orbit around the Earth
    draw_orbit_path(surface, solar_orbit_path, white)  # Moon's orbit around the Sun

    # Update orbit paths for Mars
    current_position_Mars = (Mars_x + 12, Mars_y + 10.5)

    if len(mars_orbit_path) > 0:
        pygame.draw.line(surface, white, mars_orbit_path[-1], current_position_Mars, 1)
    mars_orbit_path.append(current_position_Mars)
    if len(mars_orbit_path) > max_path_length:
        mars_orbit_path.pop(0)

    # Draw orbit paths
    draw_orbit_path(surface, mars_orbit_path, white) 

    Earth = pygame.draw.rect(surface, black, [Earth_x, Earth_y, 25, 22])
    Moon = pygame.draw.rect(surface, gray, [Moon_x, Moon_y, 15, 15])
    Mars = pygame.draw.rect(surface, red, [Mars_x, Mars_y, 24, 21])
    Sun = pygame.draw.rect(surface, yellow, [Solar_x, Solar_y, 50, 50])

    #for Planet in Planets:
    #    planet_x = calculate_gravity(Planet.x, None, None, None, None)
    #    planet_y = calculate_gravity(None, Planet.y, None, None, None)
    #    planet_mass = calculate_gravity(None, None, Planet.mass, None, None)

    #sputnik_x = calculate_gravity(0, 0, 0, Sputnik_x, 0)
    #sputnik_y = calculate_gravity(0, 0, 0, 0, Sputnik_y)

    #Sputnik_Gravitationa_fields_x = calculate_gravity(planet_x, planet_y, planet_mass, sputnik_x, sputnik_y)[0]
    #Sputnik_Gravitationa_fields_y = calculate_gravity(planet_x, planet_y, planet_mass, sputnik_x, sputnik_y)[1]

    if Sputnik:
        total_gravity_x = 0
        total_gravity_y = 0
        
        Sputnik_x += Sputnik_Resultant_Force_x 
        Sputnik_y += Sputnik_Resultant_Force_y
        
        for planet in Planets:
            # Use the planet's x, y, and mass attributes
            if planet.name == "Earth":
                planet_x = Earth_x
                planet_y = Earth_y
                planet_mass = planet.mass 
            elif planet.name == "Moon":
                planet_x = Moon_x
                planet_y = Moon_y
                planet_mass = planet.mass 
            elif planet.name == "Mars":
                planet_x = Mars_x
                planet_y = Mars_y
                planet_mass = planet.mass 
            elif planet.name == "Sun":
                planet_x = Solar_x
                planet_y = Solar_y
                planet_mass = planet.mass 
            
            # Calculate gravitational force from each planet
            force_x, force_y = calculate_gravity(planet_x, planet_y, planet_mass, Sputnik_x, Sputnik_y)
            total_gravity_x += force_x
            total_gravity_y += force_y

        Sputnik_x += total_gravity_x
        Sputnik_y += total_gravity_y


    # Draw orbit path
    draw_orbit_path(surface, orbit_path, white)

    # Draw gravitational force vector
    pygame.draw.line(surface, red, (Earth_x + 12.5, Earth_y + 11), (Earth_x + 12.5 + Force[0] * 100000, Earth_y + 11 + Force[1] * 100000), 2)

    # Draw forward force vector
    pygame.draw.line(surface, green, (Earth_x + 12.5, Earth_y + 11), (Earth_x + 12.5 + forward_force[0] * 100, Earth_y + 11 + forward_force[1] * 100), 2)

    # Draw gravitational force vectors
    pygame.draw.line(surface, red, (Moon_x + 7.5, Moon_y + 7.5), (Moon_x + 7.5 + Moon_Force[0] * 10000, Moon_y + 7.5 + Moon_Force[1] * 10000), 2)  # Earth-Moon
    pygame.draw.line(surface, red, (Moon_x + 7.5, Moon_y + 7.5), (Moon_x + 7.5 + Moon_Force_Solar[0] * 10000, Moon_y + 7.5 + Moon_Force_Solar[1] * 10000), 2)  # Sun-Moon

    # Draw forward force vectors
    pygame.draw.line(surface, green, (Moon_x + 7.5, Moon_y + 7.5), (Moon_x + 7.5 + Moon_forward_force[0] * 100, Moon_y + 7.5 + Moon_forward_force[1] * 100), 2)  # Moon's forward force (around Earth)
    pygame.draw.line(surface, green, (Moon_x + 7.5, Moon_y + 7.5), (Moon_x + 7.5 + Moon_forward_force_Solar[0] * 100, Moon_y + 7.5 + Moon_forward_force_Solar[1] * 100), 2)  # Moon's forward force (around Sun)

    # Draw Resultant orbit vector
    #pygame.draw.line(surface, light_blue, ())
    
    # Combined force vector (sum of gravitational force and forward force)
    combined_force = (Force[0] + forward_force[0], Force[1] + forward_force[1]) #ha combinato le due forze, quella Gravitazionale "Force[0,1]" e quella che fa muovere il pianeta "forward_force[0,1]"

    # Calculate the magnitude of the combined vector
    combined_magnitude = math.hypot(combined_force[0], combined_force[1])

    # Normalize the combined vector (unit vector)
    combined_force_normalized = (combined_force[0] / combined_magnitude, combined_force[1] / combined_magnitude)

    # Draw the normalized combined force vector
    pygame.draw.line(surface, light_blue, (Earth_x + 12.5, Earth_y + 11), (Earth_x + 12.5 + combined_force_normalized[0] * 50, Earth_y + 11 + combined_force_normalized[1] * 50), 2)

    # Combined force vector (sum of gravitational and forward forces) for the Moon
    combined_force_moon = (Moon_Force[0] + Moon_forward_force[0], Moon_Force[1] + Moon_forward_force[1])

    # Calculate the magnitude of the combined vector
    combined_magnitude_moon = math.hypot(combined_force_moon[0], combined_force_moon[1])

    # Normalize the combined vector (unit vector)
    combined_force_moon_normalized = (combined_force_moon[0] / combined_magnitude_moon, combined_force_moon[1] / combined_magnitude_moon)

    # Draw the normalized combined force vector for the Moon
    pygame.draw.line(surface, light_blue, (Moon_x + 7.5, Moon_y + 7.5), (Moon_x + 7.5 + combined_force_moon_normalized[0] * 50, Moon_y + 7.5 + combined_force_moon_normalized[1] * 50), 2)

    image_x = Earth_x + (25 - 31) / 2
    image_y = Earth_y + (22 - 31) / 2

    image_x1 = Solar_x + (50 - 200) / 2
    image_y1 = Solar_y + (50 - 200) / 2

    image_x2 = Moon_x + (15 - 20) / 2
    image_y2 = Moon_y + (15 - 20) / 2

    image_x3 = Mars_x + (24 - 48) / 2
    image_y3 = Mars_y + (21 - 48) / 2

    image_x4 = Sputnik_x + (1 - 30) / 2
    image_y4 = Sputnik_y + (1 - 40) / 2

     # Rotate the rectangle
    rotated_image = pygame.transform.rotate(image_surface, angle)
    angle += 1

    rotated_rect = rotated_image.get_rect(center=(Earth_x + 12.5, Earth_y + 11))
    surface.blit(rotated_image, rotated_rect.topleft)

    # Rotate the rectangle
    rotated_image1 = pygame.transform.rotate(image_surface2, angle1)
    angle1 += 0.5

    rotated_rect1 = rotated_image1.get_rect(center=(Moon_x + 7.5, Moon_y + 7.5))
    surface.blit(rotated_image1, rotated_rect1.topleft)

    # Rotate the rectangle
    rotated_image2 = pygame.transform.rotate(image_surface1, angle2)
    angle2 += 0.1

    rotated_rect2 = rotated_image2.get_rect(center=(Solar_x + 25, Solar_y + 25))
    surface.blit(rotated_image2, rotated_rect2.topleft)

    #surface.blit(image_surface, (image_x, image_y))
    #surface.blit(image_surface1, (image_x1, image_y1))
    #surface.blit(image_surface2, (image_x2, image_y2))

    if Mars_Touched == False:
        Mars = surface.blit(image_surface3, (image_x3, image_y3))
    else:
        Mars = surface.blit(image_surfaceSoviet_mars, (image_x3, image_y3))

    if Sputnik:
        Soviet_Sputnik = pygame.draw.rect(surface, black, [Sputnik_x, Sputnik_y, 1, 1])
        surface.blit(image_surface4, (image_x4, image_y4))

        collide = Soviet_Sputnik.colliderect(Mars)

        if collide:
            Mars_Touched = True

    pygame.display.update()
    clock.tick(60)

# Quit Pygame and close the window
pygame.quit()
sys.exit()
