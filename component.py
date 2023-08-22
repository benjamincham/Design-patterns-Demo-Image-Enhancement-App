# Dependency Injection with Factory and Strategy
class ImageEnhancer:
    def __init__(self, enhancement_algorithm):
        self.enhancement_algorithm = enhancement_algorithm

    def enhance(self, image):
        enhanced_image = self.enhancement_algorithm.apply(image)
        return enhanced_image
