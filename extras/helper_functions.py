# View an image 
def view_random_images(target_dir, target_class):

  # Import important libraries and classes
  import matplotlib.pyplot as plt
  import matplotlib.image as mpimg
  import random

  # Setup target directory (we will view images from here)
  target_folder = target_dir + target_class

  # Get a random image path
  random_images = random.sample(os.listdir(target_folder), 16)

  # Read in the images and plot them using matplolib
  fig, ((ax0, ax1, ax2, ax3),
      (ax4, ax5, ax6, ax7),
      (ax8, ax9, ax10, ax11),
      (ax12, ax13, ax14, ax15)) = plt.subplots(4, 4, figsize=(10, 10))

  fig.suptitle(target_class, fontsize=15)      

  img = mpimg.imread(target_folder + "/" + random_images[0])
  ax0.imshow(img)
  ax0.axis("off") 

  img = mpimg.imread(target_folder + "/" + random_images[1])
  ax1.imshow(img)
  ax1.axis("off") 

  img = mpimg.imread(target_folder + "/" + random_images[2])
  ax2.imshow(img)
  ax2.axis("off") 

  img = mpimg.imread(target_folder + "/" + random_images[3])
  ax3.imshow(img)
  ax3.axis("off") 

  img = mpimg.imread(target_folder + "/" + random_images[4])
  ax4.imshow(img)
  ax4.axis("off") 

  img = mpimg.imread(target_folder + "/" + random_images[5])
  ax5.imshow(img)
  ax5.axis("off")

  img = mpimg.imread(target_folder + "/" + random_images[6])
  ax6.imshow(img)
  ax6.axis("off") 

  img = mpimg.imread(target_folder + "/" + random_images[7])
  ax7.imshow(img)
  ax7.axis("off") 

  img = mpimg.imread(target_folder + "/" + random_images[8])
  ax8.imshow(img)
  ax8.axis("off") 

  img = mpimg.imread(target_folder + "/" + random_images[9])
  ax9.imshow(img)
  ax9.axis("off") 

  img = mpimg.imread(target_folder + "/" + random_images[10])
  ax10.imshow(img)
  ax10.axis("off")

  img = mpimg.imread(target_folder + "/" + random_images[11])
  ax11.imshow(img)
  ax11.axis("off")
 
  img = mpimg.imread(target_folder + "/" + random_images[12])
  ax12.imshow(img)
  ax12.axis("off")

  img = mpimg.imread(target_folder + "/" + random_images[13])
  ax13.imshow(img)
  ax13.axis("off")

  img = mpimg.imread(target_folder + "/" + random_images[14])
  ax14.imshow(img)
  ax14.axis("off")

  img = mpimg.imread(target_folder + "/" + random_images[15])
  ax15.imshow(img)
  ax15.axis("off")
  
  print(f"Image of {target_class} has a shape of {img.shape}")

  return img
