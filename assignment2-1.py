import numpy as np
 #
class WeatherSimulation:
    def __init__(self,transition_probabilities,holding_time):
        self.transition_probabilities = transition_probabilities
        self.holding_time = holding_time
        self.state = 'sunny' #we took sunny as initial state
        self.rem_hours = 0
 
        for i,j in transition_probabilities.items():
            s=tuple(j.values())#The values are stored in tuple
            k=sum(s)
            if k != 1:
                raise RuntimeError("Probabilities for " + i + "are not summing up to 1")
 #defining the get state
    def get_states(self):
        return [ x for x in self.transition_probabilities.keys()]
 #it will verify the current state 
    def current_state(self):
        return self.state
 #after getting the new state then it will set the new state into current state
    def set_state(self,new_state):
        self.state = new_state
 #it will show the net state 
    def next_state(self):
        if self.rem_hours <= 0:
            n_state = np.random.choice(list(self.transition_probabilities[self.current_state()].keys()), p = list(self.transition_probabilities[self.current_state()].values()))
            self.set_state(n_state)
            self.rem_hours = self.holding_time[n_state]
        self.rem_hours -= 1
 #here it gives the remaining hours left in the current state
    def current_state_remaining_hours(self):
        return self.rem_hours
 #it will check how many times the states will itterate
    def iterable(self):
        while True:
            self.next_state()
            yield self.current_state()
#creating simulation for the program 
    def simulate(self,hours):
        state_keys=self.transition_probabilities.keys()
        c_states = {k:0 for k in state_keys}
 
        for i in range(hours):
            c_states[self.current_state()] += 1
            self.next_state()
 
        o=[]
        for j in c_states.values():
            o.append((j/hours)*100)
        return o
