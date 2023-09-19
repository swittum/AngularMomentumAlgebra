from abc import ABC, abstractmethod
import numpy as np


class Operator(ABC):
    def __init__(self, l):
        self.l = l
        self.dimension = round(2*l+1)

    def __repr__(self):
        matrix = self.to_matrix()
        return str(matrix)

    @abstractmethod
    def act_on(self, state):
        """ Return action on quantum state in l-space """

    def to_matrix(self):
        matrix = np.zeros((self.dimension, self.dimension), dtype=complex)
        for i in range(self.dimension):
            state = np.zeros(self.dimension)
            state[i] = 1
            matrix[:, i] = self.act_on(state)
        return matrix
    

class Commutator(Operator):
    def __init__(self, L1: Operator, L2: Operator):
        if L1.l != L2.l:
            raise ValueError('Matrices must operator on same Hilbert space')
        else:
            super().__init__(L1.l)
            self.L1 = L1
            self.L2 = L2
        
    def act_on(self, state):
        out = self.L1.act_on(self.L2.act_on(state))-self.L2.act_on(self.L1.act_on(state))
        return out
    

class L_plus(Operator):
    def __init__(self, l):
        super().__init__(l)

    def act_on(self, state):
        out = np.zeros(self.dimension, dtype=complex)
        for i in range(0, self.dimension-1):
            m = i-self.l
            out[i+1] = np.sqrt(self.l*(self.l+1)-m*(m+1))*state[i]
        return out
    

class L_minus(Operator):
    def __init__(self, l):
        super().__init__(l)
    
    def act_on(self, state):
        out = np.zeros(self.dimension, dtype=complex)
        for i in range(1, self.dimension):
            m = i-self.l
            out[i-1] = np.sqrt(self.l*(self.l+1)-m*(m-1))*state[i]
        return out
    

class L_x(Operator):
    def __init__(self, l):
        super().__init__(l)
        self.l_plus = L_plus(l)
        self.l_minus = L_minus(l)

    def act_on(self, state):
        out = 1/2*(self.l_plus.act_on(state)+self.l_minus.act_on(state))
        return out
    

class L_y(Operator):
    def __init__(self, l):
        super().__init__(l)
        self.l_plus = L_plus(l)
        self.l_minus = L_minus(l)
    
    def act_on(self, state):
        out = 1/(2j)*(self.l_plus.act_on(state)-self.l_minus.act_on(state))
        return out
    

class L_z(Operator):
    def __init__(self, l):
        super().__init__(l)

    def act_on(self, state):
        out = np.zeros(self.dimension, dtype=complex)
        for i in range(self.dimension):
            m = i-self.l
            out[i] = m*state[i]
        return out
    

class L2(Operator):
    def __init__(self, l):
        super().__init__(l)

    def act_on(self, state):
        out = np.copy(state)
        return self.l*(self.l+1)*out
    

class J2_tot(Operator):
    def __init__(self, l, l1, l2):
        if l1+l2 != l:
            raise ValueError(f'l1+l2={l1}+{l2}≠{l}=l')
        super().__init__(l)
        self.l1 = l1
        self.l2 = l2

    def act_on(self, state):
        out = np.copy(state)
        return self.l*(self.l+1)*out
    

class Jz_tot(Operator):
    def __init__(self, l, l1, l2):
        if l1+l2 != l:
            raise ValueError(f'l1+l2={l1}+{l2}≠{l}=l')
        super().__init__(l)
        self.l1 = l1
        self.l2 = l2

    def act_on(self, state):
        pass

    