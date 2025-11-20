#!/bin/bash

# Enable error signals
set -e

# Launch hyperparam training
# -r robot (ur)
# -s sensor (tactip)
# -m model (simple_cnn)
# -t task (surface_3d)
# -mv model version (0)
python3 /workspace/ats-meta/tactile_servo_control/tactile_servo_control/learning/launch_hyper_training.py -r ur -s tactip -m simple_cnn -t surface_3d -mv docker-test
exec /bin/bash