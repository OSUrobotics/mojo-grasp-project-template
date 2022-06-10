###Pybullet Imports###
from mojograsp.simcore.episode import EpisodeDefault
from mojograsp.simcore.replay_buffer import ReplayBufferDefault
import pybullet as p
import pybullet_data
import pathlib

###Your Custom Template Classes###
# Most can be optional unless you need to support functionality that doesnt exist
from action_template import ActionTemplate
from reward_template import RewardTemplate
from state_template import StateTemplate
from environment_template import EnvironmentTemplate
from episode_template import EpisodeTemplate
from phase_template import PhaseTemplate
from sim_manager_template import SimManagerTemplate
from replay_buffer_template import ReplayBufferTemplate

###Mojograsp Defaults###
from mojograsp.simcore.sim_manager import SimManagerDefault
from mojograsp.simcore.state import StateDefault
from mojograsp.simcore.action import ActionDefault
from mojograsp.simcore.reward import RewardDefault
from mojograsp.simcore.environment import EnvironmentDefault
from mojograsp.simcore.record_data import RecordDataJSON
from mojograsp.simobjects.two_finger_gripper import TwoFingerGripper
from mojograsp.simobjects.object_base import ObjectBase, ActuatedObject

##################
# Resource Paths # (REQUIRED)
##################
#current_path = str(pathlib.Path().resolve)
#obj1_path = current_path + "/resources/***PATH TO URDF***"
#obj2_path = current_path + "/resources/***PATH TO URDF***"
#data_path = current_path + "/data/"

###############################################
# Start Pybullet, Chance Environment Settings # (REQUIRED)
###############################################
#physics_client = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.setGravity(0, 0, -10)
# p.resetDebugVisualizerCamera(cameraDistance=.02, cameraYaw=0, cameraPitch=-89.9999,
#                             cameraTargetPosition=[0, 0.1, 0.5])

#########################
# Load Pybullet Objects # (REQUIRED)
#########################
#plane_id = p.loadURDF("plane.urdf")

##########################
# Load Mojograsp Objects # (REQUIRED)
##########################
#obj1_id = p.loadURDF(obj1_path, basePosition=[0.0, 0.0, 0.0])
#obj1 = ObjectBase(obj1_id, path=obj1_path)
#obj2_id = p.loadURDF(obj2_path, basePosition=[0.0, 0.0, 0.0])
#obj2 = ActuatedObject(obj2_id, path=obj2_path)

###############
# Environment # (REQUIRED)
###############
# Your environment controls how the sim is stepped, and how your objects and environment
# Should be reset after each episode. This is a Template you will almost always need to do.
#env = EnvironmentTemplate()

#####################################
# Instantiate State, Action, Reward # (OPTIONAL IF NO DATA COLLECTION OR RL)
#####################################
# These are only needed if you wish to use record_data or replay_buffer
# You can also mix and match your own implementation (Templates) with the defaults
#state = StateDefault(objects=[obj1, obj2])
#action = ActionDefault()
#reward = RewardDefault()

##################################
# Data Recording / Replay Buffer # (OPTIONAL FOR NON RL)
##################################
# record data is optional and can be used to record state, action and reward data
# for use in replay_buffer or something else. You may also only include certain data (only state)
# you wish to record like below.
#record_data = RecordDataJSON(data_path=data_path, state=state, save_all=True)

# Replay buffer is also optional and required you to define state, action and reward objects.
#replay_buffer = ReplayBufferDefault(buffer_size=1000, state=state, action=action, reward=reward)

###########
# Episode # (OPTIONAL)
###########
# Episode is optional and only needed if you would like to do something between episodes
# environment usually does anything episode would want to do.
#ep = EpisodeDefault()

#####################
# Sim Manager Setup # (REQUIRED)
#####################
# The sim manager is where you will decide the number of episodes and pass in the
# needed objects, environmnet, record_data, state, action, reward
#manager = SimManagerDefault(num_episodes=1, env=env, record=record_data, state=state, action=action, reward=reward)

###########
# Phase's # (REQUIRED)
###########
#phase1 = PhaseTemplate()
#phase2 = PhaseTemplate()
#manager.add_phase("phase1", phase1, start=True)
#manager.add_phase("phase2", phase2)

###############
# Run the Sim # (REQUIRED)
###############
# manager.run()
#stall is optional
# manager.stall()
