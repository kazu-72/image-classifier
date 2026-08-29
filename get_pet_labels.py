from os import listdir


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet image labels.

    Parameters:
        image_dir - path to folder containing pet images

    Returns:
        results_dic - dictionary with filename as key and
                      pet label as value in a list
    """

    results_dic = dict()

    # Get filenames
    filename_list = listdir(image_dir)

    # Process each filename
    for filename in filename_list:

        # Only process JPG images
        if filename.lower().endswith(".jpg"):

            # Convert filename to lowercase
            low_pet_image = filename.lower()

            # Split filename using underscore
            word_list_pet_image = low_pet_image.split("_")

            # Create pet label
            pet_name = ""

            for word in word_list_pet_image:

                # Only keep alphabetic words
                if word.isalpha():
                    pet_name += word + " "

            # Remove leading/trailing whitespace
            pet_name = pet_name.strip()

            # Add filename and label to dictionary
            if filename not in results_dic:
                results_dic[filename] = [pet_name]

            else:
                print("** Warning: Key=", filename,
                      "already exists in results_dic with value=",
                      results_dic[filename])

    return results_dic