text = "X-DSPAM-Confidence:    0.8475"
position = text.find('0')
print(float(text[position:]))
