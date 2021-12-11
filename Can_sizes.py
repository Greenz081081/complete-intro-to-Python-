import math
def main():
    name = "#1 picnic"
    Radius = 6.63
    Height = 10.16
    volume = cylinder_volume(Radius, Height)
    surf_area = cylinder_surface_area(Radius, Height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.1f}")

    name = "#1 Tall"
    Radius = 7.78
    Height = 11.91
    volume = cylinder_volume(Radius, Height)
    surf_area = cylinder_surface_area(Radius, Height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.1f}")

    name = "#2"
    Radius = 8.73
    Height = 11.59
    volume = cylinder_volume(Radius, Height)
    surf_area = cylinder_surface_area(Radius, Height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.1f}")

    name = "#2.5"
    Radius = 10.32
    Height = 11.91
    volume = cylinder_volume(Radius, Height)
    surf_area = cylinder_surface_area(Radius, Height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.1f}")

    name = "#3 Cylinder"
    Radius = 10.79
    Height = 17.78
    volume = cylinder_volume(Radius, Height)
    surf_area = cylinder_surface_area(Radius, Height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.1f}")

    name = "#5"
    Radius = 13.02
    Height = 14.29
    volume = cylinder_volume(Radius, Height)
    surf_area = cylinder_surface_area(Radius, Height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.1f}")

    name = "#6z"
    Radius = 5.40
    Height = 8.89
    volume = cylinder_volume(Radius, Height)
    surf_area = cylinder_surface_area(Radius, Height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.1f}")

    name = "#8z short"
    Radius = 6.83
    Height = 7.62
    volume = cylinder_volume(Radius, Height)
    surf_area = cylinder_surface_area(Radius, Height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.1f}")

    name ="#10"
    Radius = 15.72
    Height = 17.78
    volume = cylinder_volume(Radius, Height)
    surf_area = cylinder_surface_area(Radius, Height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.1f}")

    name = "#211"
    Radius = 6.83
    Height = 12.38
    volume = cylinder_volume(Radius, Height)
    surf_area = cylinder_surface_area(Radius, Height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.1f}")

    name = "#300"
    Radius = 7.62
    Height = 11.27
    volume = cylinder_volume(Radius, Height)
    surf_area = cylinder_surface_area(Radius, Height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.1f}") 

    name = "#303"
    Radius = 8.10
    Height = 11.11
    volume = cylinder_volume(Radius, Height)
    surf_area = cylinder_surface_area(Radius, Height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.1f}")


def cylinder_volume(Radius, Height):
    volume = math.pi * Radius ** 2 * Height
    return volume



def cylinder_surface_area(Radius, Height):
    surf_area = math.pi * 2 * Radius * (Radius + Height)
    return surf_area



main()

