import argparse
import numpy as np
import sys
sys.path = ["."] + sys.path

from common.body_models import construct_layers
from common.object_tensors import ObjectTensors

from utils.inference import run_inference
from utils.loaders import get_mano_input, get_obj_input
from utils.visualize import visualize


def construct_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mano_p", type=str, default=None, help="Path to raw .mano.npy sequence to process")
    parser.add_argument("-f", "--frame", type=int, default=0, help="Frame number to visualize")
    args = parser.parse_args()
    return args


def main():
    args = construct_args()

    if args.mano_p is not None:
        hand_path = args.mano_p
    else:
        hand_path = "./data/arctic_data/data/raw_seqs/s01/capsulemachine_use_01.mano.npy"
    # corresponding object for the specified scene
    object_path = hand_path.replace("mano", "object")

    hand_data = np.load(hand_path, allow_pickle=True).item()
    left, right = hand_data["left"], hand_data["right"]

    frame = args.frame
    num_frames = len(left["pose"])
    if abs(frame) >= num_frames:
        print(f"Invalid frame number, input a number between 0 and {num_frames-1}")
        exit(1)

    object_data = np.load(object_path)

    # get inputs for hand and object models
    inp_lh = get_mano_input(left, frame)
    inp_rh = get_mano_input(right, frame)
    inp_obj = get_obj_input(object_data, frame, hand_path)

    # construct MANO and object layers
    layers = construct_layers("cpu")
    object_tensor = ObjectTensors()
    layers["object"] = object_tensor

    # predict vertices and meshes
    out_lh, out_rh, out_obj = run_inference(layers, inp_lh, inp_rh, inp_obj)

    # visualize scene
    scene = visualize(layers, out_lh, out_rh, out_obj)
    scene.show()


if __name__ == "__main__":
    main()