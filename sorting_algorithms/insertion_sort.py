def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        if a_list[i] < a_list[i - 1]:
            for j in range(i, -1):
                if a_list[i] < a_list[j]:
                    a_list[i], a_list[j] = a_list[j], a_list[i]
                    i-=1

