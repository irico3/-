from draw_model import draw_model
from teapot import load_triangles
from vectors import add


def polygon_map(transformation, polygons):
    return [[transformation(vertex) for vertex in triangle] for triangle in polygons]


def translate_by(translation):
    def new_function(v):
        return add(translation, v)

    return new_function


draw_model(polygon_map(translate_by((0, 0, -20)), load_triangles()))
