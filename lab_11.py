# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin ="malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"


# Store the remaining sequence elements of human insulin in variables:

lsInsulin="malwmrllpllallalwgpdpaaa"

bInsulin="fvnqhlcgshlvealylvcgergffytpkt"

aInsulin="giveqcctsicslyqlenycn"

cInsulin="rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin= bInsulin+aInsulin

print("The sequence of human preproinsulin:")
print(preproInsulin)
print("The sequence of human insulin, chain a: " + aInsulin)