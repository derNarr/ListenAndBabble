#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

import ctypes
import os
import shutil

from create_sp_par import create_speaker    # for creating speakers (-> create_sp.py)


LIB_VTL = ctypes.cdll.LoadLibrary(os.path.abspath('VTL_API/VocalTractLabApi.so'))

# define working header
WAV_HEADER = 'RIFF'+chr(0x8C)+chr(0x87)+chr(0x00)+chr(0x00)+'WAVEfmt'+chr(0x20)+chr(0x10)+chr(0x00)+chr(0x00)+chr(0x00)+chr(0x01)+chr(0x00)+chr(0x01)+chr(0x00)+'"V'+chr(0x00)+chr(0x00)+'D'+chr(0xAC)+chr(0x00)+chr(0x00)+chr(0x02)+chr(0x00)+chr(0x10)+chr(0x00)+'data'


#'''
#params_u = ar([0.9073, -3.2279, 0.0, -4.0217, 1.0, 0.3882, 0.5847, -0.1, 0.3150, -0.5707, 2.0209, -1.0122, 1.8202, -0.1492, 0.5620, 0.1637, 0.0602, -0.0386])
#params_a = ar([0.3296, -2.3640, 0.0, -4.3032, 0.0994, 0.8196, 1.0, -0.1, -0.4878, -1.2129, 1.9036, -1.5744, 1.3212, -1.0896, 1.0313, -0.1359, 0.4925, 0.0772])
#params_i = ar([0.8580, -2.9237, -0.1488, -1.8808, -0.0321, 0.5695, 0.1438, -0.1, 0.6562, -0.3901, 2.6431, -0.6510, 2.1213, 0.3124, 0.3674, 0.034, -0.1274, -0.2887])
#params_schwa = ar([1.0, -2.643, 0.0, -2.0, -0.07, 0.524, 0.0, -0.1, 0.0, -0.426, -0.767, 2.036, -0.578, 1.163, 0.321, -1.853, -1.7267, 0.0, 0.046, 0.116, 0.116])
#                                                    # prototypical vowel shapes of infant speaker
#params = params_u                                      # arbitrary shape parameters for new speaker (for sensorimotor learning)
#'''


def par_to_wav(params, speaker='adult', simulation_name='', pitch_var=0.0,
               len_var=1.0, verbose=False, rank=1, different_folder='',
               monotone=False):
    """
    Creates a wave file with vocal tract lab out of the given parameters.

    """

    if verbose:
        print('simulating ' + speaker)
    name = speaker + '_' + simulation_name


    if different_folder == '':
        wav_file = os.path.relpath(os.path.join('VTL_API/output/', name, '_',
                                               str(rank), '.wav'))
    else:
        wav_file = os.path.relpath(different_folder)
    area_file = os.path.relpath(os.path.join('VTL_API/output/', name, '_',
                                             str(rank), '.txt'))


    # gestureFile = create_gesture(name, speaker, pitch_var, len_var)
    if not speaker in ('adult', 'infant'):
        raise ValueError("speaker needs to be either 'adult' or 'infant'.")
    if monotone:
        gesture_file = os.path.relpath('VTL_API/gestures/input_%s_monotone.ges' % speaker)
    else:
        gesture_file = os.path.relpath('VTL_API/gestures/input_%s.ges' % speaker)

    speaker_file = create_speaker(speaker, params, name, verbose=verbose, rank=rank)


    # run through vocal tract lab
    LIB_VTL.vtlGesToWav(speaker_file, gesture_file, wav_file, area_file)


    # Repair header of wav File
    with open(wav_file, 'rb') as file_:
        content = file_.read()

    shutil.move(wav_file, wav_file + '.bkup')

    with open(wav_file, 'wb') as newfile:
        newcontent = WAV_HEADER + content[68:]
        newfile.write(newcontent)

    os.remove(wav_file + '.bkup')

    return wav_file

