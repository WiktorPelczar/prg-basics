###
# Sums numbers entered by user
#
total_sum = 0
count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    count += 1

if count > 0: # Sprawdzenie, czy wprowadzono jakąkolwiek liczbę
    srednia_arytmetyczna = total_sum / count
    print(f"Suma wszystkich liczb: {total_sum}")
    print(f"Średnia arytmetyczna: {srednia_arytmetyczna}")
