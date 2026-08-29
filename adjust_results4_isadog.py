def adjust_results4_isadog(results_dic, dogfile):
    """
    Determines whether the pet image label and classifier label
    represent dogs.

    Adds:
        index 3 = pet image is a dog (1) or not (0)
        index 4 = classifier says dog (1) or not (0)

    Returns:
        None
    """

    # Create dictionary of dog names
    dognames_dic = dict()

    # Read dog names
    with open(dogfile, "r") as infile:

        line = infile.readline()

        while line != "":

            # Remove newline
            dog_name = line.rstrip()

            # Add dog name if not already present
            if dog_name not in dognames_dic:
                dognames_dic[dog_name] = 1

            else:
                print("** Warning: Duplicate dog name:",
                      dog_name)

            line = infile.readline()

    # Process results
    for key in results_dic:

        pet_label = results_dic[key][0]
        classifier_label = results_dic[key][1]

        # Pet image dog?
        if pet_label in dognames_dic:
            pet_is_dog = 1
        else:
            pet_is_dog = 0

        # Classifier dog?
        # Classifier can return multiple comma-separated labels
        classifier_names = [
            name.strip()
            for name in classifier_label.split(",")
        ]

        classifier_is_dog = 0

        for name in classifier_names:
            if name in dognames_dic:
                classifier_is_dog = 1
                break

        # Add dog/not-dog results
        results_dic[key].extend(
            (pet_is_dog, classifier_is_dog)
        )