import cipher

# CaesarCipher class is extended to inherit the attributes and methods of the cipher class
class CaesarCipher(cipher.Cipher):
  """Represents a Caesar Cipher.
  Attributes:
    shift (int): Representative of the shift value.
  """
  
  def __init__(self, shift):
    """Initializes the alphabet attribute from the cipher class and the shift attribute."""
    
    super().__init__()

    # raises an error if the shift value inputted by the user is not error
      # otherwise, the shift value is set
    if type(shift) is not int:
      raise TypeError("Enter an integer")
    else:
      self._shift = shift
  
  def _encrypt_letter(self, letter):
    """Iterates through each character within the alphabet to find the location of the corresponding letter and calculate the position of its encrypted counterpart and return the encrypted letter.
    Args:
      letter: Representative of an individual character from the message inputted by the user.
    """
    
    init_location = 0
    
    for char in self._alphabet:

      # increments the location by 1 until the program finds the letter value in the alphabet
      if char != letter:
        init_location += 1

      # calculates the position of the corresponding encoded letter
      else:
        encoded_let_loc = init_location + self._shift

        # finds the remainder from the encoded letter location and 26 if the location is > than 26
          #returns the resulting encrypted letter afterwards
        if encoded_let_loc >= len(self._alphabet):
          encoded_let_loc = encoded_let_loc % 26
          return self._alphabet[encoded_let_loc]

        # otherwise, the encoded letter location must be < 26 and returns the resulting encrypted letter as is
        else:
          return self._alphabet[encoded_let_loc]

      
  def _decrypt_letter(self,letter):
    """Iterates through each character within the alphabet to find the location of the corresponding letter      and calculate the position of its decrypted counterpart and return the decrypted letter.
    Args:
      letter: Representative of an individual character from the message inputted by the user.
    """
    
    init_location = 0
    
    for char in self._alphabet:

      # increments the location by 1 until the program finds the letter value in the alphabet
      if char != letter:
        init_location += 1  

      # calculates the position of the corresponding encoded letter
      else:
        encoded_let_loc = init_location - self._shift

        # finds the remainder from the encoded letter location and 26 if the location is > than 26
          #returns the resulting encrypted letter afterwards
        if encoded_let_loc > len(self._alphabet):
          encoded_let_loc = encoded_let_loc % 26
          return self._alphabet[encoded_let_loc]

        # otherwise, the encoded letter location must be < 26 and returns the resulting encrypted letter as is
        else:
          return self._alphabet[encoded_let_loc]

  def encrypt(self, message):
    """Encrypts a given message using a Caesar cipher with the shift value.
    Args:
      message: The message to be encrypted.
    Returns:
      str: The encrypted message."""
    
    encrypted_message = ""
    
    for letter in message:
      if letter in self._alphabet:
        encrypted_message += self._encrypt_letter(letter)
      else:
        encrypted_message += letter

    return encrypted_message
