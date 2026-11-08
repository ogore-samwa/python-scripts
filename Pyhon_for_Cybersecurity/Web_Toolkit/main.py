print("Hello, Cybersecurity!")

print("Targer: Portswigger Lab ")
print("Status: Testing")
print("Tool: Python")

target = input("Enter the target URL: ")
print(f"Target URL: {target}")

if target.startswith("https://"):
    print("HTTPS detected.")
elif target .startswith("http://"):
    print("HTTP detected.")
else:
    print("Invalid URL format. Please include 'http://' or 'https://'.")

