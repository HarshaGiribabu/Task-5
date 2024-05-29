list = [[5, 6, 3], ["hrs", 3, "hello"], [9, "best", 4]]
print("The original list : " + str(list))
string_instances = [elem for sublist in list for elem in sublist if isinstance(elem, str)]
print("The string instances : " + str(string_instances))
int_instances = [elem for sublist in list for elem in sublist if isinstance(elem, int)]
print("The integer instances : " + str(int_instances))

