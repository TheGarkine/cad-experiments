from box_generator.create import create_box
from box_generator.config import BoxConfig

import yaml
with open ("config.yml", "r") as file:
    config = yaml.safe_load(file)

box_config = BoxConfig.load(config)
box = create_box(box_config)
box.export("box_with_walls.stl")
