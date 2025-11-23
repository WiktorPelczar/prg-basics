N = 10
sum_even = 0

# 1. Inicjalizacja licznika (zastępuje start pętli for)
i = 1 

# Calculate the sum of even numbers
# 2. Warunek kontynuacji: pętla działa, dopóki i jest mniejsze lub równe N
while i <= N:
    
    # Warunek sprawdzenia parzystości (niezmieniony)
    if i % 2 == 0:
        sum_even += i
        
    # 3. Zwiększanie licznika (konieczne, aby uniknąć pętli nieskończonej)
    i += 1 

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")