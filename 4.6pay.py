def computepay(h,r):
    if h<=40:
        return h*r
    else:
        oh=h-40
        op=r*1.5
        return 40*r+oh*op

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
p = computepay(h,r)
print("Pay",p)
