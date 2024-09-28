def reverse_sentence(s:str)-> str:
    l=s.split()
    l=l[::-1]
    r=" ".join(l)
    return r

input=" a good    example  "
output=reverse_sentence(input)
print(f"Input: {input}\nOutput: {output}")
    