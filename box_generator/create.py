import trimesh

from .config import BoxConfig

def create_box(config: BoxConfig):
    # Create the outer box (complete enclosure)
    outer_box = trimesh.creation.box(extents=[config.width, config.length, config.height])
    # Since trimesh boxes are centered at the origin, translate it so that the bottom is at z = 0
    outer_box.apply_translation([config.width / 2,
                                 config.length / 2,
                                 config.height / 2])

    # Create the inner box that will be subtracted from the outer box.
    # Its dimensions are reduced by twice the wall thickness in x and y, and by the floor thickness in z,
    # ensuring the bottom (floor) remains.
    inner_dims = [
        config.width - 2 * config.wall_thickness,
        config.length - 2 * config.wall_thickness,
        config.height - config.floor_thickness
    ]
    inner_box = trimesh.creation.box(extents=inner_dims)
    # Translate the inner box so that it sits inside the outer box:
    inner_box.apply_translation([config.wall_thickness + inner_dims[0] / 2,
                                 config.wall_thickness + inner_dims[1] / 2,
                                 config.floor_thickness + inner_dims[2] / 2])

    # Use the difference boolean operation to subtract the inner box from the outer box
    box_with_walls = outer_box.difference(inner_box)

    return box_with_walls