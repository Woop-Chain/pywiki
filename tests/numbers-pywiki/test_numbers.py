from decimal import Decimal

from pywiki import numbers


def test_convert_atto_to_woc():
    a = numbers.convert_atto_to_woc( 1e18 )
    assert Decimal( 1 ) == a

    b = numbers.convert_atto_to_woc( 1e18 + 0.6 )
    assert Decimal( 1 ) == b

    c = numbers.convert_atto_to_woc( "1" + ( "0" * 18 ) )
    assert Decimal( 1 ) == c

    d = numbers.convert_atto_to_woc( Decimal( 1e18 ) )
    assert Decimal( 1 ) == d


def test_convert_woc_to_atto():
    a = numbers.convert_woc_to_atto( 1e-18 )
    assert Decimal( 1 ) == a

    b = numbers.convert_woc_to_atto( 1.5 )
    assert Decimal( 1.5e18 ) == b

    c = numbers.convert_woc_to_atto( "1" )
    assert Decimal( 1e18 ) == c

    d = numbers.convert_woc_to_atto( Decimal( 1 ) )
    assert Decimal( 1e18 ) == d
