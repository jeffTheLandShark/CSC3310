from typing import List, Tuple
from pydantic import BaseModel

import matplotlib.pyplot as plt

import random as rd
import polygenerator as pg
import statistics as st

rd.seed(42)

plot = True

class Vector(BaseModel):
    """
    Represents a vector in 2D space
    """
    point_1: Tuple[float, float]
    point_2: Tuple[float, float]

def get_right_line(distinct_point: Tuple[float, float]) -> Vector:
    """
    Get the infinite line that is to the right of the distinct point
    """
    return Vector(point_1=distinct_point, point_2=(float('inf'), distinct_point[1]))

def draw_vectors(points: List[Tuple[float, float]]) -> List[Vector]:
    """
    Get a list of vectors from a list of points
    """
    vectors = []
    for i in range(len(points)):
        if i == len(points) - 1:
            vectors.append(Vector(point_1=points[i], point_2=points[0]))
        else:
            vectors.append(Vector(point_1=points[i], point_2=points[(i+1)]))

    return vectors

def plot_polygon(vectors: List[Vector], right_line: Vector) -> None:
    """
    Plot the polygon vectors and the right line
    """
    for vector in vectors:
        x_values = [vector.point_1[0], vector.point_2[0]]
        y_values = [vector.point_1[1], vector.point_2[1]]
        plt.plot(x_values, y_values, marker='o')

    plt.scatter(right_line.point_1[0], right_line.point_1[1])
    plt.plot([right_line.point_1[0], min(3, right_line.point_2[0])], [
            right_line.point_1[1], right_line.point_2[1]], linestyle='--')
    # plt.xlim(-1, 2)
    # plt.ylim(-1, 2)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Polygon Vectors')
    plt.grid(True)
    plt.show()