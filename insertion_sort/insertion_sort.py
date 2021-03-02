def insertion_sort(og_list):
    for i in range(len(og_list)):

        # print("THIS IS I", i)

        bool_err = type(og_list[i]) is int
        if bool_err is True:
            temp = og_list[i]
            j = i - 1

            while j >= 0 and temp < og_list[j]:
                og_list[j + 1] = og_list[j]
                j -= 1

            og_list[j + 1] = temp
        else:
            print("Error")
            return "Error"         
    print(og_list)
    return og_list

insertion_sort([8,4,-23, 8,16,15])
