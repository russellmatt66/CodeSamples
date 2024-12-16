import sys

# This can be used for yearly, monthly, or daily compounding
# Yearly -> pass in ror = yar
# Monthly -> pass in ror = mar = yar / 12, base is monthly addition
def P(n: int, base: float, ror: float) -> float:
    if n == 1:
        return base * ror
    return (P(n-1, base, ror) + base) * ror

if __name__ == "__main__":
    num_years = int(sys.argv[1])
    base = float(sys.argv[2])
    yar = float(sys.argv[3]) # 1.1 = 10% yar
    value_yearly = P(num_years, base, yar)
    print("Principal after {} years with yearly compounding is: {}".format(num_years, value_yearly))

    num_months = 12 * num_years
    mar = 1.0 + (yar - 1.0) / 12 
    base_month = base / 12
    value_monthly = P(num_months, base_month, mar)
    print("Principal after {} months with monthly compounding: {}".format(num_months, value_monthly))

    num_days = 365 * num_years
    dar = 1.0 + (yar - 1.0) / 365
    base_daily = base / 365
    value_daily = P(num_days, base_daily, dar)
    print("Principal after {} days with daily compounding: {}".format(num_days, value_daily))
