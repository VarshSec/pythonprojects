def check_password_strength(password):
    score = 0

    # Rules for checking
    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|" for c in password):
        score += 
  
    if score <= 2:
        return "❌ Weak: Easy to guess. Add more length, numbers, and symbols."
    elif score in (3, 4):
        return "⚠️ Medium: Better, but still breakable. Try mixing upper/lower, numbers, and special characters."
    else:
        return "✅ Strong: Great job! Your password is tough to crack."
    

if __name__ == "__main__":
    print("🔐 Password Strength Checker")
    print("-" * 30)
    pwd = input("Enter your password: ")
    print("\nResult:", check_password_strength(pwd))
