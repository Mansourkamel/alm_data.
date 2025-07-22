from statistics import mean
import numpy as np
#from pip install Pillow import Image
#from PIL import Image
Array=[80,85,90,95,100,105,110,115,120,125,77,22,1,5,21,83,254,717]
even=[]
odd=[]
y=int(input("Enter num:"))
s=1
for i in Array:
    if i%2==0:
        even+=[i]
    else:
        odd+=[i]
print(":زوجي\t",even)
print(odd,":فردي\t")

for i in Array:
    if i ==y:
        s=y

print("هذا الرقم:","found") if s==y else print("هذا الرقم:","notfound")

print("--------------------------------------------------")

print(max(Array))
print(min(Array))
print(mean(Array))

print("--------------------------------------------------")
point1=[1, 2, 3]
point2 = [4, 5, 6]
distance = sum([(i-j)**2 for i,j in zip(point1, point2)])**0.5
print ("distance:", distance)


distance = np.linalg.norm(np.array(point1) - np.array(point2))
print ("distance:", distance)
print("--------------------------------------------------")


data = np.array([[1, 2, np.nan], [4, np.nan, 6]])
print("The Data Pre-cleaning:\n",data)
col_mean = np.nanmean(data, axis=0)
data[np.isnan(data)] =col_mean[np.isnan(data).nonzero()[1]]
print ("The Data Post-cleaning:\n" , data)
print("--------------------------------------------------")


x=np.array([6, 2, 3, 4])
y=np.array([2, 4,5, 4])

coefficients=np.polyfit(x,y,1)
print ("Coefficients (Slope, Intercept):", coefficients)

print("--------------------------------------------------")
#image=Image.open("مسار الصورة")
#image_array =np.array(image)