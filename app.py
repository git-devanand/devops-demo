print("Hello DevOps!")

def login():
    return "Login feature implemented"

print(login())

def health_check():
    return {
        "status": "healthy"
    }


if __name__ == "__main__":
    print(health_check())
    print("Version 1.0")