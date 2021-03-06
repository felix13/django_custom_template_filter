from django import template


register = template.Library()

def human_format(num):
    decimal_format  = '{:.2f}'
    int_num = int(num)
    if int_num > 999 and int_num < 1000000:
        return decimal_format.format(int_num/1000.0).rstrip('0').rstrip('.') + 'K' 
    elif int_num > 999999:
        return decimal_format.format(int_num/1000000.0).rstrip('0').rstrip('.') + 'M'
    elif int_num < 1000:
        return str(int_num)

register.filter('human_format',  human_format )
