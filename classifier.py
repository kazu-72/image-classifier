#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classifier.py

import ast
from PIL import Image

import torch
import torchvision.transforms as transforms
import torchvision.models as models


# Load pretrained CNN models
resnet18 = models.resnet18(
    weights=models.ResNet18_Weights.IMAGENET1K_V1
)

alexnet = models.alexnet(
    weights=models.AlexNet_Weights.IMAGENET1K_V1
)

vgg16 = models.vgg16(
    weights=models.VGG16_Weights.IMAGENET1K_V1
)


# Dictionary containing the three models
models_dict = {
    'resnet': resnet18,
    'alexnet': alexnet,
    'vgg': vgg16
}


# Obtain ImageNet labels used by this project
with open('imagenet1000_clsid_to_human.txt') as imagenet_classes_file:
    imagenet_classes_dict = ast.literal_eval(
        imagenet_classes_file.read()
    )


def classifier(img_path, model_name):
    """
    Classifies an image using a pretrained CNN model.

    Parameters:
        img_path - path to the image
        model_name - CNN architecture:
                     resnet, alexnet, or vgg

    Returns:
        ImageNet classification label
    """

    # Load the image
    img_pil = Image.open(img_path).convert('RGB')

    # Define image preprocessing
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    # Preprocess image
    img_tensor = preprocess(img_pil)

    # Add batch dimension
    img_tensor = img_tensor.unsqueeze(0)

    # Select the requested model
    model = models_dict[model_name]

    # Put model in evaluation mode
    model.eval()

    # Run the image through the pretrained model
    with torch.no_grad():
        output = model(img_tensor)

    # Find the predicted ImageNet class index
    pred_idx = output.argmax(dim=1).item()

    # Return the original project ImageNet label.
    # This preserves labels/aliases expected by the project.
    return imagenet_classes_dict[pred_idx]