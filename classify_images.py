#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#
# PROGRAMMER: Mohd Toushif Akhtar
# DATE CREATED: August 29, 2026
# REVISED DATE:
# PURPOSE: Create a function classify_images that uses the classifier function
#          to create the classifier labels and then compares the classifier
#          labels to the pet image labels.

# Imports classifier function for using CNN to classify images
from classifier import classifier


def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to
    the classifier labels, and adds the classifier label and the comparison of
    the labels to the results dictionary using the extend function.
    """

    # Process all files in the results dictionary
    for key in results_dic:

        # Create full image path
        image_path = images_dir + "/" + key

        # Classify image using the selected CNN model
        model_label = classifier(image_path, model)

        # Convert classifier label to lowercase and strip whitespace
        model_label = model_label.lower().strip()

        # Get the true pet image label
        truth = results_dic[key][0]

        # Check whether the pet label is contained in the classifier label
        if truth in model_label:
            results_dic[key].extend([model_label, 1])
        else:
            results_dic[key].extend([model_label, 0])