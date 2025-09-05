import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

def transform_z_squared(z):
    """Transform complex number z by z^2"""
    return z**2

def plot_line_mapping():
    """Plot the mapping of line z = x + i under z^2"""
    # Original line: z = x + i for x from -3 to 3
    x_vals = np.linspace(-3, 3, 100)
    z_line = x_vals + 1j
    
    # Transform the line: w = z^2 = (x + i)^2 = x^2 - 1 + 2xi
    w_line = transform_z_squared(z_line)
    
    # Theoretical parabola for comparison: Re(w) = (Im(w))^2/4 - 1
    v_vals = np.linspace(-6, 6, 100)
    parabola_real = v_vals**2/4 - 1
    parabola_imag = v_vals
    
    # Create side-by-side plots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Original z-plane
    ax1.plot(z_line.real, z_line.imag, 'r-', linewidth=2, label='z = x + i')
    ax1.scatter(z_line.real[::10], z_line.imag[::10], c='red', s=20, alpha=0.7)
    ax1.set_xlim(-4, 4)
    ax1.set_ylim(-1, 3)
    ax1.set_xlabel('Re(z)')
    ax1.set_ylabel('Im(z)')
    ax1.set_title('Original Line in z-plane')
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    ax1.legend()
    
    # Transformed w-plane
    ax2.plot(w_line.real, w_line.imag, 'b-', linewidth=2, label='w = z²')
    ax2.plot(parabola_real, parabola_imag, 'gray', linestyle='--', alpha=0.7, 
             label='Theoretical parabola')
    ax2.scatter(w_line.real[::10], w_line.imag[::10], c='blue', s=15, alpha=0.7)
    ax2.set_xlim(-2, 10)
    ax2.set_ylim(-6, 6)
    ax2.set_xlabel('Re(w)')
    ax2.set_ylabel('Im(w)')
    ax2.set_title('Transformed Line in w-plane')
    ax2.grid(True, alpha=0.3)
    ax2.set_aspect('equal')
    ax2.legend()
    
    # Add equation text
    ax2.text(3, -5, r'Re(w) = $\frac{(Im(w))^2}{4} - 1$', 
             fontsize=12, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
    
    plt.tight_layout()
    plt.show()

def plot_point_mapping_examples():
    """Show specific point mappings"""
    # Key points on the line z = x + i
    x_points = [-2, -1, 0, 1, 2]
    z_points = [x + 1j for x in x_points]
    w_points = [transform_z_squared(z) for z in z_points]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Original line with highlighted points
    x_line = np.linspace(-3, 3, 100)
    z_line = x_line + 1j
    ax1.plot(z_line.real, z_line.imag, 'r-', linewidth=2, alpha=0.5)
    
    for i, (z, x) in enumerate(zip(z_points, x_points)):
        ax1.scatter(z.real, z.imag, s=100, c=f'C{i}', zorder=5)
        ax1.annotate(f'z = {x} + i', (z.real, z.imag), 
                    xytext=(5, 5), textcoords='offset points', fontsize=10)
    
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(0, 2)
    ax1.set_xlabel('Re(z)')
    ax1.set_ylabel('Im(z)')
    ax1.set_title('Points on Line z = x + i')
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    
    # Transformed points with parabola
    w_line = transform_z_squared(z_line)
    ax2.plot(w_line.real, w_line.imag, 'b-', linewidth=2, alpha=0.5)
    
    for i, (w, x) in enumerate(zip(w_points, x_points)):
        ax2.scatter(w.real, w.imag, s=100, c=f'C{i}', zorder=5)
        ax2.annotate(f'w = {w.real:.0f} + {w.imag:.0f}i', (w.real, w.imag), 
                    xytext=(5, 5), textcoords='offset points', fontsize=9)
        
        # Draw arrow from origin to show the transformation
        ax2.annotate('', xy=(w.real, w.imag), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', alpha=0.3, color=f'C{i}'))
    
    ax2.set_xlim(-2, 10)
    ax2.set_ylim(-6, 6)
    ax2.set_xlabel('Re(w)')
    ax2.set_ylabel('Im(w)')
    ax2.set_title('Transformed Points w = z²')
    ax2.grid(True, alpha=0.3)
    ax2.set_aspect('equal')
    
    plt.tight_layout()
    plt.show()

def analyze_transformation():
    """Print mathematical analysis of the transformation"""
    print("=" * 60)
    print("MATHEMATICAL ANALYSIS: Line z = x + i under w = z²")
    print("=" * 60)
    print("\n1. Original line: z = x + i (horizontal line at height 1)")
    print("2. Transformation: w = (x + i)² = x² + 2xi + i²")
    print("3. Simplified: w = x² + 2xi - 1 = (x² - 1) + 2xi")
    print("4. Real part: Re(w) = x² - 1")
    print("5. Imaginary part: Im(w) = 2x")
    print("6. Eliminate parameter x: x = Im(w)/2")
    print("7. Substitute: Re(w) = (Im(w)/2)² - 1 = (Im(w))²/4 - 1")
    print("8. Result: PARABOLA opening rightward with vertex at (-1, 0)")
    print("\n" + "=" * 60)
    print("KEY POINT MAPPINGS:")
    print("=" * 60)
    
    x_vals = [-1, 1, -1, 1, -1]
    y_vals = [-2, -1, 0, 1, 2]
    for x in x_vals:
        for y in y_vals:
            z = x + 1j*y
            w = transform_z_squared(z)
            print(f"z = {x:2d} + i  →  w = {w.real:2.0f} + {w.imag:2.0f}i")
        
    print("\n" + "=" * 60)
    print("GEOMETRIC PROPERTIES:")
    print("=" * 60)
    print("• Distance: |w| = |z|² (distances are squared)")
    print("• Angle: arg(w) = 2·arg(z) (angles are doubled)")
    print("• The line z = x + i has constant |z| = √(x² + 1)")
    print("• After transformation: |w| = x² + 1")
    print("• The parabola is the image of this horizontal line")

def plot_multiple_lines():
    """Show how different horizontal lines map to different parabolas"""
    y_values = [-2, -1, 0, 1, 2]
    colors = ['red', 'orange', 'green', 'blue', 'purple']
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    x_range = np.linspace(-3, 3, 100)
    
    for i, y in enumerate(y_values):
        # Original horizontal lines
        z_line = x_range + 1j * y
        ax1.plot(z_line.real, z_line.imag, color=colors[i], 
                linewidth=2, label=f'z = x + {y}i')
        
        # Transformed curves (parabolas)
        w_line = transform_z_squared(z_line)
        ax2.plot(w_line.real, w_line.imag, color=colors[i], 
                linewidth=2, label=f'y = {y}')
    
    ax1.set_xlim(-4, 4)
    ax1.set_ylim(-3, 3)
    ax1.set_xlabel('Re(z)')
    ax1.set_ylabel('Im(z)')
    ax1.set_title('Original Horizontal Lines')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_aspect('equal')
    
    ax2.set_xlim(-10, 10)
    ax2.set_ylim(-12, 12)
    ax2.set_xlabel('Re(w)')
    ax2.set_ylabel('Im(w)')
    ax2.set_title('Transformed Parabolas w = z²')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    ax2.set_aspect('equal')
    
    plt.tight_layout()
    plt.show()

def interactive_point_demo():
    """Create an interactive demonstration (requires manual point selection)"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Draw the full line and its transformation
    x_line = np.linspace(-3, 3, 100)
    z_line = x_line + 1j
    w_line = transform_z_squared(z_line)
    
    ax1.plot(z_line.real, z_line.imag, 'r-', linewidth=2, alpha=0.3)
    ax2.plot(w_line.real, w_line.imag, 'b-', linewidth=2, alpha=0.3)
    
    # Interactive points
    test_points = [0 + 1j, 1 + 1j, -1 + 1j, 2 + 1j]
    
    for z in test_points:
        w = transform_z_squared(z)
        
        # Original point
        ax1.scatter(z.real, z.imag, s=100, c='red', zorder=5)
        ax1.annotate(f'{z:.1f}', (z.real, z.imag), 
                    xytext=(5, 10), textcoords='offset points')
        
        # Transformed point
        ax2.scatter(w.real, w.imag, s=100, c='blue', zorder=5)
        ax2.annotate(f'{w:.1f}', (w.real, w.imag), 
                    xytext=(5, 10), textcoords='offset points')
        
        # Connect with arrow
        ax2.annotate('', xy=(w.real, w.imag), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', alpha=0.5, color='gray'))
    
    ax1.set_xlim(-4, 4)
    ax1.set_ylim(-1, 3)
    ax1.set_xlabel('Re(z)')
    ax1.set_ylabel('Im(z)')
    ax1.set_title('Original Line z = x + i')
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    
    ax2.set_xlim(-2, 10)
    ax2.set_ylim(-6, 6)
    ax2.set_xlabel('Re(w)')
    ax2.set_ylabel('Im(w)')
    ax2.set_title('Transformed Parabola w = z²')
    ax2.grid(True, alpha=0.3)
    ax2.set_aspect('equal')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Complex Function Mapping: z² transformation of line z = x + i")
    print("\nRunning visualizations...")
    
    # Run all demonstrations
    analyze_transformation()
    plot_line_mapping()
    plot_point_mapping_examples()
    plot_multiple_lines()
    interactive_point_demo()
    
    print("\nAll visualizations complete!")
    print("\nTo run individual functions:")
    print("- plot_line_mapping(): Basic line mapping")
    print("- plot_point_mapping_examples(): Specific point examples")
    print("- plot_multiple_lines(): Multiple horizontal lines")
    print("- analyze_transformation(): Mathematical analysis")
    print("- interactive_point_demo(): Sample points on the line")
