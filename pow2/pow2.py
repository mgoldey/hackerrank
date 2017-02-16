# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
from copy import deepcopy
val=int(input())
#val=16

twos=[2**i for i in range(27)]
twos.reverse()

def get_unique(ival):
	way=[0 for i in range(27)]
	while (ival>0):
		maxval=int(math.floor(math.log(ival)/math.log(2))+1)
		ival-=twos[-maxval]
		way[-maxval]+=1
	return way		

ways=[]
ways.append(get_unique(val))

def break_two(ival):
	way=get_unique(ival)
	maxval=int(math.floor(math.log(ival)/math.log(2)))
	way=[0 for i in range(27)]
	way[-maxval]=2
	return way


def get_new_ways(way):
	#print(iway)
	iways=[]
	def get_indices(li):
		li2=deepcopy(li)
		inds=[]
		while li2.count(1)>0:
			inds.append(li2.index(1))
			li2[inds[-1]]=0
		while li2.count(2)>0:
			inds.append(li2.index(2))
			li2[inds[-1]]=0
		return inds

	def sum_lists(l1,l2):
		l3=[0 for i in range(27)]
		for i in range(27):
			l3[i]=l1[i]+l2[i]
		return l3

	iway=deepcopy(way)
	do_vals=get_indices(iway)
	# print(do_vals)
	for ival in do_vals:
		iway=deepcopy(way)
		# print("ival is",ival)
		# print(twos[ival])
		if ival==26:
			continue
		new_way=deepcopy(iway)
		# print("iway is ",iway)
		if new_way[ival+1]>0:
			continue
		new_way[ival]-=1
		new_way=sum_lists(new_way,break_two(twos[ival]))
		iways.append(new_way)
		vals=get_indices(new_way)
		if (len(vals)!=0):
			for iway in get_new_ways(new_way):
				iways.append(iway)
	return iways
ways+=get_new_ways(ways[0])

def check_for_duplicates(ways):
	bad=[]
	lw=len(ways)
	for i in range(lw):
		for j in range(i):
			if ways[i]==ways[j]:
				bad.append(i)
	return len(bad)

print(len(ways)-check_for_duplicates(ways))