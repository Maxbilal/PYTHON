s1  = (input("Enter the first sentence:").split())
s2  = (input("Enter the second sebtence:").split())
s3  = (input("Enter the third sebtence:").split())


common_words = set(s1) & set(s2) & set(s3)

print("Common words:", common_words)
