import time
score = 0
name = "Adam"
questionData = [
				["best A-level Subject", ["Music", "Biology", "Art", "Computing"], 3],
				["best base", ["Denary", "Binary", "Hexadecimal"], 1],
				["best cookie type", ["Oreos", "Choco Chip", "Hobnobs"], 1],
				["mode of names in the LVI computing class", ["Ashby", "Adam", "Tom", "James", "Simon"], 1],
				["best os", ["UNIX", "DOS"], 0]]
print("Disappointing %s; your score was %s%..." % (name, (score/(len(questionData))))