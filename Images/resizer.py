from PIL import Image  # Import Pillow for image processing

def resize_image(image_path, scale_factor):
    """
    Resizes an image by a given scale factor.

    :param image_path: Path to the input image.
    :param scale_factor: Factor by which to scale the image (e.g., 0.5 for 50% size).
    :return: Path to the resized image.
    """
    try:
        # Open the image
        image = Image.open(image_path)

        # Calculate new dimensions
        new_width = int(image.width * scale_factor)
        new_height = int(image.height * scale_factor)

        # Resize the image
        resized_image = image.resize((new_width, new_height))

        # Save the resized image
        resized_image_path = image_path  # Save it in the same folder
        resized_image.save(resized_image_path)

        print(f"Image resized successfully! Saved at: {resized_image_path}")
        return resized_image_path

    except FileNotFoundError:
        print("Error: Image file not found. Please check the file path.")

# Example usage: Resize the image by a factor of 0.5 (50% size)
image_path = "Images/DIRECT-BIAS.png"  # Replace with the actual image file path
scale_factor = 0.8  # Change this value to scale the image

resize_image(image_path, scale_factor)
