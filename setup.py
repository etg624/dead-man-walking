from cx_Freeze import setup, Executable

options = {
    'build_exe': {
        'include_files': ['img/boulder.png',
                          'img/die_right0000.png',
                          'img/die_right0001.png',
                          'img/die_right0002.png',
                          'img/die_right0003.png',
                          'img/die_right0004.png',
                          'img/die_right0005.png',
                          'img/die_right0006.png',
                          'img/idle_left0000.png',
                          'img/idle_left0001.png',
                          'img/idle_left0002.png',
                          'img/idle_left0003.png',
                          'img/idle_left0004.png',
                          'img/idle_left0005.png',
                          'img/idle_left0006.png',
                          'img/idle_left0007.png',
                          'img/idle_left0008.png',
                          'img/idle_left0009.png',
                          'img/idle_left0010.png',
                          'img/walk_right0000.png',
                          'img/walk_right0001.png',
                          'img/walk_right0002.png',
                          'img/walk_right0003.png',
                          'img/walk_right0004.png',
                          'img/walk_right0005.png',
                          'img/walk_right0006.png',
                          'img/walk_right0007.png',
                          'img/grassy_plains.jpg',
                          'sounds/background.ogg',
                          'sounds/hit3.ogg',
                          'sounds/walk.ogg'
                          ]
    }
}

executables = [
    Executable('game.py')
]

setup(name='Dead Man Walking',
      version='1.00',
      author='Evan Guirino',
      executables=executables,
      options=options
      )
