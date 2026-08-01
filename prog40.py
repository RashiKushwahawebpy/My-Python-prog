#23. Match Data classes
#from data classes import data class
#@dataclass
class Point:
	x: int
	y: int
p = Point(10, 20)
match p:
	case Point(x=10, y=20):
		print("Matched") 
