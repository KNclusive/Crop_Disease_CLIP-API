1. Unique_classes is a pickle file which is a list of text labels the CLIP model was fine-tuned on.
2. image_inference.npy is the pre-compile numpy array of Inference_Set images which is used to create the similarity index. (This project employes nmlib as the index more here https://github.com/nmslib/nmslib)
3. The image_paths are image_names which the model returns after finding similarity. (For our endpoint, we choose not to return the image directly but name of the image.)

Future scope would be returning the image directly
