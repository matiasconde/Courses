def P_EA_(p):
    return (0.005*p)/(p*0.005+(1-p)*0.995)

print(P_EA_(0.9997488068324542))

def desired_value(x):
    return 0.995/(1-0.005*x)

print(desired_value(0.95))