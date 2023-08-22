from predefined import EnhancementType
from factory import EnhancementAlgorithmFactory
from component import ImageEnhancer
from utils import check_image, get_user_choice, load_image, show_image_comparison
#import external packages
from PIL import Image

#initailise create factory
algorithm_factory = EnhancementAlgorithmFactory()

save_path = "enhanced_image.png"

def main():
    #loop
    while True:
        file_path = input("Please enter the path of the image file: ")
        is_image = check_image(file_path)
        if is_image:
            print(f"Selected image : {file_path}")
            user_choice = get_user_choice(EnhancementType)
            enhancer = ImageEnhancer(algorithm_factory.create_enhancement_algorithm(user_choice))
            original_image = load_image(file_path)
            enhanced_image = enhancer.enhance(original_image)
            
            #visual comparison of original versus enhanced image
            show_image_comparison(original_image,enhanced_image)
            
            #save image to file
            enhanced_image.save(save_path)
        else:
            print("Selected file is not a valid image format. Please try again.")

if __name__ == "__main__":
    main()