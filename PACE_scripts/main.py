import deeplabcut

yaml_path = "/storage/coda1/p-fnajafi3/0/ydhadwal3/PupilPerimeterTrack-Yuvraj-2024-08-28/config.yaml"
analysis_path = "/storage/coda1/p-fnajafi3/0/ydhadwal3/PupilPerimeterTrack-Yuvraj-2024-08-28/videos"
output_folder = "/storage/coda1/p-fnajafi3/0/ydhadwal3/PupilPerimeterTrack-Yuvraj-2024-08-28/output"

# Creates a test/train split of 95/5 for training data to train model
# deeplabcut.create_training_dataset(yaml_path, augmenter_type='imgaug')

# Trains CNN model on training dataset
# deeplabcut.train_network(yaml_path, maxiters=500000, saveiters=50000, max_snapshots_to_keep=3)

# Evaluates CNN model based on test dataset
# deeplabcut.evaluate_network(yaml_path, plotting=True)

# Run the model on videos to get data
# deeplabcut.analyze_videos(yaml_path, [analysis_path], videotype='avi', destfolder=analysis_path, save_as_csv=True)

# Filter data to remove any outliers
deeplabcut.filterpredictions(yaml_path, [analysis_path], shuffle=1, trainingsetindex=0, filtertype='median', windowlength=5)

# Create a labelled video to see model points on video
deeplabcut.create_labeled_video(yaml_path, [analysis_path], filtered=True)
