"""
Handles conversion of WOC to ATTO and vice versa
For more granular conversions, see Web3.toWei
"""

from decimal import Decimal

_conversion_unit = Decimal( 1e18 )


def convert_atto_to_woc( atto ) -> Decimal:
    """Convert ATTO to WOC.

    Parameters
    ----------
    atto: str, int, float, decimal
        Value in ATTO to convert to WOC
        Float input will be truncated, since ATTO is the lowest possible denomination of WOC

    Returns
    -------
    decimal
        Converted value in WOC
    """
    if isinstance( atto, float ):
        atto = int( atto )
    return Decimal( atto ) / _conversion_unit


def convert_woc_to_atto( woc ) -> Decimal:
    """Convert WOC to ATTO.

    Parameters
    ----------
    woc: str, int, float, decimal
        Value in WOC to convert to ATTO

    Returns
    -------
    decimal
        Converted value in ATTO
    """
    if isinstance( woc, float ):
        woc = str( woc )
    return Decimal( woc ) * _conversion_unit
