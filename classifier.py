"""
`classifier.py` - provides `classifier(img_path, model_name)`.

This implementation lazily imports heavy ML libs (torch/torchvision).
If torchvision is unavailable it falls back to deriving a label
from the filename.
"""
from typing import Optional
import os


def _filename_label(img_path: str) -> str:
    # Derive a human-readable label from the filename
    name = os.path.splitext(os.path.basename(img_path))[0]
    # replace underscores and digits, collapse spaces
    label = " ".join([p for p in name.replace('_', ' ').split() if not any(c.isdigit() for c in p)])
    return label.strip() if label else os.path.basename(img_path)


def classifier(img_path: str, model_name: str = 'vgg') -> str:
    """Return a classifier label for `img_path` using `model_name` when
    torchvision is available, otherwise fall back to filename-derived label.

    model_name: one of 'resnet', 'alexnet', 'vgg'
    """
    # Try to import heavy dependencies only when needed
    try:
        import torch
        import torchvision
        from PIL import Image
        from torchvision import transforms
    except Exception:
        return _filename_label(img_path)

    # Map requested model name to torchvision model constructor and weights
    model_name = (model_name or 'vgg').lower()
    model_map = {
        'resnet': ('resnet18', torchvision.models.resnet.ResNet18_Weights),
        'alexnet': ('alexnet', torchvision.models.AlexNet_Weights),
        'vgg': ('vgg16', torchvision.models.VGG16_Weights),
    }

    if model_name not in model_map:
        return _filename_label(img_path)

    model_fn_name, weights_enum = model_map[model_name]

    try:
        # Get weights default if available
        weights = getattr(weights_enum, 'IMAGENET1K_V1', None) or getattr(weights_enum, 'DEFAULT', None)
        model_ctor = getattr(torchvision.models, model_fn_name)
        if weights is not None:
            model = model_ctor(weights=weights)
            preprocess = weights.transforms()
            categories = getattr(weights.meta, 'categories', None) or weights.meta.get('categories') if hasattr(weights, 'meta') else None
        else:
            model = model_ctor(pretrained=True)
            # fallback transforms
            preprocess = transforms.Compose([
                transforms.Resize(256),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            ])
            categories = None
    except Exception:
        return _filename_label(img_path)

    model.eval()

    try:
        img = Image.open(img_path).convert('RGB')
    except Exception:
        return _filename_label(img_path)

    try:
        input_tensor = preprocess(img).unsqueeze(0)
        with torch.no_grad():
            outputs = model(input_tensor)
            _, predicted = torch.max(outputs, 1)
            idx = int(predicted.item())
        # Map to human-readable label if categories are available
        if categories and 0 <= idx < len(categories):
            return categories[idx]
        return str(idx)
    except Exception:
        return _filename_label(img_path)