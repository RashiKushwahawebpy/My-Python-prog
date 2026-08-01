#22. Match Enums
from enum import Enum
class Color(Enum):
	RED = 1
	GREEN = 2
color = Color. RED
match color:
	case Color. RED:
		print("Red")
	case Color. GREEN:
		print("Green")