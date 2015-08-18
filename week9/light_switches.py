class LS:

    def __init__(self, lights, switches):
        self.lights = lights
        self.switches = switches

    def find_switching_seq(self):
        backtrack = dict()
        visited_states = set()
        states = list()
        ind = 0
        first = []
        for light in self.lights:
            if light == 'off':
                first.append(0)
            else:
                first.append(1)
        states.append(first)
        visited_states.add(tuple(states[ind]))

        while ind < len(states):

            for i in range(len(self.switches)):
                new_state = states[ind][:]
                for j in range(len(self.switches)):
                    if self.switches[i][j] == 1 and states[ind][j] == 1:
                        new_state[j] = 0
                    elif self.switches[i][j] == 1 and states[ind][j] == 0:
                        new_state[j] = 1
                if tuple(new_state) not in visited_states:
                    states.append(new_state)
                    backtrack[tuple(new_state)] = (ind, i + 1)

                    visited_states.add(tuple(new_state))


                if 1 not in new_state:

                    res = []
                    index = backtrack[tuple(new_state)][0]
                    current = backtrack[tuple(new_state)]
                    res.append(current[1])
                    while index > 0:
                        previous = states[index]
                        index = backtrack[tuple(previous)][0]
                        current = backtrack[tuple(previous)]
                        res.append(current[1])
                    #print ind
                    return res[::-1]


            ind += 1

        #print states

def main():
    '''lights_inp = input()
    lights = tuple([x for x in lights_inp.split()])
    switches = []
    for i in range(16):
        switches_inp = input()
        switches.append(tuple([int(x) for x in switches_inp.split()]))
    l = LS(lights, switches)
    l.find_switching_seq()'''

    lights = ['on', 'on', 'on', 'off', 'on', 'on', 'on', 'off', 'on', 'on', 'on', 'off', 'on', 'on', 'on', 'off']
    switches = [(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1),
    (0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1), (0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1),
    (0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0), (0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)]

    l = LS(lights, switches)
    print(l.find_switching_seq())

if __name__ == '__main__':
    main()
