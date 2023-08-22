from PIL import ImageOps, ImageStat,ImageEnhance, ImageFilter

# Strategy Pattern: Enhancement Algorithms
class EnhancementStrategy:
    def apply(self, image):
        pass

class BrightnessEnhancement(EnhancementStrategy):
    def apply(self, image):
        target_brightness = 150
        # Apply brightness enhancement logic
        stat = ImageStat.Stat(image)
        current_brightness = stat.mean[0]

        # Calculate the brightness adjustment factor
        brightness_factor = target_brightness / current_brightness

        # Create an ImageEnhance object
        enhancer = ImageEnhance.Brightness(image)

        # Adjust the brightness using the calculated factor
        enhanced_image = enhancer.enhance(brightness_factor)

        return enhanced_image

class ContrastEnhancement(EnhancementStrategy):
    def apply(self, image):
        # Apply contrast enhancement logic
        enhanced_image = ImageOps.autocontrast(image.convert('RGB'))
        return enhanced_image

class DenoiseEnhancement(EnhancementStrategy):
    def apply(self, image):
        # Apply contrast enhancement logic
        #Gaussian Blur:reduce noise by smoothing out high-frequency variations in the image.
        enhanced_image = image.filter(ImageFilter.GaussianBlur(radius=2))
        #median filter : reduce salt-and-pepper noise.
        enhanced_image = image.filter(ImageFilter.MedianFilter(size=3))
        return enhanced_image