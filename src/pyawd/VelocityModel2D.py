# pyawd - VelocityModel2D
# Tribel Pascal - pascal.tribel@ulb.be
"""
Represents the velocity models as a numpy array
"""
import numpy as np
import matplotlib.pyplot as plt
from pyawd import VelocityModel


class VelocityModel2D(VelocityModel):
    """
    Represents the velocity models as a numpy array
    """
    nx: int = 32
    """
    The width of the field, in pixels
    """
    def __init__(self, nx: int = 32):
        """
        Args:
            nx (int): The width of the field, in pixels
        """
        super().__init__(nx=nx)
        self.data = np.ones((nx, nx))

    def get_data(self) -> np.ndarray:
        """
        Returns:
            - self.data: the velocity field
        """
        return self.data

    def plot(self):
        """
        Plots the field
        """
        plt.imshow(self.data)
        plt.show()