import plot_tsr as pt
import pytest


@pytest.mark.mpl_image_compare
def test_funcion_juego():
    output = pt.funcion_juego(pt.df)
    return output
