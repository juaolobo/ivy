# global
import jax.numpy as jnp
from typing import Union, Optional, Tuple, Literal

# local
from ivy import inf
from ivy.functional.backends.jax import JaxArray

def eigvalsh(x: JaxArray) -> JaxArray:
    
    return jnp.linalg.eigvalsh(x)

# noinspection PyUnusedLocal,PyShadowingBuiltins
def vector_norm(x: JaxArray,
                axis: Optional[Union[int, Tuple[int]]] = None, 
                keepdims: bool = False,
                ord: Union[int, float, Literal[inf, -inf]] = 2)\
        -> JaxArray:

    if axis is None:
        jnp_normalized_vector = jnp.linalg.norm(jnp.ravel(x), ord, axis, keepdims)
    else:
        jnp_normalized_vector = jnp.linalg.norm(x, ord, axis, keepdims)

    if jnp_normalized_vector.shape == ():
        return jnp.expand_dims(jnp_normalized_vector, 0)
    return jnp_normalized_vector


def diagonal(x: JaxArray,
             offset: int = 0,
             axis1: int = -2,
             axis2: int = -1) -> JaxArray:
    return jnp.diagonal(x, offset, axis1, axis2)
