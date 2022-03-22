__all__ = ['load_pickle', 'PickleImage', 'PickleMaskBlock', 'show_targ_pred_masks']

from fastai.data.all import *
import torch
import pickle

def load_pickle(fn):
    with open(fn, 'rb') as handle: return pickle.load(handle).float()


class PickleImage(torch.Tensor, metaclass=BypassNewMeta):
    _bypass_type=torch.Tensor

    @classmethod
    def create(cls, fn:(Path,str, torch.Tensor), **kwargs)->None:
        if isinstance(fn, torch.Tensor): return cls(fn)
        if isinstance(fn, str): return cls(load_pickle(fn))

def PickleMaskBlock(): return TransformBlock(type_tfms=PickleImage.create) 

def show_targ_pred_masks(targ, pred, slice_nr, figsize=(10,10)): 
    f = plt.figure(figsize=figsize)
    f.add_subplot(1,2, 1)
    plt.axis('off')
    plt.title("Target")
    plt.imshow(targ[0,slice_nr,:])

    f.add_subplot(1,2, 2)
    plt.title("Prediction")
    plt.axis('off')
    plt.imshow(pred[0,slice_nr,:])