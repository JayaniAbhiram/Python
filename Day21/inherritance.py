class animal:
    def __init__(self):
        eyes = 2
    
    def breathe(self):
        print("animal with breath like exhale and inhalke")

class fish(animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("fish can also breate thhrpugh gills")
        


nemo = fish()
nemo.breathe()



