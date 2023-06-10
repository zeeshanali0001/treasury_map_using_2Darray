row1=["😑","😑", "😑","😑"]
row2=["😑","😑", "😑","😑"]
row3=["😑","😑", "😑","😑"]
row4=["😑","😑", "😑","😑"]
print(f"{row1}\n{row2}\n{row3}\n{row4}")

map=[row1,row2,row3,row4]
# Lists inside a list becomes nested list:(2D list is like a matrix)
# print(map[3-1])         # Here the map[2] will printout row2
# print(map[4-1][1-1])    # Here the map[3][0] will printout element at position 0 of row3

position = input("where do we want to put the treausre?(enter location of columns and row eg.cr/11/22...):")
#Subscripting/spliting up  the 2 digit input into 2 different parts/intigers
horizontal = int(position[0])
vertical = int(position[1])

selected_row=map[vertical-1]     #accessing the Vertical posiiton of matric: vertical represents the column
selected_row[horizontal-1]="x"   #accessing the horizonrtal postion of matrix : horizontal represents the row
print(f"{row1}\n{row2}\n{row3}\n{row4}")
