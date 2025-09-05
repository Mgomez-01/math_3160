# -*- coding: utf-8 -*-
"""
A demonstration script for visualizing various complex function transformations.
This script defines a general-purpose plotting function and then uses it
to show how different curves in the complex z-plane are mapped to the w-plane.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- The Generalized Plotting Function ---

def plot_complex_transformation(z_values, g, num_points=11, z_title="Original Path (z-plane)", w_title="Transformed Path (w-plane)"):
    """
    Transforms a set of complex numbers and plots the original and transformed curves.

    Args:
        z_values (np.ndarray): An array of complex numbers for the curve in the z-plane.
        g (callable): The transformation function g(z) that takes a complex number or array.
        num_points (int): The number of sample points to highlight on the curves.
        z_title (str): The title for the z-plane plot.
        w_title (str): The title for the w-plane plot.
    """
    print(f"Plotting transformation for: {z_title}")
    
    # 1. Apply the transformation to get the points in the w-plane
    w_values = g(z_values)

    # 2. Select evenly spaced sample points to highlight the mapping
    indices = np.linspace(0, len(z_values) - 1, num_points, dtype=int)
    z_points = z_values[indices]
    w_points = w_values[indices]

    # 3. Create side-by-side plots for the z-plane and w-plane
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

    # --- Plotting on the z-plane (left) ---
    ax1.plot(z_values.real, z_values.imag, 'r-', linewidth=2, label='Original Path')
    # Use a colormap to show correspondence between points
    ax1.scatter(z_points.real, z_points.imag, c=np.arange(num_points), 
                cmap='viridis', s=60, zorder=5, ec='black')
    ax1.set_xlabel('Re(z)')
    ax1.set_ylabel('Im(z)')
    ax1.set_title(z_title)
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.set_aspect('equal')
    ax1.axhline(0, color='black', lw=0.5)
    ax1.axvline(0, color='black', lw=0.5)
    
    # --- Plotting on the w-plane (right) ---
    ax2.plot(w_values.real, w_values.imag, 'b-', linewidth=2, label='Transformed Path')
    ax2.scatter(w_points.real, w_points.imag, c=np.arange(num_points), 
                cmap='viridis', s=60, zorder=5, ec='black')
    ax2.set_xlabel('Re(w)')
    ax2.set_ylabel('Im(w)')
    ax2.set_title(w_title)
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.set_aspect('equal')
    ax2.axhline(0, color='black', lw=0.5)
    ax2.axvline(0, color='black', lw=0.5)

    plt.tight_layout()
    plt.show()

# --- Main Execution Block ---

if __name__ == "__main__":
    
    # --- Define Transformation Functions ---
    def g_squared(z):
        """Squaring function: w = z^2"""
        return z**2

    def g_qubed(z):
        """Cubing function: w = z^2"""
        return z**3

    def g_inversion(z):
        """Inversion function: w = 1/z"""
        # Add a small epsilon to avoid division by zero if z is ever 0
        return 1 / (z + 1e-8)

    def g_exp(z):
        """Exponential function: w = e^z"""
        return np.exp(z)
        
    # # --- EXAMPLE 1: Horizontal Line under w = z^2 (Your original case) ---
    # # A horizontal line z = x + ic maps to a parabola.
    # x_vals = np.linspace(-2.5, 2.5, 200)
    # z_horizontal_line = x_vals + 1j * 1.5 # Line at y=1.5
    # plot_complex_transformation(
    #     z_values=z_horizontal_line,
    #     g=g_squared,
    #     z_title='Horizontal Line: $z = x + 1.5i$',
    #     w_title='Transformed Parabola: $w = z^2$'
    # )

    # # --- EXAMPLE 2: Vertical Line under w = z^2 ---
    # # A vertical line z = c + iy also maps to a parabola.
    # y_vals = np.linspace(-2.5, 2.5, 200)
    # z_vertical_line = 1 + 1j * y_vals # Line at x=1
    # plot_complex_transformation(
    #     z_values=z_vertical_line,
    #     g=g_squared,
    #     z_title='Vertical Line: $z = 1 + iy$',
    #     w_title='Transformed Parabola: $w = z^2$'
    # )

    # --- EXAMPLE mine: Vertical Line under w = z^3 ---
    # A vertical line z = c + iy maps to z^3.
    y_vals = np.linspace(-3.5, 3.5, 200)
    z_vertical_line = 1 + 1j * y_vals # Line at x=1
    plot_complex_transformation(
        z_values=z_vertical_line,
        g=g_qubed,
        z_title='Vertical Line: $z = 1 + iy$',
        w_title='Transformed: $w = z^3$'
    )

    # --- EXAMPLE 3: Circle under w = 1/z ---
    # A circle not passing through the origin maps to another circle.
    theta = np.linspace(0, 2 * np.pi, 200)
    z_circle = 2.5 + 1 * np.exp(1j * theta)  # Circle centered at z=2.5, radius 1
    plot_complex_transformation(
        z_values=z_circle,
        g=g_inversion,
        z_title='Original Circle: $|z - 2.5| = 1$',
        w_title='Transformed Circle: $w = 1/z$'
    )

    # # --- EXAMPLE 4: Vertical Line under w = e^z ---
    # # A vertical line segment z = c + iy maps to a circular arc.
    # # The real part 'c' determines the radius of the circle (e^c).
    # # The imaginary part 'y' determines the angle.
    # y_vals_exp = np.linspace(-np.pi, np.pi, 200)
    # z_exp_line = 0.5 + 1j * y_vals_exp # Line at x=0.5 from y=-pi to y=pi
    # plot_complex_transformation(
    #     z_values=z_exp_line,
    #     g=g_exp,
    #     num_points=15,
    #     z_title=r'Vertical Line: $z = 0.5 + iy$ for $y \in [-\pi, \pi]$',
    #     w_title=r'Transformed Circle: $w = e^z$'
    # )

    print("\nAll demonstrations complete! ✨")
