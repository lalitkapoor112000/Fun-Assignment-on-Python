def old_macdonald(st):
    st=st.title()
    st=st.replace(st[3],st[3].upper())
    return st

m=input("Enter a word:")
print(old_macdonald(m))
