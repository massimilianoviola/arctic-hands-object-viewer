import torch


def get_mano_input(hand, frame):
    """Prepare input for MANO hand model."""
    inp = dict()
    inp["betas"] = torch.tensor(hand["shape"])[None, :]
    inp["pose"] = torch.tensor(hand["pose"][frame])[None, :]
    inp["global_orient"] = torch.tensor(hand["rot"][frame])[None, :]
    inp["transl"] = torch.tensor(hand["trans"][frame])[None, :]
    return inp


def get_obj_input(obj, frame, hand_path):
    """Prepare input for the object articulation model."""
    inp = dict()
    inp["angles"] = torch.tensor(obj[frame][:1])[None, :]
    inp["global_orient"] = torch.tensor(obj[frame][1:4])[None, :]
    inp["transl"] = torch.tensor(obj[frame][4:])[None, :]
    inp["query_names"] = [hand_path.split("/")[-1].split("_")[0]]
    return inp