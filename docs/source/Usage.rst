Installation and Usage
======================

Why using HALF ?
----------------
Active learning methods helps to reduce labelling cost and time by selecting the most interesting points to label in the data according to what your model has learned up until now.

HALF is agnostic of the model and the dataset, also allowing for a full customisation of the full active learning pipeline, including the training of the model.

Installation
------------
HALF is dockerized, meaning you only need to have `Docker <https://www.docker.com/get-started/>`_ installed and our repository in local to be able to use it.

1. First, you need to clone the repository :

.. code-block:: bash

    git clone

.. seealso::
    
    (Optional) Check that the version of the pytorch image used in the dockerfile found in the folder `Framework` matches your nvidia drivers.



2. Add your custom `Dataset.py` and `Model.py` to import your dataset and models in the `Extensions` folder. You can find examples in the currently existing files.

3. Customise the `config.yaml` in the `Configs` folder according to your needs.

4. Launch the docker with the following instructions from the `root`` folder :

.. code-block:: bash

    docker compose up

5. Admire the process of active learning launching !

Usage
------
Once the docker attached, you can simply launch the process with :

.. code-block:: bash

    python Launcher/main.py

