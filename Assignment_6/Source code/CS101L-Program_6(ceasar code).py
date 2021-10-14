
import string 

def Encrypt(string_text, int_key): 
    '''Caesar-encrypts string using specified key.''' 
    new_list = []
    for x in string_text:
      if x == ' ':
        new_list.append(' ')
      else:
        new_list.append(chr((ord(x) + int_key - 65) % 26 + 65))

    return ''.join(new_list)

def Decrypt(string_text, int_key): 
  ''' Decrypts Caesar-encrypted string with specified key. ''' 
  new_list = []
  for x in string_text:
    if x == ' ':
      new_list.append(' ')
    else:
      new_list.append(chr((ord(x) - int_key - 65) % 26 + 65))

  return ''.join(new_list)
 
def Get_input(): 
  '''Interacts with user. Returns one of: '1', '2', '3', '4'.'''

  while True:
    try:
      user_input = input('Enter your selection ==>')
      if user_input == '1':
        return user_input
      elif user_input == '2':
        return user_input
      elif user_input.upper() == 'Q':
        return user_input
      else:
        raise ValueError
    except ValueError:
      print('Please enter valid value')
 

def Print_menu():
  '''Prints menu. No user interaction. '''
  print('1) Encode a string\n'
        '2) Decode a string\n'
        'Q) Quit')
  
  
def main(): 
  Again = True 
  while Again: 
    Print_menu()
    Choice = Get_input() 
    if Choice == '1': 
      print()
      Plaintext = input("Enter (brief) text to encrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Ciphertext = Encrypt(Plaintext, Key)
      print("Encrypted:", Ciphertext) 
      print()
    elif Choice == '2': 
      print()
      Ciphertext = input("Enter (brief) text to decrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Plaintext = Decrypt(Ciphertext, Key)
      print("Decrypted:", Plaintext) 
      print()
    else: 
      print("Have an ordinary day.") 
      Again = False 
      
      
# our entire program: 
main() 
