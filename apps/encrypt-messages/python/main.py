import sys
from pathlib import Path

# Make the repository-level shared package available when running this file directly.
sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from shared.check_input import get_int_range

import caesar_cipher


def encrypt_message(message, shift):
  """Encrypts a given message using a Caesar cipher with a given shift value.
  Args:
    message (str): The message to be encrypted.
    shift (int): The number of positions to shift each letter in the message.
  Returns:
    str: The encrypted message."""
    
  # Create a CaesarCipher object with the given shift value
  cipher = caesar_cipher.CaesarCipher(shift)
  
  # Encrypt the message using the CaesarCipher object
  encrypted_message = cipher.encrypt(message)

  return encrypted_message


def main():
  """Prompts the user for a message and a shift value, then encrypts the message using a Caesar cipher and prints the result."""
  
  print("Welcome to the Message Encryptor.\nYou can encrypt your messages using a Caesar cipher.")
  
  # Get user input for message and shift value
  message = input("Enter the message you want to encrypt: ")
  shift = get_int_range("Enter the shift value (1-25): ", 1, 25)
  
  # Encrypt the message and print the result
  encrypted_message = encrypt_message(message, shift)
  print(f"\nYour encrypted message is: {encrypted_message}")
    
main()