# розв'язання задачі в Codewars :Долари та центи
def format_amount(amount):
    formatted_amount = "${:.2f}".format(amount)
    return formatted_amount

amount = 39.99
formatted = format_amount(amount)
print(formatted)  
