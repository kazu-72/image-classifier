"""Classifier wrapper for the pet-image project."""


def classifier(img_path: str, model_name: str = 'vgg') -> str:
    """Return the model-predicted label for an image.

    This function must never derive a prediction from the filename.
    If the required ML dependencies are unavailable or the model cannot run,
    the error is allowed to propagate so the project fails loudly instead of
    producing fake accuracy.
    """
    import torch
    import torchvision
    from PIL import Image
    from torchvision import transforms

    model_name = (model_name or 'vgg').lower()
    model_map = {
        'resnet': ('resnet18', torchvision.models.resnet.ResNet18_Weights),
        'alexnet': ('alexnet', torchvision.models.AlexNet_Weights),
        'vgg': ('vgg16', torchvision.models.VGG16_Weights),
    }

    if model_name not in model_map:
        raise ValueError(f"Unsupported model: {model_name}")

    model_fn_name, weights_enum = model_map[model_name]
    weights = getattr(weights_enum, 'IMAGENET1K_V1', None) or getattr(weights_enum, 'DEFAULT', None)
    model_ctor = getattr(torchvision.models, model_fn_name)

    if weights is not None:
        model = model_ctor(weights=weights)
        preprocess = weights.transforms()
        meta = getattr(weights, 'meta', {}) or {}
        categories = meta.get('categories') if isinstance(meta, dict) else getattr(meta, 'categories', None)
    else:
        model = model_ctor(weights=None)
        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        categories = None

    model.eval()
    img = Image.open(img_path).convert('RGB')
    input_tensor = preprocess(img).unsqueeze(0)

    with torch.no_grad():
        outputs = model(input_tensor)
        _, predicted = torch.max(outputs, 1)
        idx = int(predicted.item())

    if categories and 0 <= idx < len(categories):
        return categories[idx]
    return str(idx)