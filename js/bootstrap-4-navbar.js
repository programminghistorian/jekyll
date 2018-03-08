
/*!
 * Bootstrap 4 multi dropdown navbar ( https://bootstrapthemes.co/demo/resource/bootstrap-4-multi-dropdown-navbar/ )
 * Copyright 2017.
 * Licensed under the GPL license
 */


$( document ).ready( function () {
    $( '.mobile-drop a.dropdown-toggle' ).on( 'click', function ( e ) {
        console.log('starting click');
        var $el = $( this );
        var $parent = $( this ).offsetParent( ".mobile-drop" );
        if ( !$( this ).next().hasClass( 'show' ) ) {
            $( this ).parents( '.mobile-drop' ).first().find( '.show' ).removeClass( "show" );
            console.log('inside first branch');
        }
        var $subMenu = $( this ).next( ".mobile-drop" );
        $subMenu.toggleClass( 'show' );

        $( this ).parent( "li" ).toggleClass( 'show' );

        $( this ).parents( 'li.nav-item.dropdown.show' ).on( 'hidden.bs.dropdown', function ( e ) {
            $( '.mobile-drop .show' ).removeClass( "show" );
        } );

         if ( !$parent.parent().hasClass( 'navbar-nav' ) ) {
            $el.next().css( { "top": $el[0].offsetTop, "left": $parent.outerWidth() - 4 } );
        }

        return false;
    } );
} );
