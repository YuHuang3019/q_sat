import pytest
import numpy as np
from q_sat.q_sat import q_sat

def test_q_sat():
    # some known results
    # T = 273.15[K], P=100000[Pa], es = 610.55[Pa], q=0.0037
    # not strict test with rtol, use approximation of above test values
    q = q_sat(273.15, 1e5)
    print(q)
    np.testing.assert_allclose(q,0.0037,atol=1e-4)
    
    # now check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
        q_sat('a')
        q_sat('a',1)
