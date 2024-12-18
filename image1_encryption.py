from PIL import Image

# Function to encrypt the image by swapping the red and blue channels
def encrypt_image(input_path, output_path):
    # Open the image
    img = Image.open(input_path)
    pixels = img.load()  # Access the pixel data

    width, height = img.size

    # Loop through every pixel in the image
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            
            # Swapping red and blue channels for encryption
            encrypted_pixel = (b, g, r)
            pixels[i, j] = encrypted_pixel

    # Save the encrypted image
    img.save(output_path)
    print(f"Image encrypted successfully!")

# Function to decrypt the image by swapping the red and blue channels back
def decrypt_image(input_path, output_path):
    # Open the encrypted image
    img = Image.open(input_path)
    pixels = img.load()  # Access the pixel data

    width, height = img.size

    # Loop through every pixel in the image
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            
            # Swapping red and blue channels back for decryption
            decrypted_pixel = (b, g, r)
            pixels[i, j] = decrypted_pixel

    # Save the decrypted image
    img.save(output_path)
    print(f"Image decrypted successfully!")

# Image file paths
input_image = r"c:\Users\BUBBY\Downloads\image1.webp"
encrypted_image = r"c:\Users\BUBBY\Downloads\image2_encrypted.webp"
decrypted_image = r"c:\Users\BUBBY\Downloads\image2_decrypted.webp"

# Encrypt the image
encrypt_image(input_image, encrypted_image)

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image)