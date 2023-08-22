from predefined import EnhancementType
from enhancement_strategies import *

# Factory Method Pattern: Enhancement Algorithm Factory
class EnhancementAlgorithmFactory:
    def create_enhancement_algorithm(self, algorithm_type):
        if algorithm_type == EnhancementType.brightness:
            return BrightnessEnhancement()
        elif algorithm_type == EnhancementType.contrast:
            return ContrastEnhancement()
        elif algorithm_type == EnhancementType.denoise:
            return DenoiseEnhancement()
        else:
            raise ValueError("Unknown enhancement algorithm")
