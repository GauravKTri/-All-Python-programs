dt1={"i":"mai","you":"tum","this":"ye"}
print(dt1["you"])
dt1.update({"that":"vo"})
print(dt1)
dt2=dt1.copy()
del dt2["you"]
print(dt2)
print(dt1)