def simplify_path(path: str) -> str:
    # Step 1: Split by '/' and filter out empty strings caused by '//'
    # This immediately handles the "multiple consecutive slashes" rule.
    parts = path.split("/")
    stack = []

    for part in parts:
        # Rule: '.' means current directory, do nothing.
        # Rule: '' happens with multiple slashes or trailing slashes, ignore.
        if part == "." or part == "":
            continue
        
        # Rule: '..' means go to parent directory.
        elif part == "..":
            if stack:
                stack.pop()
        
        # Rule: Any other sequence (including '...') is a valid name.
        else:
            stack.append(part)

    # Final Step: Reconstruct with single slashes and leading slash.
    # Handles "must not end with a slash unless it is root" automatically.
    return "/" + "/".join(stack)

# --- User Input Handling ---
if __name__ == "__main__":
    user_path = input("Enter the absolute Unix path: ").strip()
    
    # Validation: Path must start with '/'
    if not user_path.startswith("/"):
        print("Invalid Input: Path must start with '/'")
    else:
        canonical_path = simplify_path(user_path)
        print(f"Simplified Canonical Path: {canonical_path}")