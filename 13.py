x = 5
y = 2
if x > 0:
    if y > 0:
        print(f'Point P({x},{y}) is located in first quarter of coordinate system')
    elif y < 0:
        print(f'Point P({x},{y}) is located in fourth quarter of coordinate system')
    else:
        print(f'Point P({x},{y}) is located on the OX axis of coordinate system')
elif x < 0:
    if y > 0:
        print(f'Point P({x},{y}) is located in second quarter of coordinate system')
    elif y < 0:
        print(f'Point P({x},{y}) is located in third quarter of coordinate system')
    else:
        print(f'Point P({x},{y}) is located on the OX axis of coordinate system')
else:
    if y != 0:
        print(f'Point P({x},{y}) is located on the OY axis of coordinate system')
    else:
        print(f'Point P({x},{y}) is located at the point 0,0 of coordinate system')