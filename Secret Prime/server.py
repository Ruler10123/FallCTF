from Crypto.Util.number import getPrime, getRandomRange, bytes_to_long, long_to_bytes

FLAG = bytes_to_long(open("flag.txt", "rb").read())

def gen_key():
    p = 9942564401124784370817949981506109463550890467971163846364245914543686506095700362448364280259029479542280541985520857408286580088352541049846554629477137 # getPrime(512)
    print("p is", p)
    k = 9301568977067599595794917435536322072979096972667835027052777328667056134966201698148663065711079784539030845611119652110075758146440790725325026976284542 # getRandomRange(1, p)
    print("k is", k)
    return p, k

def encrypt(p, k, m):
    m = bytes_to_long(m)
    return long_to_bytes((m * k) % p)

if __name__ == "__main__":
    p, k = gen_key()
    
    print("""Welcome to the SecretPrime online encryption service!""")

    while True:
        print("""    1. Encrypt
    2. Get encrypted flag
              """)
        choice = input("> ")

        if choice == "1":
            m = input("Enter the message to encrypt: ")
            print(f"Encrypted message: {encrypt(p, k, m.encode()).hex()}")
        elif choice == "2":
            print(f"Encrypted flag: {encrypt(p, k, long_to_bytes(FLAG)).hex()}")
            break
        else:
            print("Invalid choice")