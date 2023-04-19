from datetime import datetime 

user_input =input("enter your goal with its date time seperated by ':' \n")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]

deadline_date =datetime.strptime(deadline, "%d-%m-%Y")
today_date =datetime.today()

#calculate haw many days untill the deadline 
the_rest = deadline_date-today_date
hours_till = int(the_rest.total_seconds() / 60 / 60)- the_rest.days*24

print(f'Dear user \nthere is {the_rest.days} day and {hours_till} hour \nleft until the deadline ')
