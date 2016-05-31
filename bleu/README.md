This isolates BLEU from grasp.

Requirements:

* numpy
* cython
* python3


# Environment

    
        virtualenv -p python3 ~/workspace/envs/grasp
        source ~/workspace/envs/grasp/bin/activate
        pip install numpy
        pip install cython


# Building


        git clone https://github.com/wilkeraziz/misc.git        
        cd misc/bleu
        python setup.py develop


# Test

The example should produce BLEU=0.84.

        python test.py
