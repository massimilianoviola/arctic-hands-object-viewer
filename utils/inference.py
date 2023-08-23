import torch


def run_inference(layers, inp_lh, inp_rh, inp_obj):
    """Obtain vertices and meshes using the MANO and object models."""
    with torch.no_grad():
        # use MANO model for left hand
        out_lh = layers["left"](
            global_orient=inp_lh["global_orient"],
            hand_pose=inp_lh["pose"],
            betas=inp_lh["betas"],
            transl=inp_lh["transl"],
        )
        # use MANO model for right hand
        out_rh = layers["right"](
            global_orient=inp_rh["global_orient"],
            hand_pose=inp_rh["pose"],
            betas=inp_rh["betas"],
            transl=inp_rh["transl"],
        )
        # use object model to articulate the parts
        obj_out = layers["object"](
            angles=inp_obj["angles"],
            global_orient=inp_obj["global_orient"],
            transl=inp_obj["transl"] / 1000,
            query_names=inp_obj["query_names"],
        )
    return out_lh, out_rh, obj_out