

VAT_NORMAL = 0.081
VAT_REDUCED  = 0.026
VAT_NONE = 0.0

def calculate_total(price, quantity):
    return price * quantity

def calculate_vat(price, vat_rate):
    net_price = price / (1 + vat_rate)
    return price - net_price