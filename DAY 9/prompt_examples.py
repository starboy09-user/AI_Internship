print("PROMPT ENGINEERING EXAMPLES")

print("\n1. ZERO-SHOT PROMPT")
zero_shot = """
Translate the following sentence into French:
Hello, how are you?
"""
print(zero_shot)

print("\n2. FEW-SHOT PROMPT")
few_shot = """
English: Hello
French: Bonjour

English: Thank You
French: Merci

English: Good Morning
French:
"""
print(few_shot)

print("\n3. MARKETING PROMPT")
marketing_prompt = """
Write a persuasive advertisement for a smartphone
under ₹15,000 with a 50MP camera and 5000mAh battery.
"""
print(marketing_prompt)