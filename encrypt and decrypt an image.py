#pixel manipulation for image encryption

from PIL import Image

def encrypt_image(image_path):
    img = Image.open(image_path)
    width, height = img.size

    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            new_pixel = (pixel[2], pixel[0], pixel[1])
            img.putpixel ((x, y), new_pixel)

    encrypted_path = image_path.split('.')[0] + '_encrypted.png'
    img.save(encrypted_path)
    print("Image encrypted successfully.")
    return encrypted_path

def decrypt_image(encrypted_image_path):
    img = Image.open(encrypted_image_path)
    width, height = img.size

    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            new_pixel = (pixel[1], pixel[2], pixel[0])
            img.putpixel((x, y), new_pixel)

    decrypted_path = encrypted_image_path.split('_encrypted')[0] + '_decrypted.png'
    img.save(decrypted_path)
    print("Image decrypted successafully.")
    return decrypted_path

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt an image? (e/d): ")
        if choice == "e":
            image_path = input("Enter the path of the image: ")
            encrypted_image_path = encrypt_image(image_path)
            print("Encrypted image saved as: ", encrypted_image_path)
        elif choice == "d":
            encrypted_image_path = input("Enter the path of the encrypted image: ")
            decrypted_image_path = decrypt_image(encrypted_image_path)
        else:
            print("Invalid choice! please enter valid choice.")
            continue
        
        cont = input("Do you want to continue? (y/n): ")
        if cont != "y":
            break

if __name__ == "__main__":
    main()
