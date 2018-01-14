# Computing the volume of a cylinder
# by Yiyang 14/01/18

_radius = float(input("Radius of the cylinder = "))
_length = float(input("Length of the cylinder = "))

_area = (_radius ** 2) * 3.141593
_volume = _area * _length

print("Volume of the cylinder = {0:.2f}".format( _volume))
