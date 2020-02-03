ones = ['','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['','eleven', 'twelve', 'thirteen', 'fourteen','fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['','ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
specials = ['hundred', 'and']

nums = ''

for i in range(1000):
    ten = int(str(i)[-2:])
    if(i > 99):
        nums += ones[i//100] + specials[0]
        if i%100 != 0:
            nums += specials[1]
    if(ten>10 and ten<20):
        nums += teens[i%10]
    else:
        nums += tens[ten//10] + ones[ten%10]

nums += 'onethousand'

print(len(nums))
