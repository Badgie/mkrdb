

class MkrdbTheme:
    name = ''
    iden = ''

    background_color = ''
    card_color = ''

    primary_color = ''
    accent_color = ''

    primary_text_color = ''
    secondary_text_color = ''

    navbar_primary_text_color = ''
    navbar_secondary_text_color = ''


class Light(MkrdbTheme):
    name = 'Light'
    iden = 'light'

    background_color = 'white'
    card_color = 'lightgray'

    primary_color = '#177377'
    accent_color = '#11c462'

    primary_text_color = '#161616'
    secondary_text_color = '#3f3f3f'

    navbar_primary_text_color = '#b2b2b2'
    navbar_secondary_text_color = '#7c7c7c'


THEMES = {
    Light.iden: Light
}


def get_theme(request) -> MkrdbTheme:
    # FIXME: collect from user object
    return Light
