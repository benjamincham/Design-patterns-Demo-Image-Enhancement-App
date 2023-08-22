from PIL import Image, ImageDraw, ImageFont

def add_text_overlay(image, text):
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()  # You can also load a specific font here

    text_width, text_height = draw.textsize(text, font)
    image_width, image_height = image.size

    x = (image_width - text_width) // 2
    y = image_height - text_height - 10  # Adjust the vertical position

    draw.text((x, y), text, font=font, fill=(255, 255, 255))  # White text color

def show_image_comparison(original_image,enhanced_image):
    # Add text overlay to the first image
    add_text_overlay(original_image, "Original")

    # Add text overlay to the second image
    add_text_overlay(enhanced_image, "Enhanced")

    # Specify the desired gap width (in pixels)
    gap_width = 20

    width1, height1 = original_image.size
    width2, height2 = enhanced_image.size

    new_width = width1 + gap_width + width2
    new_height = max(height1, height2)

    combined_image = Image.new("RGB", (new_width, new_height))
    combined_image.paste(original_image, (0, 0))
    combined_image.paste(enhanced_image, (width1 + gap_width, 0))

    combined_image.show()

def load_image(file_path):
    return Image.open(file_path) 

def check_image(file_path):
    try:
        image = Image.open(file_path)
        image.close()
        return True
    except Exception as e:
        return False
    
def get_user_choice(enum_class):
    while True:
        print("Image Enhancement options:")
        for option in enum_class:
            print(f"{option.value}: {option.name}")

        try:
            user_choice = int(input("Select an option: "))
            if user_choice in [option.value for option in enum_class]:
                return enum_class(user_choice)
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")