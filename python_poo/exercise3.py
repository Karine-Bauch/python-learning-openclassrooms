# toolbox
class Toolbox:
  def __init__(self):
    # initialise les outils
    self.tools = []
  
  def add_tools(self, tool):
    # ajoutez un outil
    self.tools.append(tool)

  def remove_tools(self, tool):
    # enlève un outil
    index = self.tools.index(tool)
    del self.tools[index]


# screwdriver
class Screwdriver:
  def __init__(self, size=3):
    # initialise la taille
    self.size = size
  
  def tighten(self, screw):
    # serrer une vis
    screw.tighten()

  def loosen(self, screw):
    # desserrer une vis
      screw.loosen()

  def __repr__(self):
    # Représentation de l'objet
    return f"Tournevis de taille {self.size}"
  

# hammer
class Hammer:
  def __init__(self, color="red"):
    # initialise la couleur
    self.color = color
  
  def paint(self, color):
    # paint le marteau
    self.color = color

  def plant_nail(self, nail):
    # enfonce un clou
    nail.nail_in()

  def remove_nail(self, nail):
    # enlève un clou
    nail.remove()

  def __repr__(self):
    # Représentation de l'objet
    return f"Marteau de couleur {self.color}"


# Vis
class Screw:

  MAW_TIGHTNESS = 5

  def __init__(self):
    # initialise le degré de serrage
    self.tightness = 0

  def loosen(self):
    # Desserre la vis
    if self.tightness > 0:
      self.tightness -= 1

  def tighten(self):
    if self.tightness < self.MAW_TIGHTNESS:
      self.tightness += 1

  def __str__(self):
    # Retourne une forme lisible de l'objet
    return "Vis avec un serrage de {}".format(self.tightness)


# Clou
class Nail:
  def __init__(self):
    # Inititalise son statut dans le mur
    self.in_wall = False
  
  def nail_in(self):
    # enfonce le clou
    if not self.in_wall:
      self.in_wall = True
  
  def remove(self):
    # enfonce le clou
    if self.in_wall:
      self.in_wall = False

  def __str__(self):
    # Retroune une forme lisible de l'objet
    wall_state = "dans le mur" if self.in_wall else "hors du mur"
    return f"Clou {wall_state}."


toolbox1 = Toolbox()

screwdriver1 = Screwdriver()

hammer1 = Hammer()

toolbox1.add_tools(screwdriver1)
toolbox1.add_tools(hammer1)

print(toolbox1.tools)

screw1 = Screw()
print(screw1)
screw1.tighten()
print(screw1)

nail1 = Nail()
print(nail1)
nail1.nail_in()
print(nail1)
