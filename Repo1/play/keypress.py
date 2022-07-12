import pygame
keypress_map = {
    # use english names like 'space' instead of the space character ' '
    # there is no need of other keys here
    pygame.K_BACKSPACE: 'backspace',
    pygame.K_TAB: 'tab',
    pygame.K_CLEAR: 'clear',
    pygame.K_RETURN: 'enter',
    pygame.K_PAUSE: 'pause',
    pygame.K_ESCAPE: 'escape',
    pygame.K_SPACE: 'space',
    pygame.K_DELETE: 'delete',
    pygame.K_UP: 'up',
    pygame.K_DOWN: 'down',
    pygame.K_RIGHT: 'right',
    pygame.K_LEFT: 'left',
    pygame.K_INSERT: 'insert',
    pygame.K_HOME: 'home',
    pygame.K_END: 'end',
    pygame.K_PAGEUP: 'pageup',
    pygame.K_PAGEDOWN: 'pagedown',
    pygame.K_F1: 'F1',
    pygame.K_F2: 'F2',
    pygame.K_F3: 'F3',
    pygame.K_F4: 'F4',
    pygame.K_F5: 'F5',
    pygame.K_F6: 'F6',
    pygame.K_F7: 'F7',
    pygame.K_F8: 'F8',
    pygame.K_F9: 'F9',
    pygame.K_F10: 'F10',
    pygame.K_F11: 'F11',
    pygame.K_F12: 'F12',
    pygame.K_F13: 'F13',
    pygame.K_F14: 'F14',
    pygame.K_F15: 'F15',
    pygame.K_NUMLOCK: 'numlock',
    pygame.K_CAPSLOCK: 'capslock',
    pygame.K_SCROLLOCK: 'scrollock',
    pygame.K_RSHIFT: 'shift',
    pygame.K_LSHIFT: 'shift',
    pygame.K_RCTRL: 'control',
    pygame.K_LCTRL: 'control',
    pygame.K_RALT: 'alt',
    pygame.K_LALT: 'alt',
    pygame.K_RMETA: 'meta',
    pygame.K_LMETA: 'meta',
    pygame.K_LSUPER: 'super',
    pygame.K_RSUPER: 'super',
}

def pygame_key_to_name(pygame_key_event):
    return keypress_map.get(pygame_key_event.key, pygame_key_event.unicode)
    # use english names if key is in the dictionary
    # use unicode characters in all the other cases including 
    # capital letters, # when shift+3 is pressed
    # and so on.