import math


def sales_prediction():
    x= float(input())
    sales_pred= x*1.19
    print(sales_pred)   

def yard_to_meter():
    yard=float (input())
    m= yard*0.914
    mm=m*1000
    km=m/1000
    print(mm)
    print(m)
    print(km)



def cashier():
    price1=float(input())
    price2=float(input())
    price3=float(input())
    price4=float(input())
    price5=float(input())
    summary= price1+price2+price3+price4+price5
    pdv=summary*0.14
    before_pdv=summary*0.86
    print(summary)
    print(pdv)
    print(before_pdv)


def odometer():
    import math
    vzero=float(input())
    a=float(input())
    t_w_a=float(input())
    t_w_o_a=float(input())
    s_w_o_a=vzero*t_w_o_a
    v= vzero+(a*t_w_o_a)
    s_w_a= math.fabs (v*t_w_a+((a*((t_w_a)**2))/2))
    print(s_w_a)
    print(s_w_o_a)


def payment_instalments():
    sum=float(input())
    howmanypayments=float(input())
    sum_plus_fees=sum*1.05
    onepayment=sum_plus_fees/howmanypayments
    print(sum_plus_fees)
    print(onepayment)


def miles_per_galon():
    miles_driven=float(input())
    gallons_used=float(input())
    mpg=miles_driven/gallons_used
    print(mpg)


def cookie():
    how_many_cookies=float(input())
    how_much_sugar=how_many_cookies*.03125
    how_much_butter=how_many_cookies*(1/48)
    how_much_flour=how_many_cookies*(2.75/48)
    print(how_much_sugar)
    print(how_much_butter)
    print(how_much_flour)


def vineyard():
    r=float(input())
    e=float(input())
    s=float(input())
    v=int((r-2*e)/s)
    print(v)


def compound_interest():
    p=float(input())
    r=float(input())
    n=float(input())
    t=float(input())
    r_divby100=r/100
    a=p*(1+(r_divby100/n))**(n*t)
    print(a)



if __name__ == "__main__":
    eval(input() + "()")