import re

def password_strength(password):
    # Criteria definitions
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    # Scoring
    score = 0
    if length_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_char_criteria:
        score += 1

    # Feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should contain at least one digit.")
    if not special_char_criteria:
        feedback.append("Password should contain at least one special character.")

    # Strength
    strength_levels = {1: "Very Weak", 2: "Weak", 3: "Moderate", 4: "Strong", 5: "Very Strong"}
    strength = strength_levels[score]

    return score, strength, feedback

# Example usage
password = input("Enter a password to evaluate: ")
score, strength, feedback = password_strength(password)

print(f"Password Score: {score}/5")
print(f"Password Strength: {strength}")
print("Feedback:")
for comment in feedback:
    print(f"- {comment}")
18