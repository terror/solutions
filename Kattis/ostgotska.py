s = input().split()
print("dae ae ju traeligt va" if sum([1 for i in s if "ae" in i]) / len(s) >= .40 else "haer talar vi rikssvenska")
