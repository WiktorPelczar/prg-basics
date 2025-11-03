###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_task = 20
tasks_ok =int(input('Wpisz liczbę:'))
test_passed = False

if tasks_ok >=10 and total_task >= tasks_ok:
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')