from queue import Queue

waiting_list = Queue()
print(waiting_list)

waiting_list.put("Ali")
waiting_list.put("Vali")
waiting_list.put("G'ani")

print(waiting_list.get())
print(waiting_list.get())
print(waiting_list.get())