import numpy as np
 
# Example Input
with open("example.txt") as f:
    lines = [line.rstrip() for line in f]

# # Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

key = [1 if i == "#" else 0 for i in lines[0]]

image = []

for idx, line in enumerate(lines):
    if idx < 2:
        continue
    image.append([1 if i == "#" else 0 for i in line])
image = np.array(image)


for round in range(2):
    print(f"ROUND {round}")
    if key[0] == 1:
        image = np.pad(image, 2, mode="constant", constant_values=(round%2))
    else:
        image = np.pad(image, 2, mode="constant", constant_values=0)
    new_image = []

    for i, r in enumerate(image):
        tmp = []
        if i == len(image)-2:
            break
        for j, c in enumerate(r):
            if j == len(image[0])-2:
                break
            img_slice = image[i:i+3, j:j+3]
            binary = ''.join(map(str, img_slice.flatten()))

            # print(img_slice)
            decimal = int(binary, 2)
            tmp.append(key[decimal])

        new_image.append(tmp)

    image = np.array(new_image)

print(len(image[image == 1]))