from abc import ABC, abstractmethod
from collections import deque
from mixins import LoggerUtil

class IoManagerInf(ABC):
    """ IoManagerInf is the contract that all IO Managers need to implement """
    def __init__(self):
        pass

    @abstractmethod
    def pressed_up(self):
        return True

    @abstractmethod
    def pressed_up_left(self):
        return True
    
    @abstractmethod
    def pressed_up_right(self):
        return True

    @abstractmethod
    def pressed_center(self):
        return True

    @abstractmethod
    def pressed_down(self):
        return True

    @abstractmethod
    def pressed_down_left(self):
        return True

    @abstractmethod
    def pressed_down_right(self):
        return True

    @abstractmethod
    def pressed_left(self):
        return True

    @abstractmethod
    def pressed_right(self):
        return True

    @abstractmethod
    def pressed_trigger_left(self):
        return True
    
    @abstractmethod
    def pressed_trigger_right(self):
        return True

    @abstractmethod
    def pressed_bumper_left(self):
        return True
    
    @abstractmethod
    def pressed_bumper_right(self):
        return True

    @abstractmethod
    def pressed_action_one(self):
        return True

    @abstractmethod
    def pressed_action_two(self):
        return True

    @abstractmethod
    def pressed_action_three(self):
        return True

    @abstractmethod
    def pressed_action_four(self):
        return True


class IoManagerABC(LoggerUtil.LoggerMixIn, IoManagerInf):
    """ IoManagerABC is the class that contains global helper functions for all implementations """
    def __init__(self):
        IoManagerInf.__init__(self)
        LoggerUtil.LoggerMixIn.__init__(self)
        self.get_logger().debug("INIT: IoManagerABC")

class IoManagerStock(IoManagerABC):
    """ IoManagerStock is the class that contains the standard implementation """

    def __init__(self):
        IoManagerABC.__init__(self)
        self.get_logger().debug("INIT: IoManagerStock")
        self._input_queue = deque(maxlen=10)

    def _add_command(self, command_str):
        self.get_logger().debug("_add_command: %s", command_str)
        self._input_queue.appendleft(command_str)
        print('_input_queue:', self._input_queue)

    def get_next_command(self):
        return self._input_queue.pop()

    def pressed_up(self):
        self._add_command("UP")
        return True

    def pressed_up_left(self):
        self._add_command("UL")
        return True
    
    def pressed_up_right(self):
        self._add_command("UR")
        return True

    def pressed_center(self):
        self._add_command("CT")
        return True

    def pressed_down(self):
        self._add_command("DN")
        return True

    def pressed_down_left(self):
        self._add_command("DL")
        return True

    def pressed_down_right(self):
        self._add_command("DR")
        return True

    def pressed_left(self):
        self._add_command("ML")
        return True

    def pressed_right(self):
        self._add_command("MR")
        return True

    def pressed_trigger_left(self):
        self._add_command("TL")
        return True
    
    def pressed_trigger_right(self):
        self._add_command("TR")
        return True

    def pressed_bumper_left(self):
        self._add_command("BL")
        return True
    
    def pressed_bumper_right(self):
        self._add_command("BR")
        return True

    def pressed_action_one(self):
        self._add_command("A1")
        return True

    def pressed_action_two(self):
        self._add_command("A2")
        return True

    def pressed_action_three(self):
        self._add_command("A3")
        return True

    def pressed_action_four(self):
        self._add_command("A4")
        return True
    