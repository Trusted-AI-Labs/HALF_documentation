# Configuration

| Key | Value | Information |
| :-: | :-: | :-- |
| `experiment_name` | `my_experiment` | Name of your experiment |
| `nb_epochs` | `30` | Number of epochs for the training of the model |
| `seed` | `1` | Random seed to set the experiments |



## `dir`

 Directories to set

| Key | Value | Information |
| :-: | :-: | :-- |
| `model_path` | `"./Models"` | Directories to set Path where to save the models |
| `logs_path` | `"./Logs"` | Path where to save the trainings logs |


## `config_active_learner`

| Key | Value | Information |
| :-: | :-: | :-- |
| `AL_batch_size` | `500` | Number of samples to query at each iteration |
| `budget` | `5000` | Total number of samples to query to the oracle<br />(Opt.) |
| `targeted_accuracy` | `1` | Minimum accuracy to reach for the active learning<br />process to stop (Opt.) |
| `strategy` | `EntropySampling` | Name of the query strategy to use |
| `strategy_args` |  | Parameters specific to the strategy. We advise to<br />you to check the documentation of their respective<br />library for more information. |
| `batch_size` | `64` |  |


## `trainer`

 Trainer configuration, for more information see pytorch-lightning

| Key | Value | Information |
| :-: | :-: | :-- |
| `max_epochs` | `${nb_epochs}` | Trainer configuration, for more information see<br />pytorch-lightning |
| `accelerator` | `gpu` |  |
| `devices` | `1` |  |
| `log_every_n_steps ` | `4` |  |


## `test`


| Key | Value | Information |
| :-: | :-: | :-- |
| `dataloader` | `` |  |
| `batch_size` | `800` |  |
| `num_workers` | `0` |  |


## `train`

| Key | Value | Information |
| :-: | :-: | :-- |
| `dataloader` |  |  |
| `batch_size` | `64` |  |
| `num_workers` | `0` |  |
