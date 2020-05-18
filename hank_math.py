# HANK MATH!
# by Timothy Merritt 2020
#
# A simple program for practicing math problems. Displays addition
# and subtraction problems, tracks results, and exports scores to 
# separate file for score-keeping.
#
# To do:
# * Use class instances to generate tabulate-style table with final
# results
# --------------------------------------------------------------------

import random, os, datetime, platform
from tabulate import tabulate

# Global score-keeping variables
RIGHT_ANSWERS = 0
WRONG_ANSWERS = 0
TOTAL_QUESTIONS = 0
score_list = []

class Score():
	""" Class for creating instances of each problem/answer set """
	def __init__(self, num1, num2, user_ans, result):
		self.num1 = num1
		self.num2 = num2
		self.user_ans = user_ans
		self.result = result

# Clears screen based on OS, then displays program logo
def logo():
	if platform.system() == "Windows":
		os.system('cls')
	else:
		os.system('clear')
	print("""

██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗    ███╗   ███╗ █████╗ ████████╗██╗  ██╗██╗
██║  ██║██╔══██╗████╗  ██║██║ ██╔╝    ████╗ ████║██╔══██╗╚══██╔══╝██║  ██║██║
███████║███████║██╔██╗ ██║█████╔╝     ██╔████╔██║███████║   ██║   ███████║██║
██╔══██║██╔══██║██║╚██╗██║██╔═██╗     ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║╚═╝
██║  ██║██║  ██║██║ ╚████║██║  ██╗    ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝
  Answer the math problems. Press 'Enter' to continue. Type 'q' to quit.
	""")

# Function to center passed variables; used for positioning
# math problem centered under logo
def border_line(x):
	word_length = len(x)
	border = (77 - word_length) // 2
	border_amount = (" " * border)
	print(border_amount, x, border_amount)

# --------------------------------------------------------------------
# -----------E Q U A T I O N  C H O I C E  &  D I S P L A Y-----------
# --------------------------------------------------------------------

# Display the math problem with the two randomly chasen numbers
def choose_problem_type(num1, num2):
	selector = random.randint(0,1)
	if selector == 1:
		correct_answer = add_problem(num1, num2)
		return correct_answer
	else:
		correct_answer = sub_problem(num1, num2)
		return correct_answer

def add_problem(num1, num2):
	# format problem with digits right-aligned
	border_line("{:3d}".format(num1))
	border_line("+ ""{:2d}".format(num2))
	border_line("-----")
	correct_answer = num1 + num2
	return correct_answer

def sub_problem(num1, num2):
	if num1 >= num2:
		border_line("{:3d}".format(num1))
		border_line("- ""{:2d}".format(num2))
		border_line("-----")
		correct_answer = num1 - num2
		return correct_answer
	else:
		border_line("{:3d}".format(num2))
		border_line("- ""{:2d}".format(num1))
		border_line("-----")
		correct_answer = num2 - num1
		return correct_answer

# Get user answer as string, center under problem
def get_user_answer():
	while True:
		try:
			answer = input(" " * 39)
			return answer
		except Exception:
			continue

# --------------------------------------------------------------------
# ---------------------------R E S U L T S----------------------------
# --------------------------------------------------------------------

# Creates a list of current problem numbers, user answer, and correct
# answer; adds that list to global list
def add_stats(num1, num2, user_ans, result):
	global score_list
	problem = Score(num1, num2, user_ans, result)
	list_entry = [problem.num1, problem.num2, problem.user_ans, problem.result]
	score_list.append(list_entry)

# Exports/appends global results to external file 'scores.txt' with 
# current datetime
def export_final_results():
	global TOTAL_QUESTIONS
	global RIGHT_ANSWERS
	global WRONG_ANSWERS
	with open('scores.txt', 'a') as f:
		f.write("\n")
		f.write("-" * 33)
		f.write("\n")
		when = str(f"{datetime.datetime.now():%Y-%m-%d %-I:%M %p}")
		f.write(when)
		f.write("\n")
		TOTAL_QUESTIONS = str(TOTAL_QUESTIONS)
		RIGHT_ANSWERS = str(RIGHT_ANSWERS)
		WRONG_ANSWERS = str(WRONG_ANSWERS)
		f.write("Total Questions: "+TOTAL_QUESTIONS+"\nRight: "+RIGHT_ANSWERS+"\nWrong: "+WRONG_ANSWERS)

# Print simplified final results
def final_results():
	global TOTAL_QUESTIONS
	global RIGHT_ANSWERS
	global WRONG_ANSWERS
	logo()
	print((30 * " "), "Total Questions: ", TOTAL_QUESTIONS)
	print((30 * " "), "Right: ", RIGHT_ANSWERS)
	print((30 * " "), "Wrong: ", WRONG_ANSWERS)
	with open('scores.txt', 'r') as f:
		f.read()
	input("\n"+30 * " "+"Press any key to exit.")

# --------------------------------------------------------------------
# -----------------------M A I N  P R O G R A M-----------------------
# --------------------------------------------------------------------

def main():
	global TOTAL_QUESTIONS
	global RIGHT_ANSWERS
	global WRONG_ANSWERS
	user_answer = ""
	while user_answer != "q":
		try:
			TOTAL_QUESTIONS += 1
			logo()
			print((" " * 34), "Problem ", TOTAL_QUESTIONS, "\n")
			num1 = random.randint(1,12)
			num2 = random.randint(1,12)
			correct_answer = choose_problem_type(num1, num2)
			user_answer = get_user_answer()
			if user_answer.lower() == "q":
				TOTAL_QUESTIONS -= 1
				pass	
			elif int(user_answer) == correct_answer:
				RIGHT_ANSWERS += 1
				add_stats(num1, num2, user_answer, correct_answer)
				print("\n", " " * 16, end='')
				input("Correct! Nice job! Press any key to continue.") # 77-45
			elif int(user_answer) != correct_answer:
				WRONG_ANSWERS += 1
				add_stats(num1, num2, user_answer, correct_answer)
				print("\n", " " * 27,"Sorry, the answer was", correct_answer, ".") # 77-(23~24)
				print(" " * 29, end='')
				input("Press any key to continue.") # 77-26 // 2
		except KeyboardInterrupt:
			break

	export_final_results()
	final_results()

	# print(tabulate(score_list, headers=["Number", "Number", "User", "Correct"], numalign="right", showindex=False, tablefmt="presto"))

main()