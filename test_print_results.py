from print_results import print_results

# sample data
results = {
    'img1.jpg': ['maltese', 'maltese', 1, 1, 1],
    'img2.jpg': ['tabby', 'tabby', 1, 0, 0],
    'img3.jpg': ['golden retriever', 'labrador, golden retriever', 0, 1, 1],
    'img4.jpg': ['siamese', 'maltese', 0, 0, 1]
}

results_stats = {
    'n_images': 4,
    'n_dogs_img': 3,
    'n_notdogs_img': 1,
    'n_correct_dogs': 2,
    'n_correct_notdogs': 1,
    'n_correct_breed': 1,
    'pct_correct_dogs': 66.6667,
    'pct_correct_breed': 33.3333,
    'pct_correct_notdogs': 100.0
}

print_results(results, results_stats, 'vgg', True, True)
