import os

# Set the path to the main folder
main_folder = "/Users/keanocollins/Desktop/Data Science/Images"

# Allowed image extensions (add more if needed)
image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"}

# Traverse the folder and subfolders
for root, _, files in os.walk(main_folder):
    for file in files:
        file_path = os.path.join(root, file)
        file_name, file_ext = os.path.splitext(file)

        # Check if the file has an image extension but no actual name
        if file_ext.lower() in image_extensions and not file_name:
            print(f"Removing: {file_path}")
            os.remove(file_path)  # Delete the file

print("✅ Cleanup complete!")
