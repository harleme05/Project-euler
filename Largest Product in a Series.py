num = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
""".strip().replace("\n", "")


list_of_chunks = []
for i in range(len(num)-13):
    chunk = num[i:(i+13)]
    if "0" in chunk:
        continue
    list_of_chunks.append(chunk)

for chunk in list_of_chunks:
    best = 0
    for i in chunk:
        sum = int(i)*sum
    if sum > best:
        best = sum
        
print(best)




        