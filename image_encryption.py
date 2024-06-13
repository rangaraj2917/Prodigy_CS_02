import numpy as np
import cv2
from matplotlib import pyplot as plt

# Function to encrypt the image using pixel swapping
def encrypt_image(image, key):
    encrypted_image = image.copy()
    height, width, channels = image.shape
    flat_image = image.reshape(-1, channels)
    
    # Swap pixels according to the key
    encrypted_image_flat = flat_image[key]
    
    # Reshape back to the original image dimensions
    encrypted_image = encrypted_image_flat.reshape(height, width, channels)
    return encrypted_image

# Function to decrypt the image using pixel swapping
def decrypt_image(encrypted_image, key):
    decrypted_image = encrypted_image.copy()
    height, width, channels = encrypted_image.shape
    flat_encrypted_image = encrypted_image.reshape(-1, channels)
    
    # Create an inverse key for decryption
    inverse_key = np.argsort(key)
    
    # Swap pixels according to the inverse key
    decrypted_image_flat = flat_encrypted_image[inverse_key]
    
    # Reshape back to the original image dimensions
    decrypted_image = decrypted_image_flat.reshape(height, width, channels)
    return decrypted_image

# Load the image
image_path = '/home/attacker/Desktop/image.png'
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print(f"Error: Unable to load image at {image_path}. Please check the file path and try again.")
else:
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Generate a random key for pixel swapping
    height, width, channels = image.shape
    num_pixels = height * width
    key = np.random.permutation(num_pixels)

    # Encrypt the image
    encrypted_image = encrypt_image(image, key)

    # Decrypt the image
    decrypted_image = decrypt_image(encrypted_image, key)

    # Display the images
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.title('Original Image')
    plt.imshow(image)
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title('Encrypted Image')
    plt.imshow(encrypted_image)
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title('Decrypted Image')
    plt.imshow(decrypted_image)
    plt.axis('off')

    plt.show()
