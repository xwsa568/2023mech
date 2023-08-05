# Import TF and TF Hub libraries.
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np

# Load the input image.
image_path = 'data/image1.jpeg'
image = tf.io.read_file(image_path)
image = tf.compat.v1.image.decode_jpeg(image)
image = tf.expand_dims(image, axis=0)
# Resize and pad the image to keep the aspect ratio and fit the expected size.
image = tf.cast(tf.image.resize_with_pad(image, 256, 256), dtype=tf.int32)

# Download the model from TF Hub.
model = hub.load("https://tfhub.dev/google/movenet/singlepose/thunder/4")
movenet = model.signatures['serving_default']

# Run model inference.
outputs = movenet(image)
# Output is a [1, 1, 17, 3] tensor.
keypoints = outputs['output_0']

# Define body part connections.
connections = [
    (5, 6),  # left shoulder to right shoulder
    (5, 7),  # left shoulder to left elbow
    (7, 9),  # left elbow to left wrist
    (6, 8),  # right shoulder to right elbow
    (8, 10),  # right elbow to right wrist
    (5, 11), # left shoulder to left hip
    (6, 12), # right shoulder to right hip 
    (11, 12),  # left hip to right hip
    (11, 13),  # left hip to left knee
    (13, 15),  # left knee to left ankle
    (12, 14),  # right hip to right knee
    (14, 16)  # right knee to right ankle
]

# Load the image using matplotlib.
image = tf.io.read_file(image_path)
image = tf.image.decode_jpeg(image)

# Create a figure and axis to plot the image.
fig, ax = plt.subplots()
ax.imshow(image)

# Convert the image to float.
image = tf.cast(image, dtype=tf.float32)

# Plot the keypoints on the image.
keypoints = keypoints[0, 0]  # Extract keypoints from the tensor
threshold = 0

for keypoint in keypoints:
    x, y, confidence = keypoint  # Extract x, y coordinates, and confidence
    if confidence > threshold:  # Adjust the threshold as needed
        x *= image.shape[0]  # Scale the x coordinate to image frame
        y *= image.shape[1]  # Scale the y coordinate to image frame
        plt.plot(y, x, 'r.', markersize=5)
    if np.array_equal(keypoint, keypoints[5]):  # Check for left shoulder
        left_shoulder = (y, x)
    elif np.array_equal(keypoint, keypoints[6]):  # Check for right shoulder
        right_shoulder = (y, x)

for connection in connections:
    part_a, part_b = connection
    x_a, y_a, _ = keypoints[part_a]
    x_b, y_b, _ = keypoints[part_b]
    if keypoints[part_a, 2] > threshold and keypoints[part_b, 2] > threshold:  # Adjust the threshold as needed
        x_a *= image.shape[0]
        y_a *= image.shape[1]
        x_b *= image.shape[0]
        y_b *= image.shape[1]
        plt.plot( [y_a, y_b], [x_a, x_b],'r-', linewidth=1)  # Plot connection as a red line


# Connect the left shoulder and right shoulder with a line.
if left_shoulder is not None and right_shoulder is not None:
    plt.plot([left_shoulder[0], right_shoulder[0]], [left_shoulder[1], right_shoulder[1]], 'g-', linewidth=2)

# Remove the axis labels and ticks.
ax.axis('off')

# Show the plotted image.
plt.show()
