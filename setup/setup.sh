### Run script in the ./setup directory ###

### Generate list of valid images ###
# python generate_split_list.py

### Directory to save the processed data ###
mkdir -p ../data/train/Type_1/ ../data/train/Type_2/ ../data/train/Type_3/
mkdir -p ../data/valid/Type_1/ ../data/valid/Type_2/ ../data/valid/Type_3/
mkdir -p ../data/test/unknown/

### Preprocess image and split into train and valid ###

