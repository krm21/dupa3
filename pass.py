import secrets
import string
import argparse


def generate_password(length=16, use_digits=True, use_symbols=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    while True:
        password = "".join(secrets.choice(chars) for _ in range(length))
        # Ensure at least one of each required character type
        has_letter = any(c in string.ascii_letters for c in password)
        has_digit = any(c in string.digits for c in password) if use_digits else True
        has_symbol = any(c in string.punctuation for c in password) if use_symbols else True
        if has_letter and has_digit and has_symbol:
            return password


def main():
    parser = argparse.ArgumentParser(description="Generate secure passwords")
    parser.add_argument("-l", "--length", type=int, default=16, help="Password length (default: 16)")
    parser.add_argument("-n", "--count", type=int, default=5, help="Number of passwords (default: 5)")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    args = parser.parse_args()

    print(f"\nGenerating {args.count} password(s) of length {args.length}:\n")
    for i in range(args.count):
        pw = generate_password(
            length=args.length,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols,
        )
        print(f"  {i + 1}. {pw}")
    print()


if __name__ == "__main__":
    main()
