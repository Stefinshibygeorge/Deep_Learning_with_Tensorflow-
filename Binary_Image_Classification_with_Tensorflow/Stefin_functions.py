

def unzip_and_extract(path):
    ''' Argument : path of a zip_file , as a string
    
        Takes a zip file path, extracts it to the current working directory of colab
        
        Returns   : void
    '''
    
    import zipfile

    zipped_file = zipfile.ZipFile(path)
    zipped_file.extractall()
    zipped_file.close()
    
    
def walk_through_dir(path):
    
    import os 

    for dir_path,dir_names,file_names in os.walk("pokemon_data"):
        print(f'There are {len(dir_names)} directories and {len(file_names)} images in {dir_path}')
    

def view_random_image(target_dir, target_class):
    '''
    traget_dir :  takes the path of the directory
    target_class : takes the name of the class needed. It should be a folder in the target_dir containing the images of the class
    '''
     
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import random
    import os
  # Setup the target directory (we'll view images from here)
    target_folder = target_dir + "/" + target_class

  # Get a random image path
    random_image = random.sample(os.listdir(target_folder), 1)
  #print(random_image)

  # Read in the image and plot it using matplotlib
    img = mpimg.imread(target_folder + "/" + random_image[0])
    plt.imshow(img)
    plt.title(target_class)
    plt.axis("off");

    print(f"Image shape: {img.shape}") # show the shape of the image
    
    return img
  
def create_tensorboard_callback(dir_name, experiment_name):
  import tensorflow as tf
  import datetime
  """
  Creates a TensorBoard callback instand to store log files.

  Stores log files with the filepath:
    "dir_name/experiment_name/current_datetime/"

  Args:
    dir_name: target directory to store TensorBoard log files
    experiment_name: name of experiment directory (e.g. efficientnet_model_1)
  """
  log_dir = dir_name + "/" + experiment_name + "/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
  tensorboard_callback = tf.keras.callbacks.TensorBoard(
      log_dir=log_dir
  )
  print(f"Saving TensorBoard log files to: {log_dir}")
  return tensorboard_callback




def select_random_file_from_directory(directory):
  '''
  Takes in a directory path and returns a random file inside it
  
  '''
  import os
  import random
  
  files = os.listdir(directory)
  
  if files:
    random_file = random.choice(files)
    print("Randomly selected file:", random_file)
  else:
    raise FileNotFoundError
    
  file = f"{directory}/{random_file}"
  
  return file
  
  
  
    