d = {"sora":7, "sim":0.2e-4}
print('ccc{sora},{sim}'.format(**d))
print(",", **{'sep' : "", "end":"0"})
print(",")

def funk(at, fat, mist):
    print(at, fat, mist)

def tag(tag_name, **attributes):
    attribute_list = [
        f'{name}="{value}"'
        for name, value in attributes.items()
    ]
    return f"<{tag_name} {' '.join(attribute_list)}>"

print(tag(tag_name="sss", soma = 3, tolik =2, bulka = 'b'))