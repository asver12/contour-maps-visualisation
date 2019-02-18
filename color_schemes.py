import numpy as np
from matplotlib import pyplot as plt

import color_converter


def create_monochromatic_colorscheme(startcolor, levels):
    """
    Generates a monochromatic colorscheme from a startcolor. The alphavalue of the startcolor is 255

    :param startcolor: rgba with alpha 255
    :param levels: Array with levels at which the color change
    :return: colorarray with len(levels) + 1 entrys
    """
    norm_levels = np.linspace(0, 1, len(levels) + 1)
    return [color_converter.rgb01_to_rgb255([startcolor[0], startcolor[1], startcolor[2], startcolor[3] - i]) for i in
            norm_levels]


def matplotlib_colorschemes(colorscheme, levels):
    """
    Generates a colorscheme from matplotlib

    :param colorscheme: Colorscheme as String
    :param levels: Array with levels at which the color change
    :return: colorarray with len(levels) + 1 entrys
    """

    def reverse_alpha(color):
        return color[0], color[1], color[2], color[3] - 255

    return [reverse_alpha(color_converter.rgb01_to_rgb255(i)) for i in
            plt.cm.get_cmap(colorscheme)(np.linspace(0, 1, len(levels) + 1))]
