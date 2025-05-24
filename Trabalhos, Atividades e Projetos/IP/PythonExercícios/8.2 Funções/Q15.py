""" Write a function called reverseWords that given a string representing a
sentence, returns the same sentence but with each word reversed. For
instance, reverseWords(“hi there how are you”) would return “ih erehtwoh
era uoy”. """

def reverseWords(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(word[::-1] for word in words) #GPT // Lembrar de pedir explicação de como fazer
    return reversed_sentence

def main():
    sentence = input('Digite uma palavra ou frase: ')
    print(reverseWords(sentence))

main()