from PIL import Image
import matplotlib.pyplot as plt
image = Image.open("inputt.jpg")
gray = image.convert("L")

width, height = gray.size
total_pixels = width * height
histogram = [0] * 256

for y in range(height):
    for x in range(width):
        pixel = gray.getpixel((x, y))
        histogram[pixel] += 1

pdf = []
for i in range(256):
    pdf.append(histogram[i] / total_pixels)
cdf = []
total = 0

for i in range(256):
    total = total + pdf[i]
    cdf.append(total)

cdf_min = 1

for value in cdf:
    if value > 0:
        cdf_min = value
        break
mapping = [0] * 256

for i in range(256):
    mapping[i] = round(
        ((cdf[i] - cdf_min) / (1 - cdf_min)) * 255
    )
equalized = Image.new("L", (width, height))

for y in range(height):
    for x in range(width):
        old_pixel = gray.getpixel((x, y))
        new_pixel = mapping[old_pixel]

        equalized.putpixel((x, y), new_pixel)


equalized_histogram = [0] * 256

for y in range(height):
    for x in range(width):
        pixel = equalized.getpixel((x, y))
        equalized_histogram[pixel] += 1


gray.save("gray_image.jpg")
equalized.save("equalized_image.jpg")


plt.figure(figsize=(12, 8))


plt.subplot(2, 3, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")


plt.subplot(2, 3, 2)
plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")


plt.subplot(2, 3, 3)
plt.plot(histogram)
plt.title("Original Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")


plt.subplot(2, 3, 4)
plt.plot(pdf)
plt.title("PDF")
plt.xlabel("Intensity")
plt.ylabel("Probability")


plt.subplot(2, 3, 5)
plt.imshow(equalized, cmap="gray")
plt.title("Equalized Image")
plt.axis("off")


plt.subplot(2, 3, 6)
plt.plot(equalized_histogram)
plt.title("Equalized Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")


plt.tight_layout()
plt.show()


print("Program completed successfully.")