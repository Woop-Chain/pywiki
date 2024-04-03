"""
Handles conversion of WOO to ATTO and vice versa
For more granular conversions, see Web3.toWei
"""

from decimal import Decimal

_conversion_unit = Decimal( 1e18 )


def convert_atto_to_woo( atto ) -> Decimal:
    """Convert ATTO to WOO.

    Parameters
    ----------
    atto: str, int, float, decimal
        Value in ATTO to convert to WOO
        Float input will be truncated, since ATTO is the lowest possible denomination of WOO

    Returns
    -------
    decimal
        Converted value in WOO
    """
    if isinstance( atto, float ):
        atto = int( atto )
    return Decimal( atto ) / _conversion_unit


def convert_woo_to_atto( woo ) -> Decimal:
    """Convert WOO to ATTO.

    Parameters
    ----------
    woo: str, int, float, decimal
        Value in WOO to convert to ATTO

    Returns
    -------
    decimal
        Converted value in ATTO
    """
    if isinstance( woo, float ):
        woo = str( woo )
    return Decimal( woo ) * _conversion_unit
