
class Cipher:
  """Represents a cipher.
  Attributes:
    alphabet(list) - An alphabetical list.
  """
  
  def __init__(self):
    """Initializes an alphabet list"""

    self._alphabet = [
      chr(i) for i in 
      range(ord('a'), ord('z') + 1)
     ]
    
    self._alphabet += [
      chr(i) for i in 
      range(ord('A'), ord('Z') + 1)
     ]
    
  def encrypt_message(self, message):
    """Encrypts the message inputted by the user using Atbash Cipher.
    Args:
      message: Representative of the string inputted by the user that is to be encrypted.
    """

    encrypt_str = ""
    message_upper = str(message.upper())

    # encrypts every alphabetical character in the upper-cased version of the user's message 
      # and adds it to a string
    for char in message_upper:
      if char.isalpha():
        encrypted_letter = self._encrypt_letter(char)
        encrypt_str += encrypted_letter
      else:
        encrypt_str += char

    # returns the encrypted-version of the original message afterwards
    return encrypt_str

    
  def decrypt_message(self, message):
    """Decrypts the message inputted by the user using Atbash Cipher.
    Args:
      message: Representative of the string inputted by the user that is to be decrypted.
    """
    
    decrypt_str = ""
    message_upper = str.upper(message)

    # decrypts every alphabetical character in the upper-cased version of the user's message
      # and adds it (along with non-alphabetical characters) to a string
    for char in message_upper:
      if char.isalpha():
        decrypted_letter = self._decrypt_letter(char)
        decrypt_str += decrypted_letter
      else:
        decrypt_str += char
        
    # returns the decrypted-version of the original message afterwards
    return decrypt_str

    
  def _encrypt_letter(self, letter):
    '''Iterates through each character within the alphabet to find the location of corresponding letter and      calculate the position of its encrypted counterpart and return the encrypted letter.
    Args:
      letter: Representative of an individual character from the message inputted by the user.
    '''
    
    let_location = 0

    for char in self._alphabet:

      # increments the location by 1 until the program finds the letter value in the alphabet
      if char != letter:
        let_location += 1

      # calculates the position of the corresponding letter and returns the resulting encrypted letter
      else:
        encoded_let_loc = 25 - let_location
        return self._alphabet[encoded_let_loc]
        
    
  def _decrypt_letter(self, letter):
    """Iterates through each character within the alphabet to find the location of the corresponding letter      and calculate the position of its decrypted counterpart and return the decrypted letter.
    Args:
      letter: Representative of an individual character from the message inputted by the user.
    """
    
    let_location = 0

    for char in self._alphabet:

      # increments the location by 1 until the program finds the letter value in the alphabet
      if char != letter:
        let_location += 1
        
      # calculates the position of the corresponding letter and returns the resulting decrypted letter 
      else:
        decoded_let_loc = 25 - let_location
        return self._alphabet[decoded_let_loc]
        