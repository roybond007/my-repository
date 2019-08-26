from tkinter import *
import time
from tkinter import ttk
import random




#--------------------------------------------------------program to sort an array of data by bubble sort algorithem------------------------------------------------









def Bubble_sort(self):
	temp1 = None
	for i in range(self.no_of_lines):	
		self.draw_lines()
		self.update()
		time.sleep(self.time_delay)
		for j in range(i + 1,self.no_of_lines):
			if self.line_widget_y_co_array[i] > self.line_widget_y_co_array[j]:
				temp1 = self.line_widget_y_co_array[i]
				self.line_widget_y_co_array[i] = self.line_widget_y_co_array[j]
				self.line_widget_y_co_array[j] = temp1
	self.draw_lines()
	self.update()



def Insertion_sort(self):
	key = None
	for i in range(1,self.no_of_lines):
		self.draw_lines()
		self.update()
		time.sleep(self.time_delay)
		key = self.line_widget_y_co_array[i]
		j = i - 1
		while j >= 0 and self.line_widget_y_co_array[j] > key:
			self.line_widget_y_co_array[j + 1] = self.line_widget_y_co_array[j]
			j -= 1
		self.line_widget_y_co_array[j + 1] = key

	self.draw_lines()
	self.update()



def Selection_sort(self):
	length = len(self.line_widget_y_co_array)
	minn = None
	temp = None
	for i in range(0,length - 1):
		minn = i
		self.draw_lines()
		self.update()
		time.sleep(self.time_delay)
		for j in range(i + 1,length):
			if self.line_widget_y_co_array[minn] > self.line_widget_y_co_array[j]:
				minn = j
		temp = self.line_widget_y_co_array[minn]
		self.line_widget_y_co_array[minn] = self.line_widget_y_co_array[i]
		self.line_widget_y_co_array[i] = temp
		
		self.draw_lines()
		self.update()
		
		
		
		
		
		
		
		
		
def Merge_sort(self,l,u): 
	if l < u: 
		mid = int((l + u)/2) #Finding the mid of the array 
		Merge_sort(self,l,mid) # Sorting the first half 
		Merge_sort(self,mid + 1,u) # Sorting the second half 
		L = self.line_widget_y_co_array[l:mid + 1] # Dividing the array elements  
		R = self.line_widget_y_co_array[mid + 1:u + 1] # into 2 halves 
		i = j = 0
		k = l
        # Copy data to temp arrays L[] and R[] 
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				self.line_widget_y_co_array[k] = L[i] 
				i+=1
			else: 
				self.line_widget_y_co_array[k] = R[j] 
				j+=1
			k+=1
          
        # Checking if any element was left 
		while i < len(L): 
			self.line_widget_y_co_array[k] = L[i]
			i+=1
			k+=1
          
		while j < len(R): 
			self.line_widget_y_co_array[k] = R[j] 
			j+=1
			k+=1
	
		self.draw_lines()
		self.update()
		time.sleep(self.time_delay)
		




def partition(self,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = self.line_widget_y_co_array[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if  self.line_widget_y_co_array[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            self.line_widget_y_co_array[i],self.line_widget_y_co_array[j] = self.line_widget_y_co_array[j],self.line_widget_y_co_array[i] 
  
    self.line_widget_y_co_array[i+1],self.line_widget_y_co_array[high] = self.line_widget_y_co_array[high],self.line_widget_y_co_array[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def Quick_sort(self,low,high): 
    if low < high: 
        # pi is partitioning index, arr[p] is now 
        # at right place
        self.draw_lines()
        self.update()
        time.sleep(self.time_delay)
        pi = partition(self,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        Quick_sort(self, low, pi-1) 
        Quick_sort(self, pi+1, high) 
        self.draw_lines()
        self.update()
        time.sleep(self.time_delay)



def countingSort(arr, exp1): 
  
    n = len(arr) 
  
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
  
    # initialize count array as 0 
    count = [0] * (10) 
  
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = int((arr[i]/exp1)) 
        count[ (index)%10 ] += 1
  
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    # Build the output array 
    i = n-1
    while i>=0: 
        index = int((arr[i]/exp1)) 
        output[ count[ (index)%10 ] - 1] = arr[i] 
        count[ (index)%10 ] -= 1
        i -= 1
  
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
  
# Method to do Radix Sort 
def Radix_sort(self): 
  
    # Find the maximum number to know number of digits 
	max1 = max(self.line_widget_y_co_array) 
  
    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
	exp = 1
	self.draw_lines()
	self.update()
	time.sleep(self.time_delay)
	while int(max1/exp) > 0: 
		countingSort(self.line_widget_y_co_array,exp) 
		exp *= 10
		self.draw_lines()
		self.update()
		time.sleep(self.time_delay)
  

if __name__ == '__main__':
	
	arr_size = int(input("ENTER THE ARRAY SIZE : "))
	arr_data = [0] * arr_size
	data = input("ENTER THE ARRAY ELEMENTS SEPERATED BY SPACE : ")
	arr_data = data.split(" ")
	for i in range(arr_size):
		arr_data[i] = int(arr_data[i])
	print("ARRAY BEFORE SORTING : ",arr_data)
	arr_data = bubble_sort(arr_data)
	print("ARRAY AFTER SORTING : ",arr_data)
