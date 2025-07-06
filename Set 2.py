#This is an amendment as I had only uploaded the notebook previously

'''Programming Set 2

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def shift_letter(letter, shift):
    if letter == ' ':
        return ' '
    letter_index = ord(letter) - ord('A')
    shifted_index = (letter_index + shift) % 26
    return chr(shifted_index + ord('A'))
def caesar_cipher(message, shift):
    '''Caesar Cipher.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def caesar_cipher(message, shift):
    def shift_letter(letter, shift):
        if letter == ' ':
            return ' '
        return chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
    shifted_message = ''
    for char in message:
        shifted_message += shift_letter(char, shift)
    return shifted_message
def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def shift_by_letter(letter, letter_shift):
        if letter == " ":
            return " "
        if letter_shift == " ":
            return " "
    shift = ord(letter_shift) - ord('A')
    return chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
def vigenere_cipher(message, key):
    '''Vigenere Cipher.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the key is extended to match the length of the message.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
 def vigenere_cipher(message, key):
    lettertonumber = {
        ' ': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
        'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
        'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
        'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
        'Z': 26
    }

    lettershifttonumber = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
        'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
        'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
        'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
        'Z': 25
    }

    numbertoletter = {
        1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G',
        8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M',
        14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S',
        20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',
        26: 'Z'
    }
    if len(key) < len(message):
        times = len(message) // len(key)
        remainder = len(message) % len(key)
        extended_key = key * times + key[:remainder] if remainder > 0 else key * times
    else:
        extended_key = key
    shifted_message = ''
    index_counter = 0
    for char in message:
        if char != ' ':
            msg_value = lettertonumber[char]
            shift_letter = extended_key[index_counter]
            shift_value = lettershifttonumber[shift_letter]
            combined_value = msg_value + shift_value
            if combined_value > 26:
                combined_value = combined_value % 26
                if combined_value == 0:
                    combined_value = 26  
            shifted_letter = numbertoletter[combined_value]
            shifted_message += shifted_letter
        else:
            shifted_message += ' '
        index_counter += 1
    return shifted_message
def scytale_cipher(message, shift):
    '''Scytale Cipher.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def scytale_cipher(message, shift):
        message_length = len(message)
    remainder = message_length % shift
    if remainder == 0:
        padded_message = message
    else:
        padding_needed = shift - remainder
        padding_string = "_" * padding_needed
        padded_message = message + padding_string
    total_characters = len(padded_message)
    columns = total_characters // shift
    encoded_message = ""
    for i in range(total_characters):
        original_index = (i // shift) + columns * (i % shift)
        current_char = padded_message[original_index]
        encoded_message += current_char
    return encoded_message
def scytale_decipher(message, shift):
    '''Scytale De-cipher.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def scytale_decipher(message, shift):
        total_chars = len(message)
        columns = total_chars // shift 
        decoded_message = ""
    for i in range(total_chars):
        row = i % columns
        col = i // columns
        original_index = row * shift + col
        decoded_message += message[original_index]
    return decoded_message