import numpy as np

def normal_mean(data, variance):
    """ Creates a segment cost function for a time series with a
        Normal distribution with changing mean
    Args:
        data (:obj:`list` of float): 1D time series data
        variance (float): variance
    Returns:
        function: Function with signature
            (int, int) -> float
            where the first arg is the starting index, and the second
            is the last arg. Returns the cost of that segment
    """
    if not isinstance(data, np.ndarray):
        data = np.array(data)

    i_variance_2 = 1 / (variance ** 2)
    cmm = [0.0]
    cmm.extend(np.cumsum(data))
    cmm2 = [0.0]
    cmm2.extend(np.cumsum(np.abs(data)))
    def cost(start, end):
        """ Cost function for normal distribution with variable mean
        Args:
            start (int): start index
            end (int): end index
        Returns:
            float: Cost, from start to end
        """
        cmm2_diff = cmm2[end] - cmm2[start]
        cmm_diff = pow(cmm[end] - cmm[start], 2)
        i_diff = end - start
        diff = cmm2_diff - cmm_diff
        return (diff/i_diff) * i_variance_2

    return cost


def find_min(arr, val=0.0):
    """ Finds the minimum value and index
    Args:
        arr (np.array)
        val (float, optional): value to add
    Returns:
        (float, int): minimum value and index
    """
    return min(arr) + val, np.argmin(arr)

def pelt(cost, length, pen=None):
    """ PELT algorithm to compute changepoints in time series
    Ported from:
        https://github.com/STOR-i/Changepoints.jl
        https://github.com/rkillick/changepoint/
    Reference:
        Killick R, Fearnhead P, Eckley IA (2012) Optimal detection
            of changepoints with a linear computational cost, JASA
            107(500), 1590-1598
    Args:
        cost (function): cost function, with the following signature,
            (int, int) -> float
            where the parameters are the start index, and the second
            the last index of the segment to compute the cost.
        length (int): Data size
        pen (float, optional): defaults to log(n)
    Returns:
        (:obj:`list` of int): List with the indexes of changepoints
    """
    if pen is None:
        pen = np.log(length)

    F = np.zeros(length + 1)
    R = np.array([0], dtype=np.int)
    candidates = np.zeros(length + 1, dtype=np.int)

    F[0] = -pen

    for tstar in range(2, length + 1):
        cpt_cands = R
        seg_costs = np.zeros(len(cpt_cands))
        for i in range(0, len(cpt_cands)):
            seg_costs[i] = cost(cpt_cands[i], tstar)

        F_cost = F[cpt_cands] + seg_costs
        F[tstar], tau = find_min(F_cost, pen)
        candidates[tstar] = cpt_cands[tau]

        ineq_prune = [val < F[tstar] for val in F_cost]
        R = [cpt_cands[j] for j, val in enumerate(ineq_prune) if val]
        R.append(tstar - 1)
        R = np.array(R, dtype=np.int)

    last = candidates[-1]
    changepoints = [last]
    while last > 0:
        last = candidates[last]
        changepoints.append(last)

    return sorted(changepoints)

if __name__ == "__main__":
    size = 100

    var = 0.1
    #data = [1,2,3,4,5,6]
    data = [1] * 5
    data2 = [4] * 20
    data = data + data2

    cost = normal_mean(data, var)
    print(cost(10,25))

    #cp = pelt(normal_mean(data, var), len(data))
