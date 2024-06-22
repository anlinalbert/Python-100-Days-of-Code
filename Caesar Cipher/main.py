from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    """Function used to ciper or dipher text input."""
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
        
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
            
        else:
            end_text += char
    
    print(f"Here's the {cipher_direction}d result: {end_text}")

# Print logo.
print(logo)

shouldContinue = True

while(shouldContinue):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
  text = input("Type your message: ").lower()
  shift = int(input("Type the shift number: "))
  
  # If user enters a value greater than 26. This will be a problem because we have only 26 alphabets.
  shift = shift % 26
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  result = input("Type 'Yes' if you want to go again. Otherwise type 'No': ")
  if result == "no":
    shouldContinue = False