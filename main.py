def get_max_length():
    while True:
        try:
            max_length = int(input("Enter the maximum length in feet: "))
            if max_length > 0:
                return max_length
            else:
                print("Please enter a valid positive integer.")
        except ValueError:
            print("Please enter a valid positive integer.")

def print_conversion_chart(max_length):
    print(f"{'Feet':<10}{'Meters':<10}")
    print("-" * ss20)

    for feet in range(1, max_length + 1):
        meters = feet * 0.3048
        print(f"{feet:<10}{meters:<10.4f}")

    max_length = get_max_length()
def main():
    print_conversion_chart(max_length)

if __name__ == "__main__":
    main()
