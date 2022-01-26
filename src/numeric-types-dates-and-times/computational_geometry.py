""""Computational Geometry"""

"""Interesting behavior of True and False"""
# True == 1
# False == 0
print(True - False)  # 1
print(False - True)  # -1
print(False - False)  # 0


"""Sign function"""
# usual approach
def sign_usual(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    return 0

# True/False arithmetic approach
def sign(num):
    return (num > 0) - (num < 0)

print(sign(5))
print(sign(0))
print(sign(-5))
