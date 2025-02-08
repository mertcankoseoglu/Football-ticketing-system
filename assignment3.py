input_list = []
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ticket_list = []        # unsold seat list for every category
rows = []               # rows are letters
columns = []            # columns are numbers
sold_ticket = []        # sold seat for every category


def create_category(add_category):
    global ticket_list
    global rows
    global columns                          # add_category[0][9] must be 1 or 2 (marathon and back-goal tribune)
    x = add_category[1].split("x")          # x[0] is row and x[1] is column (limit is 26 for row and column)
    if (0 < int(add_category[0][9]) < 3) and (int(x[0]) < 27) and ((int(x[1])) < 27):
        catg_found = False
        if not ticket_list:
            seat = int(int(x[0]) * int(x[1]))       # number of seat
            catg_ticket = [add_category[0]]         # list in list (add_category[0] is category)
            a = []
            for letter in alphabet[:int(x[0])]:
                for num in range(int(x[1])):
                    num_str = str(num)              # to use join function
                    seat_list = [letter, num_str]   # seat_list is seats in category
                    new_list = "".join(seat_list)   # join letter and number
                    a.append(new_list)
            catg_ticket.append(a)                   # 0.index is category name and 1.index is seats
            ticket_list.append(catg_ticket)         # ticket_list is list of list

            # rows list is row list for every category
            row1 = [add_category[0]]
            b = alphabet[:int(x[0])]
            row1.append(b)
            rows.append(row1)

            # columns list is column for every category
            column1 = [add_category[0]]
            c = list(range(int(x[1])))
            column1.append(c)
            columns.append(column1)
            with open('output.txt', 'a') as output_file:
                output_file.write("The category " + add_category[0] + " having "
                                  + str(seat) + " seats has been created\n")
                print("The category " + add_category[0] + " having "
                      + str(seat) + " seats has been created")
        else:
            for r in range(len(ticket_list)):
                if ticket_list[r][0] == add_category[0]:
                    with open('output.txt', 'a') as output_file:
                        output_file.write("Warning: Cannot create the category for the second time. "
                                          + "The stadium has already " + add_category[0] + ".\n")
                        print("Warning: Cannot create the category for the second time. "
                              + "The stadium has already " + add_category[0] + ".")
                    catg_found = True
            if not catg_found:
                x = add_category[1].split("x")
                seat = int(int(x[0]) * int(x[1]))
                catg_ticket = [add_category[0]]
                a = []
                for letter in alphabet[:int(x[0])]:
                    for num in range(int(x[1])):
                        num_str = str(num)
                        seat_list = [letter, num_str]
                        new_list = "".join(seat_list)
                        a.append(new_list)
                catg_ticket.append(a)
                ticket_list.append(catg_ticket)
                row1 = [add_category[0]]
                b = alphabet[:int(x[0])]
                row1.append(b)
                rows.append(row1)
                column1 = [add_category[0]]
                c = list(range(int(x[1])))
                column1.append(c)
                columns.append(column1)
                with open('output.txt', 'a') as output_file:
                    output_file.write("The category " + add_category[0] + " having "
                                      + str(seat) + " seats has been created\n")
                    print("The category " + add_category[0] + " having "
                          + str(seat) + " seats has been created")


def sell_ticket(sell_tic):
    global ticket_list
    global sold_ticket
    for catg in range(len(ticket_list)):
        if ticket_list[catg][0] == sell_tic[2]:   # check if category names are same
            catg_list = [sell_tic[2]]   # it is used for sold seat
            seat_list = []
            for seat in sell_tic[3:]:   # seats in input file
                if len(seat) < 4:       # not range seats
                    if (seat[0] not in rows[catg][1]) and (int(seat[1:]) not in columns[catg][1]):
                        print("Error: The category " + sell_tic[2]
                              + " has less row and column than the specified index " + seat + "!")
                        with open('output.txt', 'a') as output_file:
                            output_file.write("Error: The category " + sell_tic[2]
                                              + " has less row and column than the specified index " + seat + "!\n")
                    elif (seat[0] in rows[catg][1]) and (int(seat[1:]) not in columns[catg][1]):
                        print("Error: The category " + sell_tic[2]
                              + " has less column than the specified index " + seat + "!")
                        with open('output.txt', 'a') as output_file:
                            output_file.write("Error: The category " + sell_tic[2]
                                              + " has less column than the specified index " + seat + "!\n")
                    elif (seat[0] not in rows[catg][1]) and (int(seat[1:]) in columns[catg][1]):
                        print("Error: The category " + sell_tic[2]
                              + " has less row than the specified index " + seat + "!")
                        with open('output.txt', 'a') as output_file:
                            output_file.write("Error: The category " + sell_tic[2]
                                              + " has less row than the specified index " + seat + "!\n")
                    else:
                        if seat in ticket_list[catg][1]:   # it is available to sell
                            # remove it from ticket_list and append it sold_ticket
                            ticket_list[catg][1].remove(seat)
                            seat_type = [seat, sell_tic[1]]
                            seat_list.append(seat_type)
                            print("Success: " + sell_tic[0] + " has bought " + seat + " at " + sell_tic[2])
                            with open('output.txt', 'a') as output_file:
                                output_file.write("Success: " + sell_tic[0] + " has bought "
                                                  + seat + " at " + sell_tic[2] + "\n")
                        else:
                            # it is not is ticket_list, it was already sold
                            print("Warning: The seat " + seat + " cannot be sold to "
                                  + sell_tic[0] + " since it was already sold!")
                            with open('output.txt', 'a') as output_file:
                                output_file.write("Warning: The seat " + seat + " cannot be sold to "
                                                  + sell_tic[0] + " since it was already sold!\n")
                else:
                    # range seat
                    new_seat = seat.split('-')      # split range "-"
                    if (new_seat[0][0] not in rows[catg][1]) and (int(new_seat[1]) not in columns[catg][1]):
                        print("Error: The category " + sell_tic[2]
                              + " has less row and column than the specified index " + seat + "!")
                        with open('output.txt', 'a') as output_file:
                            output_file.write("Error: The category " + sell_tic[2]
                                              + " has less row and column than the specified index " + seat + "!\n")
                    elif (new_seat[0][0] in rows[catg][1]) and (int(new_seat[1]) not in columns[catg][1]):
                        print("Error: The category " + sell_tic[2]
                              + " has less column than the specified index " + seat + "!")
                        with open('output.txt', 'a') as output_file:
                            output_file.write("Error: The category " + sell_tic[2]
                                              + " has less column than the specified index " + seat + "!\n")
                    elif (new_seat[0][0] not in rows[catg][1]) and (int(new_seat[1]) in columns[catg][1]):
                        print("Error: The category " + sell_tic[2]
                              + " has less row than the specified index " + seat + "!")
                        with open('output.txt', 'a') as output_file:
                            output_file.write("Error: The category " + sell_tic[2]
                                              + " has less row than the specified index " + seat + "!\n")
                    else:
                        seats = []      # it is a list for every seat in range
                        for x in range(int(new_seat[0][1:]), int(new_seat[1]) + 1):
                            row = new_seat[0][0]
                            column = str(x)
                            new_seats = [row, column]
                            new_seat1 = "".join(new_seats)
                            seats.append(new_seat1)
                        # every seat in range must be unsold to sell
                        check = all(item in ticket_list[catg][1] for item in seats)
                        if check:
                            # sell and add it to sold_ticket and remove from ticket_list
                            for el in seats:
                                ticket_list[catg][1].remove(el)
                                seat_type = [el, sell_tic[1]]
                                seat_list.append(seat_type)
                            print("Success: " + sell_tic[0] + " has bought "
                                  + seat + " at " + sell_tic[2])
                            with open('output.txt', 'a') as output_file:
                                output_file.write("Success: " + sell_tic[0] + " has bought "
                                                  + seat + " at " + sell_tic[2] + "\n")
                        else:
                            # some seats are already sold in range
                            print("Error: The seats " + seat + " cannot be sold to " + sell_tic[0]
                                  + " due some of them have already been sold!")
                            with open('output.txt', 'a') as output_file:
                                output_file.write("Error: The seats " + seat + " cannot be sold to " + sell_tic[0]
                                                  + " due some of them have already been sold!\n")
            catg_list.append(seat_list)     # sold seat in one category
            sold_ticket.append(catg_list)   # list of list for sold seat


def cancel_ticket(cancel_tic):
    global ticket_list
    global sold_ticket
    for catg in range(len(ticket_list)):
        if ticket_list[catg][0] == cancel_tic[0]:       # check if the category names are same
            for seat in cancel_tic[1:]:
                if (seat[0] not in rows[catg][1]) and (int(seat[1:]) not in columns[catg][1]):
                    print("Error: The category " + cancel_tic[0]
                          + " has less row and column than the specified index " + seat + "!")
                    with open('output.txt', 'a') as output_file:
                        output_file.write("Error: The category " + cancel_tic[0]
                                          + " has less row and column than the specified index " + seat + "!\n")
                elif (seat[0] in rows[catg][1]) and (int(seat[1:]) not in columns[catg][1]):
                    print("Error: The category " + cancel_tic[0]
                          + " has less column than the specified index " + seat + "!")
                    with open('output.txt', 'a') as output_file:
                        output_file.write("Error: The category " + cancel_tic[0]
                                          + " has less column than the specified index " + seat + "!\n")
                elif (seat[0] not in rows[catg][1]) and (int(seat[1:]) in columns[catg][1]):
                    print("Error: The category " + cancel_tic[0]
                          + " has less row than the specified index " + seat + "!")
                    with open('output.txt', 'a') as output_file:
                        output_file.write("Error: The category " + cancel_tic[2]
                                          + " has less row than the specified index " + seat + "!\n")
                else:
                    if seat not in ticket_list[catg][1]:
                        # sold seat is cancelled, remove from sold_ticket and add to ticket_list
                        ticket_list[catg][1].append(seat)
                        for item in sold_ticket:
                            if item[0] == ticket_list[catg][0]:
                                for seat_type in item[1]:
                                    if seat_type[0] == seat:
                                        item[1].remove(seat_type)
                        print("Success: The seat " + seat + " at " + cancel_tic[0]
                              + " have been canceled and now ready to sell again")
                        with open('output.txt', 'a') as output_file:
                            output_file.write("Success: The seat " + seat + " at " + cancel_tic[0]
                                              + " have been canceled and now ready to sell again\n")
                    else:
                        # it is not sold, nothing to cancel
                        print("Error: The seat " + seat + " at " + cancel_tic[0]
                              + " has already been free! Nothing to cancel")
                        with open('output.txt', 'a') as output_file:
                            output_file.write("Error: The seat " + seat + " at " + cancel_tic[0]
                                              + " has already been free! Nothing to cancel\n")


def balance(category):
    stud_count = 0      # count the student ticket in sold seat, 10 dollars
    full_count = 0      # count the full ticket in sold seat, 20 dollars
    seas_count = 0      # count the season ticket in sold seat, 250 dollars
    for item in sold_ticket:
        if item[0] == category[0]:
            for seat_type in item[1]:
                if seat_type[1] == "student":
                    stud_count += 1
                elif seat_type[1] == "full":
                    full_count += 1
                elif seat_type[1] == "season":
                    seas_count += 1

    revenues = 10*stud_count + 20*full_count + 250*seas_count       # formula for revenues
    print("category report of " + category[0])
    print("------------------------------")
    print("Sum of students = ", stud_count, ",", "Sum of full pay = ", full_count, ","
          " Sum of season ticket = ", seas_count, ",", "and Revenues = ", revenues, "Dollars")
    with open('output.txt', 'a') as output_file:
        output_file.write("category report of " + category[0] + "\n")
        output_file.write("------------------------------\n")
        output_file.write("Sum of students = " + str(stud_count) + "," + " Sum of full pay = " + str(full_count) + "," +
                          " Sum of season ticket = " + str(seas_count) + "," + " and Revenues = " +
                          str(revenues) + " Dollars\n")


def show_category(lay_out):
    print("Printing category layout of ", lay_out[0])
    with open('output.txt', 'a') as output_file:
        output_file.write("Printing category layout of " + lay_out[0] + "\n")
    for row in rows:
        if row[0] == lay_out[0]:            # check the category name
            for letter in row[1][::-1]:     # every letter from row, reverse it
                letter_list = [letter]
                for element in ticket_list:
                    if element[0] == lay_out[0]:
                        for seat in element[1]:
                            if seat[0] == letter:
                                index = int(seat[1]) + 1
                                letter_list.insert(index, "X")  # X for unsold seat
                for item in sold_ticket:
                    if item[0] == lay_out[0]:
                        for seat in item[1]:
                            if seat[0][0] == letter:
                                index = int(seat[0][1]) + 1
                                if seat[1] == "student":
                                    letter_list.insert(index, "S")  # S for student seat
                                elif seat[1] == "full":
                                    letter_list.insert(index, "F")  # F for full seat
                                elif seat[1] == "season":
                                    letter_list.insert(index, "T")  # T for season seat
                print(" ".join(letter_list))  # join to letters seats in one row
                for let_line in letter_list:
                    with open('output.txt', 'a') as output_file:
                        output_file.write(let_line + " ")
                with open('output.txt', 'a') as output_file:
                    output_file.write("\n")

    # print the columns numbers
    str_col = []
    for column in columns:
        if column[0] == lay_out[0]:         # check for the same category
            for num in column[1]:
                str_col.append(str(num))    # convert string to use join function
                with open('output.txt', 'a') as output_file:
                    output_file.write(" " + str(num))
            with open('output.txt', 'a') as output_file:
                output_file.write("\n")
    print(" ", " ".join(str_col))


with open('input.txt', 'r') as input_file:
    for line in input_file:                 # read the input file line by line
        input_list.append(line.split())

# check the input list to call to function
for i in range(len(input_list)):
    if input_list[i][0] == 'CREATECATEGORY':
        input_list[i].pop(0)
        create_category(input_list[i])
    elif input_list[i][0] == 'SELLTICKET':
        input_list[i].pop(0)
        sell_ticket(input_list[i])
    elif input_list[i][0] == 'CANCELTICKET':
        input_list[i].pop(0)
        cancel_ticket(input_list[i])
    elif input_list[i][0] == 'BALANCE':
        input_list[i].pop(0)
        balance(input_list[i])
    elif input_list[i][0] == 'SHOWCATEGORY':
        input_list[i].pop(0)
        show_category(input_list[i])
