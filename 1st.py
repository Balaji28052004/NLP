import re
text = "The rain in Spain falls mainly on the plain."
match = re.search(r"\bSpain\b", text)
if match:
    print("Match found:", match.group())
else:
    print("No match found for 'Spain'")
matches = re.findall(r"\b\w+ain\b", text)
print("Words ending with 'ain':", matches)
phone_pattern = r"^\d{3}-\d{3}-\d{4}$"
2text = "My phone number is 123-456-7890."
match = re.search(phone_pattern, text)
if match:
    print("Phone number found:", match.group())
else:
    print("No phone number found")
new_text = re.sub(r"\bplain\b", "plateau", text)
print("Modified text:", new_text)
