from decimal import Decimal

from pywiki import numbers


def test_convert_atto_to_woo():
    a = numbers.convert_atto_to_woo( 1e18 )
    assert Decimal( 1 ) == a

    b = numbers.convert_atto_to_woo( 1e18 + 0.6 )
    assert Decimal( 1 ) == b

    c = numbers.convert_atto_to_woo( "1" + ( "0" * 18 ) )
    assert Decimal( 1 ) == c

    d = numbers.convert_atto_to_woo( Decimal( 1e18 ) )
    assert Decimal( 1 ) == d


def test_convert_woo_to_atto():
    a = numbers.convert_woo_to_atto( 1e-18 )
    assert Decimal( 1 ) == a

    b = numbers.convert_woo_to_atto( 1.5 )
    assert Decimal( 1.5e18 ) == b

    c = numbers.convert_woo_to_atto( "1" )
    assert Decimal( 1e18 ) == c

    d = numbers.convert_woo_to_atto( Decimal( 1 ) )
    assert Decimal( 1e18 ) == d
