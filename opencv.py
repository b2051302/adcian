import cv2
import difflib


def CalcImageHash(FileName):
    image = cv2.imread(FileName)
    resized = cv2.resize(image, (8, 8), interpolation=cv2.INTER_AREA)
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    avg = gray_image.mean()
    ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0)
    hash = ""
    for x in range(8):
        for y in range(8):
            val = threshold_image[x, y]
            if val == 255:
                hash = hash + "1"
            else:
                hash = hash + "0"

    return hash
def CompareHash(hash1, hash2):
    l = len(hash1)
    i = 0
    count = 0
    while i < l:
        if hash1[i] != hash2[i]:
            count = count + 1
        i = i + 1
    return count

fname1 = input("Enter the first filename: ")
fname2 = input("Enter the second filename: ")
hash1 = CalcImageHash(fname1)
hash2 = CalcImageHash(fname2)

print(hash1)
print(hash2)
print(CompareHash(hash1, hash2))

if CompareHash(hash1, hash2) >= 0 and CompareHash(hash1, hash2) <= 13:
    print("Similar")
elif CompareHash(hash1, hash2) > 13 and CompareHash(hash1, hash2) <= 25:
    print("Quiet Similar")
else:
    print("Not Similar")