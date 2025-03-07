class BoxConfig:
    width: float
    length: float
    height: float
    wall_thickness: float
    floor_thickness: float
    lid_thickness: float

    @staticmethod
    def load(d):
        config = BoxConfig()
        config.width = d["width"]
        config.length = d["length"]
        config.height = d["height"]
        config.wall_thickness = d["wall_thickness"]
        config.floor_thickness = d["floor_thickness"]
        config.lid_thickness = d["lid_thickness"]
        return config