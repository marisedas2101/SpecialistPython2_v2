# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67

def sort_choice(nums, key=lambda el: el, reverse=False):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            comp = key(nums[j].replace('-', '')) > key(nums[m].replace('-', '')) if reverse else key(nums[j].replace('-', '')) < key(nums[m].replace('-', ''))
            if comp:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1

phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]
sort_choice(phones, int)
print(phones)
