# while statement

nbr = 1

while nbr <= 10 :
    # if nbr == 3 :
    #     break
    if nbr % 2 == 1 :
        nbr += 1
        continue
    print(f"nbr is {nbr ** 2}")
    nbr = nbr + 1 # Don't forget to do this!!!

print("Done ...")

# if statement

# Conditional Expressions

# final_test_score = 72  # 0 to 100

# the_student_passed = True if final_test_score > 69 else False

# if final_test_score >= 70 :
#     the_student_passed = True
# else :
#     the_student_passed = False

# print(f"The student passed: {the_student_passed}")



# empty string

# empty_string = ""

# if len(empty_string) == 0 :
#     print("The empty string is empty!")
# else :
#     print("The empty string is NOT empty!")


# if customer sales >= 1000 then A
# if customer sales >= 100 and < 1000 then B
# if customer sales < 100 then C

# customer_sales = 42 # should be a C

# if customer_sales >= 1000 :
#     customer_rating = "A"
# elif customer_sales >= 100 and customer_sales < 1000 :
#     customer_rating = "B"
# else :
#     customer_rating = "C"

# print(f"Customer rating is {customer_rating}")


# color = "red"

# if color == "green" :
#     print("Drive on thru")
# elif color == "yellow" :
#     print("Drive on thru carefully!")
# elif color == "red" :
#     print("STOP!")
# else :
#     print("Treat as a stop sign")


# tf = None

# if tf :
#     print("tf is True")
#     print("tf is not False")

# elif not tf :
#     print("tf is False")
#     print("tf is not True")

# else :
#     print("tf is neither True or False")

# print("Done ...")