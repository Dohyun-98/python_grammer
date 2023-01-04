# O(N^3)을 O(N^2)로 바꿀시, 엄청난 성능향상이다.
def word_builder(list):
    collection = []

    for i in range(0,len(list)):
        for j in range(0,len(list)):
            if i != j:
                collection.append(list[i]+list[j])

    return collection

print(word_builder(["a","b","c","d"]))