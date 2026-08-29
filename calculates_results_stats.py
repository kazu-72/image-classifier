#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER: Mohd Toushif Akhtar
# DATE CREATED: August 29, 2026
# REVISED DATE:
# PURPOSE: Calculates statistics from the results dictionary, including
#          counts and percentages for dog classification and breed accuracy.


def calculates_results_stats(results_dic):
    """
    Calculates statistics from the results dictionary.

    Parameters:
      results_dic - Dictionary with filename as key and a list containing:
                    index 0 = pet image label
                    index 1 = classifier label
                    index 2 = 1/0 label match
                    index 3 = 1/0 pet image is a dog
                    index 4 = 1/0 classifier says image is a dog

    Returns:
      results_stats_dic - Dictionary containing calculated statistics.
    """

    # Creates empty Results Statistics Dictionary
    results_stats_dic = dict()

    # Initialize counts
    n_images = len(results_dic)
    n_dogs_img = 0
    n_notdogs_img = 0
    n_correct_dogs = 0
    n_correct_notdogs = 0
    n_correct_breed = 0
    n_match = 0

    # Calculate counts by iterating through results dictionary
    for key in results_dic:

        # Count number of dog images
        if results_dic[key][3] == 1:
            n_dogs_img += 1

            # Correctly classified as a dog
            if results_dic[key][4] == 1:
                n_correct_dogs += 1

            # Correctly classified dog breed
            if results_dic[key][2] == 1:
                n_correct_breed += 1

        # Count number of non-dog images
        else:
            n_notdogs_img += 1

            # Correctly classified as not a dog
            if results_dic[key][4] == 0:
                n_correct_notdogs += 1

        # Count all label matches across all images exactly once.
        if results_dic[key][2] == 1:
            n_match += 1

    # Store counts in Results Statistics Dictionary
    results_stats_dic["n_images"] = n_images
    results_stats_dic["n_dogs_img"] = n_dogs_img
    results_stats_dic["n_notdogs_img"] = n_notdogs_img
    results_stats_dic["n_correct_dogs"] = n_correct_dogs
    results_stats_dic["n_correct_notdogs"] = n_correct_notdogs
    results_stats_dic["n_correct_breed"] = n_correct_breed
    results_stats_dic["n_match"] = n_match

    # Calculate percentage of correctly classified dog images
    if n_dogs_img > 0:
        results_stats_dic["pct_correct_dogs"] = (
            n_correct_dogs / n_dogs_img
        ) * 100.0

        # Calculate percentage of correctly classified dog breeds
        results_stats_dic["pct_correct_breed"] = (
            n_correct_breed / n_dogs_img
        ) * 100.0
    else:
        results_stats_dic["pct_correct_dogs"] = 0.0
        results_stats_dic["pct_correct_breed"] = 0.0

    # Calculate percentage of correctly classified non-dog images
    if n_notdogs_img > 0:
        results_stats_dic["pct_correct_notdogs"] = (
            n_correct_notdogs / n_notdogs_img
        ) * 100.0
    else:
        results_stats_dic["pct_correct_notdogs"] = 0.0

    if n_images > 0:
        results_stats_dic["pct_match"] = (n_match / n_images) * 100.0
    else:
        results_stats_dic["pct_match"] = 0.0

    return results_stats_dic
