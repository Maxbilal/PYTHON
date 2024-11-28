def count_occurrences():
    num = []
    n = int(input("Enter the number of elements: "))
    
    for i in range(n):
        a = input("Enter an element: ")
        num.append(a)
    
    print("List of elements:", num)
    
    element_to_count = input("Enter an element to count: ")
    count = num.count(element_to_count)
    
    print("It occurs", count, "times.")

count_occurrences()
