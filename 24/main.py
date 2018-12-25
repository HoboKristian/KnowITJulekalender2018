txt = "GODJULOGGODTNYTTÅR"
txt = txt.replace("Æ", "[")
txt = txt.replace("Ø", "\\")
txt = txt.replace("Å", "]")

print(sum([(ord(t) - 64) * 29 ** (len(txt) - i - 1) for i,t in enumerate(txt)]))
