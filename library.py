from decimal import Decimal

def cm_to_inch(cm, round_result: bool = False):
    if round_result:
        result = cm / 2.54
        result = Decimal(result).quantize(Decimal('0.01'))
        return float(result)
    return cm / 2.54
# 1 inch = ~2.54 cm
# print(cm_to_inch(2.54, True))
# print(type(cm_to_inch(25, True)))
