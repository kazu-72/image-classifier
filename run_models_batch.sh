
#!/bin/sh
# Run check_images.py using all three CNN model architectures

python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt > resnet_pet-images.txt

python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt > alexnet_pet-images.txt

python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt > vgg_pet-images.txt

