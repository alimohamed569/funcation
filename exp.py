def get_max_length():
    while True:
            max_length = int(input("Enter the maximum length in feet: "))
            if max_length > 0:
                return max_length
            else:
                print("Please enter a valid positive integer.")
