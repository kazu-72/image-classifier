#!/usr/bin/env python3
import argparse
import os
import csv
import sys

from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results


def main():
    parser = argparse.ArgumentParser(description='Batch classify uploaded images')
    parser.add_argument('--dir', required=True, help='Directory with images')
    parser.add_argument('--arch', default='vgg', help='CNN architecture')
    parser.add_argument('--dogfile', default='dognames.txt', help='Dog names file')
    parser.add_argument('--out', default='uploaded_results.csv', help='Output CSV file')
    args = parser.parse_args()

    image_dir = args.dir
    arch = args.arch
    dogfile = args.dogfile
    out_csv = args.out

    # Ensure working directory is script location so relative imports/files work
    # but preserve provided paths
    try:
        results = get_pet_labels(image_dir)
    except Exception as e:
        print(f"Error getting pet labels: {e}")
        sys.exit(1)

    try:
        classify_images(image_dir, results, arch)
    except Exception as e:
        print(f"Error classifying images: {e}")
        sys.exit(1)

    try:
        adjust_results4_isadog(results, dogfile)
    except Exception as e:
        print(f"Warning: adjust_results4_isadog failed: {e}")

    try:
        results_stats = calculates_results_stats(results)
    except Exception as e:
        print(f"Warning: calculates_results_stats failed: {e}")
        results_stats = {}

    # Write per-image CSV
    fieldnames = ['filename', 'pet_label', 'classifier_label', 'is_match', 'is_pet_dog', 'is_classifier_dog']
    try:
        with open(out_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for fname, vals in results.items():
                row = {
                    'filename': fname,
                    'pet_label': vals[0] if len(vals) > 0 else '',
                    'classifier_label': vals[1] if len(vals) > 1 else '',
                    'is_match': vals[2] if len(vals) > 2 else 0,
                    'is_pet_dog': vals[3] if len(vals) > 3 else 0,
                    'is_classifier_dog': vals[4] if len(vals) > 4 else 0,
                }
                writer.writerow(row)
        print(f"Wrote results to {out_csv}")
    except Exception as e:
        print(f"Error writing CSV: {e}")

    # Print summary using existing helper
    try:
        print_results(results, results_stats, arch, True, True)
    except Exception:
        # fallback simple summary
        print('Images:', len(results))


if __name__ == '__main__':
    main()
