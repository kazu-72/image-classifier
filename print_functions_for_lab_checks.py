def check_command_line_arguments(in_arg):
    print("[check] Command line arguments:", in_arg)


def check_creating_pet_image_labels(results):
    print("[check] Created pet image labels. Number of items:", len(results))


def check_classifying_images(results):
    print("[check] Classified images. Number of items:", len(results))


def check_classifying_labels_as_dogs(results):
    print("[check] Adjusted results for 'is-a-dog'.")


def check_calculating_results(results, results_stats):
    print("[check] Calculated results stats. Stats keys:", list(results_stats.keys()))
