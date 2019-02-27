import numpy as np

from src import helper


def blend_color(blending_operator, color_1, color_2, *args, **kwargs):
    """
    blends rgb color with blendingoperator and returns rgb255 data

    :param blending_operator: blending operator which is used to calculate new color, color_1, color_2, alpha
    :param color_1: first color
    :param color_2: second color
    :param alpha: alpha value
    :return: new color
    """
    return blending_operator(color_1, color_2, *args, **kwargs)


def map_colors(x, colormap, levels):
    """

    :param x: 2D-Array with values to map
    :param colormap: colors for each level
    :param levels: levels at which colors are seperated
    :return: 2D-Array with rgba color-codes
    """
    if len(colormap) != len(levels) + 1:
        raise Exception("{} !={} + 1".format(len(colormap), len(levels)))
    x_new = np.zeros([len(x), len(x[0]), 3])
    alpha_new = np.zeros([len(x), len(x[0]), 1])
    for i in range(len(x)):
        for j in range(len(x[0])):
            x_new[i][j] = colormap[helper.find_index(x[i][j], levels)][:3]
            alpha_new[i][j] = colormap[helper.find_index(x[i][j], levels)][3]
    return x_new, alpha_new
