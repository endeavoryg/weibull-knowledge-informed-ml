import numpy as np
from pathlib import Path
import os
import h5py


# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.utils import shuffle

# import custom functions and classes
from data_utils import (
    get_min_max,
    scaler,
    create_x_y,
    create_date_dict,
)

from src.features.build_features import build_spectrogram_df_femto


###################
# Create Data Set
###################

# set the root (parent folder) and the data folder locations
folder_root = Path.cwd().parent  # get root folder of repository

folder_raw_data = (
    folder_root / "data/raw/FEMTO/Training_set/Learning_set/"
)  # raw data folder

folder_raw_data_test = (
    folder_root / "data/raw/FEMTO/Test_set/Test_set/"
)  # raw data folder

# Constants
BUCKET_SIZE = 64 # the bin size - number of features
RANDOM_STATE = 694

def create_femto_dataset(folder_raw_data_train, folder_raw_data_test, folder_processed_data, bucket_size=64, random_state=694):
    """Create the PRONOSTIA (FEMTO) processed data, with appropriate train/val/test sets
    
    Parameters
    ===========
    folder_raw_data_train : pathlib object 
        Location of raw training data, likely in ./data/raw/FEMTO/Training_set/Learning_set/

    folder_raw_data_test : pathlib object 
        Location of raw test data, likely in ./data/raw/FEMTO/Test_set/Test_set/

    folder_processed_data : pathlib object
        Location to store processed data (.h5py files). Likely ./data/processed/FEMTO/

    bucket_size : int
        The number of data points (from FFT spectrum) to include in each bin, or bucket.
        For example, if we want 20 bins on the FEMTO data set, we should set the bucket
        size to 64. The average, or max value, is taken from each bucket to make the 
        final vector of size 20 for each time step (vector of 20 fed into neural network)

    random_state : int
        Number to reproduce the data split

    Returns
    ===========
    A bunch of .h5py files, in the folder_processed_data, for each of the respective
    train/validation/testing sets.

    """
    
    #!#!#!# TRAIN #!#!#!#
    # Bearing1_1
    folder_indv_bearing = folder_raw_data_train / "Bearing1_1"
    date_dict = create_date_dict(folder_indv_bearing)
    df_spec, labels_dict = build_spectrogram_df_femto(
        folder_indv_bearing, date_dict, channel_name="acc_horz",
    )

    # create temp x, y
    x1_1, y1_1 = create_x_y(
        df_spec, labels_dict, bucket_size, print_shape=False
    )
    x_train = x1_1
    y_train = y1_1

    print("x_train.shape:", x_train.shape)

    ####
    # Bearing2_1
    folder_indv_bearing = folder_raw_data_train / "Bearing2_1"
    date_dict = create_date_dict(folder_indv_bearing)
    df_spec, labels_dict = build_spectrogram_df_femto(
        folder_indv_bearing, date_dict, channel_name="acc_horz",
    )

    # create temp x, y
    x2_1, y2_1 = create_x_y(
        df_spec, labels_dict, bucket_size, print_shape=False
    )
    x_train = np.append(x_train, x2_1, 0)
    y_train = np.append(y_train, y2_1, 0)

    print("x_train.shape:", x_train.shape)

    ####
    # Bearing3_1
    folder_indv_bearing = folder_raw_data_train / "Bearing3_1"
    date_dict = create_date_dict(folder_indv_bearing)
    df_spec, labels_dict = build_spectrogram_df_femto(
        folder_indv_bearing, date_dict, channel_name="acc_horz",
    )

    # create temp x, y
    x3_1, y3_1 = create_x_y(
        df_spec, labels_dict, bucket_size, print_shape=False
    )
    x_train = np.append(x_train, x3_1, 0)
    y_train = np.append(y_train, y3_1, 0)

    print("x_train.shape:", x_train.shape)


    ##############################################################
    #!#!#!# VAL #!#!#!#
    # Bearing1_2
    folder_indv_bearing = folder_raw_data_train / "Bearing1_2"
    date_dict = create_date_dict(folder_indv_bearing)
    df_spec, labels_dict = build_spectrogram_df_femto(
        folder_indv_bearing, date_dict, channel_name="acc_horz",
    )

    # create temp x, y
    x1_2, y1_2 = create_x_y(
        df_spec, labels_dict, bucket_size, print_shape=False
    )
    x_val = x1_2
    y_val = y1_2

    print("x_val.shape:", x_val.shape)

    ####
    # Bearing2_2
    folder_indv_bearing = folder_raw_data_train / "Bearing2_2"
    date_dict = create_date_dict(folder_indv_bearing)
    df_spec, labels_dict = build_spectrogram_df_femto(
        folder_indv_bearing, date_dict, channel_name="acc_horz",
    )

    # create temp x, y
    x2_2, y2_2 = create_x_y(
        df_spec, labels_dict, bucket_size, print_shape=False
    )
    x_val = np.append(x_val, x2_2, 0)
    y_val = np.append(y_val, y2_2, 0)

    print("x_val.shape:", x_val.shape)

    ####
    # Bearing3_2
    folder_indv_bearing = folder_raw_data_train / "Bearing3_2"
    date_dict = create_date_dict(folder_indv_bearing)
    df_spec, labels_dict = build_spectrogram_df_femto(
        folder_indv_bearing, date_dict, channel_name="acc_horz",
    )

    # create temp x, y
    x3_2, y3_2 = create_x_y(
        df_spec, labels_dict, bucket_size, print_shape=False
    )
    x_val = np.append(x_val, x3_2, 0)
    y_val = np.append(y_val, y3_2, 0)

    print("x_val.shape:", x_val.shape)


    ##############################################################
    #!#!#!# TEST #!#!#!#
    # Bearing1_3
    folder_indv_bearing = folder_raw_data_test / "Bearing1_3"
    date_dict = create_date_dict(folder_indv_bearing)
    df_spec, labels_dict = build_spectrogram_df_femto(
        folder_indv_bearing, date_dict, channel_name="acc_horz",
    )

    # create temp x, y
    x1_3, y1_3 = create_x_y(
        df_spec, labels_dict, bucket_size, print_shape=False
    )
    x_test = x1_3
    y_test = y1_3

    print("x_test.shape:", x_test.shape)

    ####
    # Bearing2_3
    folder_indv_bearing = folder_raw_data_test / "Bearing2_3"
    date_dict = create_date_dict(folder_indv_bearing)
    df_spec, labels_dict = build_spectrogram_df_femto(
        folder_indv_bearing, date_dict, channel_name="acc_horz",
    )

    # create temp x, y
    x2_3, y2_3 = create_x_y(
        df_spec, labels_dict, bucket_size, print_shape=False
    )
    x_test = np.append(x_test, x2_3, 0)
    y_test = np.append(y_test, y2_3, 0)

    print("x_test.shape:", x_test.shape)

    ####
    # Bearing3_3
    folder_indv_bearing = folder_raw_data_test / "Bearing3_3"
    date_dict = create_date_dict(folder_indv_bearing)
    df_spec, labels_dict = build_spectrogram_df_femto(
        folder_indv_bearing, date_dict, channel_name="acc_horz",
    )

    # create temp x, y
    x3_3, y3_3 = create_x_y(
        df_spec, labels_dict, bucket_size, print_shape=False
    )
    x_test = np.append(x_test, x3_3, 0)
    y_test = np.append(y_test, y3_3, 0)

    print("x_test.shape:", x_test.shape)


    ##############################################################
    #### Weibull ####

    t1_1 = np.max(y1_1[:, 0])  # get the run-time in days
    t2_1 = np.max(y2_1[:, 0])
    t3_1 = np.max(y3_1[:, 0])

    # bold printout https://stackoverflow.com/a/17303428/9214620
    print(
        f"\033[1mt1_1\033[0m run-time: {t1_1:.3f} days \n\033[1mt2_1\033[0m run-time: {t2_1:.3f} days \n\033[1mt3_1\033[0m run-time: {t3_1:.3f} days"
    )

    # calculate the weibull properties
    beta = 2.0 # shape parameter
    t_array = np.array([t1_1, t2_1, t3_1]) # build a time array of t
    r = 3 # number of failed units

    # characteristic life
    eta = (np.sum((t_array ** beta) / r)) ** (1 / beta)
    eta_beta_r = np.array([eta, beta, r])

    print('eta:', eta)


    ##############################################################
    #######
    # Create x, y train/val/test
    #######

    # shuffle
    x_train, y_train = shuffle(x_train, y_train, random_state)
    x_val, y_val = shuffle(x_val, y_val, random_state)

    # scale
    min_val, max_val = get_min_max(x_train)
    x_train = scaler(x_train, min_val, max_val)
    x_val = scaler(x_val, min_val, max_val)

    # create individual data sets for each run
    # so that we can easily trend the results
    x_train1_1 = scaler(x1_1, min_val, max_val) 
    y_train1_1 = y1_1

    x_train2_1 = scaler(x2_1, min_val, max_val) 
    y_train2_1 = y2_1

    x_train3_1 = scaler(x3_1, min_val, max_val) 
    y_train3_1 = y3_1

    x_val1_2 = scaler(x1_2, min_val, max_val) 
    y_val1_2 = y1_2

    x_val2_2 = scaler(x2_2, min_val, max_val) 
    y_val2_2 = y2_2

    x_val3_2 = scaler(x3_2, min_val, max_val) 
    y_val3_2 = y3_2

    x_test1_3 = scaler(x1_3, min_val, max_val) 
    y_test1_3 = y1_3

    x_test2_3 = scaler(x2_3, min_val, max_val) 
    y_test2_3 = y2_3

    x_test3_3 = scaler(x3_3, min_val, max_val) 
    y_test3_3 = y3_3


    ####
    # save as h5py files
    with h5py.File("x_train.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "x_train", data=x_train)
    with h5py.File("y_train.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "y_train", data=y_train)

    with h5py.File("x_val.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "x_val", data=x_val)
    with h5py.File("y_val.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "y_val", data=y_val)

    with h5py.File("x_test.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "x_test", data=x_test)
    with h5py.File("y_test.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "y_test", data=y_test)

    # save eta/beta
    with h5py.File("eta_beta_r.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "eta_beta_r", data=eta_beta_r)

    # save t_array
    with h5py.File("t_array.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "t_array", data=t_array)

    # Bearing1_1
    with h5py.File("x_train1_1.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "x_train1_1", data=x_train1_1)
    with h5py.File("y_train1_1.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "y_train1_1", data=y_train1_1)

    # Bearing2_1
    with h5py.File("x_train2_1.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "x_train2_1", data=x_train2_1)
    with h5py.File("y_train2_1.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "y_train2_1", data=y_train2_1)

    # Bearing3_1
    with h5py.File("x_train3_1.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "x_train3_1", data=x_train3_1)
    with h5py.File("y_train3_1.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "y_train3_1", data=y_train3_1)

    # Bearing1_2
    with h5py.File("x_val1_2.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "x_val1_2", data=x_val1_2)
    with h5py.File("y_val1_2.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "y_val1_2", data=y_val1_2)

    # Bearing2_2
    with h5py.File("x_val2_2.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "x_val2_2", data=x_val2_2)
    with h5py.File("y_val2_2.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "y_val2_2", data=y_val2_2)

    # Bearing3_2
    with h5py.File("x_val3_2.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "x_val3_2", data=x_val3_2)
    with h5py.File("y_val3_2.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "y_val3_2", data=y_val3_2)

    # Bearing1_3
    with h5py.File("x_test1_3.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "x_test1_3", data=x_test1_3)
    with h5py.File("y_test1_3.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "y_test1_3", data=y_test1_3)

    # Bearing2_3
    with h5py.File("x_test2_3.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "x_test2_3", data=x_test2_3)
    with h5py.File("y_test2_3.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "y_test2_3", data=y_test2_3)

    # Bearing3_3
    with h5py.File("x_test3_3.hdf5", "w") as f:
        dset = f.create_dataset("x_test3_3", data=x_test3_3)
    with h5py.File(folder_processed_data / "y_test3_3.hdf5", "w") as f:
        dset = f.create_dataset(folder_processed_data / "y_test3_3", data=y_test3_3)


