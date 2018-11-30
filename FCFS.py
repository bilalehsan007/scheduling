arr=[]
total_w=[]
n=int(raw_input('Total processes: '))
start_time=0
total=0

for i in xrange(n):
	arr.append([])
	arr[i].append(raw_input('process name: '))
	arr[i].append(int(raw_input('arrival time: ')))
	arr[i].append(int(raw_input('burst time: ')))
	total_w.append([])
	total_w[i].append(int(start_time-arr[i][1]))
	start_time=start_time+arri][2]

arr.sort(key=lambda a:a[1])
print 'Process \t Arrival time \t Burst time \t waiting time'

for i in xrange(n):
	print arr[i][0],' \t\t',arr[i][1],' \t\t',arr[i][2],' \t\t',total_w[i]