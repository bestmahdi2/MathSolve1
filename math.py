from random import choice, choices
from math import sqrt
import operator
from numpy import cbrt


class Math:
	def get(self):
		number = input("enter your number : ")

		if number == "":
			self.get()

		elif number != "exit":
			# try:
				self.mains(int(number))
			# except:
			# 	print("\nincorrect\n")
			# 	self.get()
		else:
			pass


	def mains(self, onumber):
		#all operator want to use
		states = ["+", "-", "*", "/", "**"]

		#dic to translate sign to operators
		ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "**": operator.pow}

		#a list to collect all answers
		answer = []

		#to test 100k state
		x = 0
		while x < 100000:
			
			#choose a operator
			x1 = choice(states)
			x2 = choice(states)
			#convert operators
			ox1 = ops[x1]
			ox2 = ops[x2]

			#creat list of numbers 
			numbers = [onumber, onumber, onumber]

			#to use sqrt for random number in numbers list
			count_number_sqr = [0, 1, 2]
			for i in count_number_sqr:
				sqr = choice([True, False])
				if sqrt(onumber).is_integer() and sqr:
					numbers[i] = int(sqrt(onumber))

				#to use cube root for random number in numbers list
				if cbrt(onumber).is_integer() and sqr:
					numbers[i] = int(cbrt(onumber))


			#calculate result
			result = ox2(ox1(numbers[0], numbers[1]), numbers[2])


			#sqrt string adding for next print
			c = 0
			while c < len(numbers):
				if numbers[c] == sqrt(onumber):
					numbers[c] = "sqrt({})".format(onumber)
			
				elif numbers[c] == cbrt(onumber):
					numbers[c] = "cbrt({})".format(onumber)
									
				c += 1


			if result == 6:
				answer.append("(" + str(numbers[0]) + str(x1) + str(numbers[1]) + ")" + str(x2) + str(numbers[2]))
				# answer.append([numbers[0], numbers[1], numbers[2]])

			# to use | or not
			if result == (-6):
				answer.append("|" + "(" + str(numbers[0]) + str(x1) + str(numbers[1]) + ")" + str(x2) + str(numbers[2]) + "|")		
				# answer.append([numbers[0], numbers[1], numbers[2]])

			x += 1

		#remove duplicated answers
		answer = list(set(answer))
		for i in answer:
			print(i)
		print()
		self.get()


M = Math()
M.get()
input()


			# edit_numbers = [i for i in numbers if i == onumber]
			# edit_numbers = edit_numbers + [str("sqrt({})").format(i**2) for i in numbers if i != onumber]
			# numbers = edit_numbers