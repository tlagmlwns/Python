d = {"번호":10, "성명":"코난","나ㅇㅣ":23, "사는곳":"사울"}
print(d)

print(type(d))
print(d["나ㅇㅣ"])

d["직업"] = "탐정"
print(d)

print(d.keys())
print(d.values())
print("사는곳"in d)
del d["사는곳"]
print("사는곳"in d)

print(d)