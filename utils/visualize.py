from common.mesh import Mesh


colors = {
    "pink": [1.00, 0.75, 0.80],
    "skin": [0.96, 0.75, 0.69],
    "purple": [0.63, 0.13, 0.94],
    "red": [1.0, 0.0, 0.0],
    "green": [.0, 1., .0],
    "yellow": [1., 1., 0],
    "brown": [1.00, 0.25, 0.25],
    "blue": [.0, .0, 1.],
    "white": [1., 1., 1.],
    "orange": [1.00, 0.65, 0.00],
    "grey": [0.75, 0.75, 0.75],
    "black": [0., 0., 0.],
    "light-blue": [0.588, 0.5647, 0.9725],
}


def visualize(layers, out_lh, out_rh, out_obj, hand_color="skin", obj_color="light-blue"):
    """Render both hands and the object in a single scene."""
    # left hand
    mesh_lh = Mesh(
        v=out_lh.vertices.squeeze(),
        f=layers["left"].faces,
        fc=colors[hand_color],
    )
    # right hand
    mesh_rh = Mesh(
        v=out_rh.vertices.squeeze(),
        f=layers["right"].faces,
        fc=colors[hand_color],
    )
    # object
    mesh_obj = Mesh(
        v=out_obj["v"].squeeze(),
        f=out_obj["f"].squeeze(),
        fc=colors[obj_color],
    )
    # concatenate in a single scene
    scene = Mesh.cat([mesh_obj, mesh_lh, mesh_rh])
    return scene