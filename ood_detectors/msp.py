import torch
from typing import Dict
import torch.nn.functional as F

from ood_detectors.interface import OODDetector

class MSPOODDetector(OODDetector):

    def setup(self, train_model_outputs, hyperparam: Dict = None):
        pass

    def infer(self, model_outputs):
        
        logits = model_outputs['logits']
        return F.softmax(logits, dim=1).max(dim=1)[0]