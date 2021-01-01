from collections import Counter
n = input().strip()
count_number = Counter(n)

mod_number = []

mod_number.append([])
mod_number.append(['1','4','7'])
mod_number.append(['2','5','8'])
mod_number = [[x for x in d if x in count_number] for d in mod_number]

sum_digit = sum(int(digit)*count_number[digit] for digit in count_number)

mod = sum_digit%3


if mod:
   
    count_digit_same_mode = sum(int(count_number[number]) for number in mod_number[mod])
    
    number_digit_delete = 1
    if not count_digit_same_mode:
        mod = 3 - mod   
        number_digit_delete = 2

    for _ in mod_number[mod]:
        
        __ = min(number_digit_delete, count_number[_])
        number_digit_delete -= __
        count_number[_] -= __

for _ in sorted(count_number.keys(), reverse=True):
    print(_*count_number[_], end="")

