def encrypt_array(arr, key):
    encrypted_arr = []
    for num in arr:
        encrypted_num = (num + key) % 256  # Assuming array elements are in the range 0-255
        encrypted_arr.append(encrypted_num)
    return encrypted_arr

def main():
    arr = [100, 150, 200, 50, 75]
    key = 5
    encrypted_arr = encrypt_array(arr, key)
    print("Original array:", arr)
    print("Encrypted array:", encrypted_arr)

if __name__ == "__main__":
    main()
